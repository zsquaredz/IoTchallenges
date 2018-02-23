import ev3dev.ev3 as ev3

def main():
    """
    To be run at the first client demonstration.
    """

    # declaring variables
    motorLeft  = ev3.LargeMotor("outA")
    motorRight = ev3.LargeMotor("outD")

    # gyro       = ev3.UltrasonicSensor("in4")
    # ultrasonic = ev3.UltrasonicSensor("in1")

    csTapeL = ev3.ColorSensor("in3")
    csTapeR = ev3.ColorSensor("in2")

    # start movement
    motorLeft.run_forever(speed_sp=-200)
    motorRight.run_forever(speed_sp=-200)

    while True:
        print("Left: {} Right: {}".format(csTapeL.color, csTapeR.color))
        if csTapeL.color == 1 and not csTapeR.color == 1:
            motorLeft.run_forever(speed_sp=0)
            motorRight.run_forever(speed_sp=-100)
        elif csTapeR.color == 1 and not csTapeL.color == 1:
            motorLeft.run_forever(speed_sp=-100)
            motorRight.run_forever(speed_sp=0)
        else:
            motorLeft.run_forever(speed_sp=-200)
            motorRight.run_forever(speed_sp=-200)


if __name__ == '__main__':
    main()
