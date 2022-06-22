import libhousy
import time
timer = time.time()
right = True
#You can define helper functions here, make sure to but them *above* the main function
target_color = (255, 0 ,0)
def main(robot: libhousy.robot):
    #Here is where your recurring code will go

    if robot.colorSensor.getColor() == target_color:
        robot.rDrive.Set(1)
        robot.lDrive.Set(1)
    else:
        if right:
            robot.lDrive.Set(.6)
            robot.rDrive.Set(0)
        else:
            robot.lDrive.Set(0)
            robot.rDrive.Set(.6)
            
    if time.time() - timer > 2:
        timer = time.time()
        right = not right        