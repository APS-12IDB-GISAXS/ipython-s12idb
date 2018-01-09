print(__file__)
from ophyd import (PVPositioner, EpicsMotor, EpicsSignal, EpicsSignalRO,
                   PVPositionerPC, Device)
from ophyd import Component as Cpt

class MotorDialValues(Device):
	value = Cpt(EpicsSignalRO, ".DRBV")
	setpoint = Cpt(EpicsSignal, ".DVAL")

class MyEpicsMotorWithDial(EpicsMotor):
	dial = Cpt(MotorDialValues, "")

# m1 = MyEpicsMotorWithDial('12idb:m1', name='m1')

chi = EpicsMotor('12idb:m1', name='chi')
crl_z = EpicsMotor('12idb:m2', name='crl_z')
pitch = EpicsMotor('12idb:m3', name='pitch')
yaw = EpicsMotor('12idb:m4', name='yaw')
theta = EpicsMotor('12idb:m5', name='theta')
sample_v = EpicsMotor('12idb:m6', name='sample_v')
sample_h = EpicsMotor('12idb:m7', name='sample_h')
phi = EpicsMotor('12idb:m8', name='phi')
