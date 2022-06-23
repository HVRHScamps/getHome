import libhousy
import time
timer = time.time()
right = True
# You can define helper functions here, make sure to but them *above* the main function
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
    # Here is where your recurring code will go

    # So we don't ever call myFunction which does our color decision.
    # Instead of the if below, do something like if myFunction(robot.colorSensor.getColor()) == "red"
    if myFunction(robot.colorSensor.getColor()) == "red":
        robot.rDrive.Set(.6)
        robot.lDrive.Set(.6)
    elif myFunction(robot.colorSensor.getColor()) == "blue":
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
    else:
        if right:
            robot.lDrive.Set(.3)
            robot.rDrive.Set(0)
        else:
            robot.lDrive.Set(0)
            robot.rDrive.Set(.3)

    if time.time() - timer > 2:
        timer = time.time()
        right = not right        
        