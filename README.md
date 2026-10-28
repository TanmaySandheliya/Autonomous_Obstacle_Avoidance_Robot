# Autonomous Obstacle Avoidance Robot Using Webots

## Project Overview

This project demonstrates an **Autonomous Obstacle Avoidance Robot** developed using the Webots robotics simulation software. The robot navigates through a simulated environment and automatically detects and avoids obstacles without human intervention.

The simulation consists of **one mobile robot and four solid boxes** placed as obstacles in the environment.

## Objectives

- To design and simulate an autonomous mobile robot using Webots.
- To implement obstacle detection and avoidance using sensors.
- To enable the robot to navigate without colliding with obstacles.
- To understand basic autonomous robot navigation and control.

## Software and Technologies Used

- **Simulation Software:** Webots
- **Programming Language:** Python
- **Robot:** Mobile robot equipped with distance sensors
- **Environment:** Simulated world containing four solid box obstacles

## Simulation Environment

The Webots simulation environment contains:

1. **One Autonomous Robot:** A mobile robot programmed to move and avoid obstacles.
2. **Four Solid Boxes:** Stationary obstacles placed at different positions in the environment.
3. **Distance Sensors:** Used to detect obstacles in the robot's path.
4. **Simulation World:** A virtual environment where the robot performs autonomous navigation.

## Working Principle

The robot uses a sensor-based obstacle avoidance mechanism.

1. The robot starts moving forward.
2. Distance sensors continuously monitor the surroundings.
3. When an obstacle is detected within a predefined distance, the robot changes its movement direction.
4. The robot turns to avoid the obstacle.
5. Once the path is clear, the robot continues moving forward.
6. This process repeats as the robot navigates around the four solid boxes.

## Project Structure

```text
Autonomous-Obstacle-Avoidance-Robot/
│
├── worlds/
│   └── ObstacleAvoidanceRobot.wbt
│
├── controllers/
│   └── obstacle_avoidance/
│       └── obstacle_avoidance.py
│
└── README.md
```

*Note: File and controller names may differ