from config import *
from Utils import *
from resetAndMotor import *

def littleUpMotor():
    up_motor.run_angle(rotation_angle=-45, speed=1000, then=Stop.HOLD)
    
def putRockets():
    base.sync_acc(215)
    up_motor.run_time(speed=-1000,time=1000, then=Stop.HOLD)
    up_motor.hold()
    base.turn(180)
    base.sync_acc(150)
    up_motor.run_time(speed=1000,time=1000, then=Stop.HOLD)
    littleUpMotor()
    base.sync_acc(-200 , 1000)
    up_motor.hold()
    base.turn(90) 

def battary():
    base.move_until_black(-1000)
    base.stop()
    base.sync_acc(-40)
    line.turn_to_line(dis = -1 , angle=-90)
    wait(100)

    line.followUntilSensor(speed=-70)
    wait(50)
    line.followUntilSensor(speed=-70)
    wait(50)

    base.sync_acc(-30)
    line.turn_to_line(dis = -1 , angle=-90)
    line.follow_cm(distance_cm=38, speed=-60)
    base.stop()
    base.turn(-100)
    base.sync_acc(400)
    up_motor.run_time(speed=-1000 , time=800)
    up_motor.hold()
    base.stop()
    ##############################
    #backword
    base.move_until_black(-1000)
    base.stop_and_hold()
    base.sync_acc(-50)
    line.turn_to_line(dis = -1 , angle=-90)
    line.follow_cm(distance_cm=20, speed=-60)
    line.followUntilSensor(dis=1 ,speed=-70)
    base.sync_acc(-30)
    line.turn_to_line(dis = -1 , angle=90 )
    line.follow_cm(distance_cm=28.5, speed=-70)
    line.followUntilSensor(dis=1 ,speed=-70)
    base.sync_acc(-30)
    line.turn_to_line(dis = -1 , angle=90)
    line.followUntilSensor(speed=-70)
    base.stop_and_hold()
    base.sync_acc(300)
    wait(100)
    base.turn(9)
    up_motor.run_time(speed=1000,time=450, then=Stop.HOLD)
    base.sync_acc(-50)
    base.turn(-11)
    base.move_until_black(speed=-500)
    base.sync_acc(-30)
def theater ():
    # up_motor.run_time(speed=1000 , time=150)
    #base.move_until_black(speed=-500)
    #base.sync_acc(-30)
    line.followUntilSensor(speed=-50)
    base.sync_acc(-30)
    wait(500)
    ReadColorC(left_sensor,1)
    wait(500)
    base.sync_acc(-30)
    wait(500)  
    ReadColorC(right_sensor,2)
    wait(500)
    base.turn(90)
    base.sync_acc(-50)
    base.turn(-90)
    base.sync_acc(-310)
    ReadColorB(up_right_sensor,1)
    wait(500)
    base.turn(90)
    base.sync_acc(130)
    base.turn(-90)
    wait(1000)
    ReadColorB(up_left_sensor,2)
    base.turn(180)
    #up_motor.run_angle(rotation_angle=30, speed=1000, then=Stop.HOLD)
    base.move_until_black(speed=-500)
    base.sync_acc(-30)
    line.turn_to_line(dis = -1 , angle=-90)

def breaker ():
   
    line.follow_cm(distance_cm=30, speed=-70)
    wait(500)
    line.followUntilSensor(speed=-70)
    # base.turn(180)
    line.turn_to_line(dis = -1 , angle=-90)
    base.sync_acc(300)
    up_motor.run_time(speed=-1000 , time= 1000)
    base.sync_acc(-60)
    base.sync_acc(55)
    up_motor.run_time(speed=1000 , time= 600)
    up_motor.run_time(speed=-1000 , time= 600)
    base.sync_acc(-50)
    up_motor.run_time(speed=1000 , time= 400)
    base.turn(15)





















































def TakingBlocks():
    #first block
    base.move_until_black(speed=-500)
    base.sync_acc(-30)
    line.turn_to_line(dis = -1 , angle=90)
    line.follow_cm(distance_cm=30, speed=-50)
    line.followUntilSensor(speed=-50)
    base.sync_acc(50)
    color1 = COLOR[1]
    if color1 == 1:
        base.turn(90)
        base.sync_acc(-90)
        base.turn(-95)
        base.sync_acc(-110)
        upClaw()
        base.sync_acc(200)
        base.turn(-90)
        base.move_until_black(speed=-500)
        base.sync_acc(-30)
        line.turn_to_line(dis = -1 , angle=90)
        line.followUntilSensor(speed=-30)
    elif color1 == 2:
        base.turn(-90)
        base.sync_acc(-90)
        base.turn(90)
        base.sync_acc(-110)
        upClaw()
        base.sync_acc(200)
        base.turn(90)
        base.move_until_black(speed=-500)
        base.sync_acc(-40)
        line.turn_to_line(dis = -1 , angle=-90)
        line.followUntilSensor(speed=-30)
    elif color1 == 3:
        base.sync_acc(-80)
        upClaw()
        base.sync_acc(80)
        line.followUntilSensor(speed=-30)
    #second block
    base.sync_acc(50)
    color1 = COLOR[2]
    if color1 == 1:
        base.turn(90)
        base.sync_acc(-90)
        base.turn(-90)
        base.sync_acc(-110)
        upClawTwo()
        base.sync_acc(200)
        base.turn(-90)
        base.move_until_black(speed=-500)
        base.sync_acc(-30)
        line.turn_to_line(dis = -1 , angle=90)
        line.followUntilSensor(speed=-30)
    elif color1 == 2:
        base.turn(-90)
        base.sync_acc(-90)
        base.turn(90)
        base.sync_acc(-100)
        upClawTwo()
        base.sync_acc(200)
        base.turn(90)
        base.move_until_black(speed=-500)
        base.sync_acc(-30)
        line.turn_to_line(dis = -1 , angle=-90)
        line.followUntilSensor(speed=-30)
    elif color1 == 3:
        base.sync_acc(-80)
        upClawTwo()
        base.sync_acc(80)
        line.followUntilSensor(speed=-30)


#to read colors on the ground
def ReadColorC(sensor, ind):
    h, s, v = sensor.hsv()
    if h <= 20 and h > 0:
        COLORS[ind] = 1
        print("red")
    elif h <= 155 and h >= 85:
        COLORS[ind] = 2
        print("green")
    else:
        COLORS[ind] = 3
        print("white")

#to read colors on the mini castles   
def ReadColorB(sensor, ind):
    h, s, v = sensor.hsv()
    if h <= 250 and h >= 175:
        COLOR[ind] = 1
        print("blue")
    elif h <= 80 and h >= 40:
        COLOR[ind] = 2
        print("yellow")
    else:
        COLOR[ind] = 3
        print("black")   
    


