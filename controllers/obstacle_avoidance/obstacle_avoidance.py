
from controller import Robot
import random

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

# Sensors
sensors = []

for i in range(8):
    sensor = robot.getDevice("ps" + str(i))
    sensor.enable(timestep)
    sensors.append(sensor)

speed = 3
threshold = 100
obstacle_count = 0

def move(left, right):
    left_motor.setVelocity(left)
    right_motor.setVelocity(right)

def move_for(left, right, seconds):
    move(left, right)

    steps = int(seconds * 1000 / timestep)

    for i in range(steps):
        if robot.step(timestep) == -1:
            return False

    return True

print("Smart Obstacle Avoidance Started!", flush=True)

while robot.step(timestep) != -1:

    values = []

    for sensor in sensors:
        values.append(sensor.getValue())

    right_obstacle = max(values[0], values[1]) > threshold
    left_obstacle = max(values[6], values[7]) > threshold

    if left_obstacle or right_obstacle:

        obstacle_count += 1
        print("Obstacle detected:", obstacle_count, flush=True)

        # Reverse away from obstacle
        if not move_for(-3.0, -3.0, 0.8):
            break

        # Alternate escape direction when both sides are blocked
        if left_obstacle and not right_obstacle:
            direction = "right"
        elif right_obstacle and not left_obstacle:
            direction = "left"
        else:
            direction = random.choice(["left", "right"])

        # Make a larger turn
        turn_time = random.uniform(0.9, 1.5)

        if direction == "left":
            if not move_for(-3.0, 3.0, turn_time):
                break
        else:
            if not move_for(3.0, -3.0, turn_time):
                break

        # Try moving forward
        if not move_for(3.0, 3.0, 0.4):
            break

    else:
        move(speed, speed)
