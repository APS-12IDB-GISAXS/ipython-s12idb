print(__file__)

"""motors, stages, positioners, ..."""

# m1 = MyEpicsMotorWithDial('12idb:m1', name='m1')

chi      = EpicsMotor('12idb:m1', name='chi')
crl_z    = EpicsMotor('12idb:m2', name='crl_z')
pitch    = EpicsMotor('12idb:m3', name='pitch')
yaw      = EpicsMotor('12idb:m4', name='yaw')
theta    = EpicsMotor('12idb:m5', name='theta')
sample_v = EpicsMotor('12idb:m6', name='sample_v')
sample_h = EpicsMotor('12idb:m7', name='sample_h')
phi      = EpicsMotor('12idb:m8', name='phi')

append_wa_motor_list(chi, crl_z, pitch, yaw, theta, sample_h, sample_v, phi)
