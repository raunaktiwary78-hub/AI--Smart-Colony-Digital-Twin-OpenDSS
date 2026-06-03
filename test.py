import opendssdirect as dss

dss.Text.Command("Clear")
dss.Text.Command("New Circuit.MyCircuit BasekV=11")

# Linecode
dss.Text.Command("New Linecode.MyCode R1=0.1 X1=0.2 R0=0.3 X0=0.6 Units=km")

# Line
dss.Text.Command(
    "New Line.Line1 Bus1=SourceBus Bus2=LoadBus Length=5 Units=km Linecode=MyCode"
)

# Load
dss.Text.Command(
    "New Load.Load1 Bus1=LoadBus kV=11 kW=15000 PF=0.95"
)

dss.Solution.Solve()

dss.Circuit.SetActiveBus("LoadBus")

print("Load Bus Voltage:")
print(dss.Bus.VMagAngle())
print("Total Power:")
print(dss.Circuit.TotalPower())

print("Losses:")
print(dss.Circuit.Losses())