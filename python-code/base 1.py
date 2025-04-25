import orientation
from hub import motion_sensor
from hub import port
import runloop
import motor_pair
import motor
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

async def goforward(vzdalenost, speed):
    motion_sensor.reset_yaw(0)
    pozice = 0
    motor.reset_relative_position(port.A, 0)
    motor.reset_relative_position(port.B, 0)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
    while vzdalenost > pozice:
        pozice = motor.relative_position(port.A) * -1 + motor.relative_position(port.B) /720 * 27.6
        motor_pair.move_tank(motor_pair.PAIR_1, 1000, 1000)
        
        await runloop.sleep_ms(100)
    motor_pair.stop(motor_pair.PAIR_1)



async def main():
    #runloop.run(goforward(1000, 1))
    motion_sensor.reset_yaw(0)
    while True:
        print(motion_sensor.tilt_angles()[0])    
        await runloop.sleep_ms(40)
runloop.run(main())
