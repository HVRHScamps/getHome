import libhousy
import time
timer = time.time()
right = True
#You can define helper functions here, make sure to but them *above* the main function
target_color = (255, 0 ,0)

def myFunction(color: tuple):
    if color[0] > color[1] and color[0] > color[2]:
            return "red"
    elif color[1] > color[0] and color[1] > color[2]:
            return "green"
    elif color[2] > color[0] and color[2] > color[1]:
            return "blue"
def main(robot: libhousy.robot):
    global right, timer
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
        