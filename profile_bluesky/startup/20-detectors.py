print(__file__)

"""various detectors and other signals"""

aps_current = EpicsSignalRO("S:SRcurrentAI", name="aps_current")
userCalcs_12idb = userCalcsDevice("12idb:", name="userCalcs_12idb")
scaler = EpicsScaler('12idb:scaler1', name='scaler')
