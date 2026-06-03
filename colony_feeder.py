import opendssdirect as dss

# Fresh Circuit
dss.Text.Command("Clear")
dss.Text.Command("New Circuit.Colony BasekV=11")

# Transformer
dss.Text.Command(
    "New Transformer.T1 "
    "Phases=3 Windings=2 XHL=5 "
    "wdg=1 bus=SourceBus conn=wye kv=11 kva=1000 %r=1 "
    "wdg=2 bus=LoadBus conn=wye kv=0.415 kva=1000 %r=1"
)

# House Loads
dss.Text.Command(
    "New Load.House1 Bus1=LoadBus kV=0.415 kW=50 PF=0.95"
)

dss.Text.Command(
    "New Load.House2 Bus1=LoadBus kV=0.415 kW=75 PF=0.95"
)

dss.Text.Command(
    "New Load.House3 Bus1=LoadBus kV=0.415 kW=100 PF=0.95"
)

# Shop
dss.Text.Command(
    "New Load.Shop1 Bus1=LoadBus kV=0.415 kW=80 PF=0.95"
)

# EV Charger
dss.Text.Command(
    "New Load.EV1 Bus1=LoadBus kV=0.415 kW=500 PF=0.98"
)
dss.Text.Command(
    "New Generator.Solar1 Bus1=LoadBus kV=0.415 kW=300 PF=1.0"
)

# Solve
dss.Solution.Solve()

# Voltage
dss.Circuit.SetActiveBus("LoadBus")
v = dss.Bus.VMagAngle()[0]

# Power & Losses
p = abs(dss.Circuit.TotalPower()[0])
loss = dss.Circuit.Losses()[0] / 1000

print("\n===== SMART COLONY REPORT =====")
print(f"Load Voltage = {v:.2f} V")
print(f"Source Power = {p:.2f} kW")
print(f"System Loss = {loss:.2f} kW")
print(f"Loss Percentage = {(loss/p)*100:.2f}%")

print("\nLoads Connected:")
print(dss.Loads.AllNames())