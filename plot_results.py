import opendssdirect as dss

# =====================================
# SMART COLONY DIGITAL TWIN
# =====================================

# Fresh Circuit
dss.Text.Command("Clear")
dss.Text.Command("New Circuit.SmartColony BasekV=11")

# =====================================
# TRANSFORMER
# =====================================

dss.Text.Command(
    "New Transformer.T1 "
    "Phases=3 Windings=2 XHL=5 "
    "wdg=1 bus=SourceBus conn=wye kv=11 kva=1000 %r=1 "
    "wdg=2 bus=LoadBus conn=wye kv=0.415 kva=1000 %r=1"
)

# =====================================
# HOUSE LOADS
# =====================================

dss.Text.Command(
    "New Load.House1 Bus1=LoadBus kV=0.415 kW=50 PF=0.95"
)

dss.Text.Command(
    "New Load.House2 Bus1=LoadBus kV=0.415 kW=75 PF=0.95"
)

dss.Text.Command(
    "New Load.House3 Bus1=LoadBus kV=0.415 kW=100 PF=0.95"
)

# =====================================
# SHOP LOAD
# =====================================

dss.Text.Command(
    "New Load.Shop1 Bus1=LoadBus kV=0.415 kW=80 PF=0.95"
)

# =====================================
# EV CHARGER
# =====================================

dss.Text.Command(
    "New Load.EV1 Bus1=LoadBus kV=0.415 kW=500 PF=0.98"
)

# =====================================
# SOLAR PV
# =====================================

dss.Text.Command(
    "New Generator.Solar1 Bus1=LoadBus kV=0.415 kW=300 PF=1.0"
)

# =====================================
# BATTERY STORAGE
# =====================================

dss.Text.Command(
    "New Storage.Battery1 Bus1=LoadBus "
    "Phases=3 "
    "kV=0.415 "
    "kWRated=200 "
    "kWhRated=500 "
    "%Stored=80 "
    "State=Discharging"
)

# =====================================
# SOLVE
# =====================================

dss.Solution.Solve()

# =====================================
# VOLTAGE
# =====================================

dss.Circuit.SetActiveBus("LoadBus")

voltage = dss.Bus.VMagAngle()[0]

# =====================================
# POWER
# =====================================

source_power = abs(dss.Circuit.TotalPower()[0])

# =====================================
# LOSSES
# =====================================

loss_kw = dss.Circuit.Losses()[0] / 1000

# =====================================
# REPORT
# =====================================

print("\n===================================")
print(" SMART COLONY DIGITAL TWIN REPORT ")
print("===================================\n")

print(f"Load Voltage      : {voltage:.2f} V")
print(f"Source Power      : {source_power:.2f} kW")
print(f"System Loss       : {loss_kw:.2f} kW")
print(f"Loss Percentage   : {(loss_kw/source_power)*100:.2f} %")

print("\nConnected Loads:")
print(dss.Loads.AllNames())

print("\nResources:")
print("Solar PV          : 300 kW")
print("Battery Storage   : 200 kW")
print("EV Charger        : 500 kW")

print("\nTransformer:")
print("Rating            : 1000 kVA")

print("\n===================================")
print(" Simulation Complete ")
print("===================================\n")