import opendssdirect as dss

# Fresh Circuit
dss.Text.Command("Clear")
dss.Text.Command("New Circuit.MyCircuit BasekV=11")

# Transformer
dss.Text.Command(
    "New Transformer.T1 "
    "Phases=3 "
    "Windings=2 "
    "XHL=5 "
    "wdg=1 bus=SourceBus conn=wye kv=11 kva=1000 %r=1 "
    "wdg=2 bus=LoadBus conn=wye kv=0.415 kva=1000 %r=1"
)

# Load at LT side
dss.Text.Command(
    "New Load.Load1 Bus1=LoadBus kV=0.415 kW=900 PF=0.95"
)

# Solve
dss.Solution.Solve()

# Check voltage on LT bus
dss.Circuit.SetActiveBus("LoadBus")

print("Load Bus Voltage:")
print(dss.Bus.VMagAngle())
print("Total Power:")
print(dss.Circuit.TotalPower())

print("Losses:")
print(dss.Circuit.Losses())

v = dss.Bus.VMagAngle()[0]

p = abs(dss.Circuit.TotalPower()[0])

loss = dss.Circuit.Losses()[0] / 1000

print("\n===== SYSTEM REPORT =====")
print(f"Load Voltage = {v:.2f} V")
print(f"Source Power = {p:.2f} kW")
print(f"System Loss = {loss:.2f} kW")
print(f"Loss Percentage = {(loss/p)*100:.2f}%")