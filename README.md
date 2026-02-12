# Car in the Maze - Intelligent Agent 🚗🧩

## About the Project
This project was developed for the **Intelligent Systems** (Sistemas Inteligentes) course at the Faculty of Sciences, University of Lisbon (2023/2024).

The objective is to implement an intelligent agent capable of controlling a car within a discrete maze. The agent must use **State-Space Search** techniques to find a plan that moves the car from a starting position to a designated exit, minimizing the number of actions used.

## The Challenge
Unlike simple pathfinding, this problem incorporates vehicle dynamics (inertia and orientation).

### The Agent
* **State:** The car has a specific position $(x, y)$, an orientation (North, South, East, West), and a variable velocity.
* **Actions:** In a single step, the agent can change its orientation (turn left/right) or adjust its velocity (accelerate/brake) to move forward.
* **Physics:** The car cannot stop instantly; it must manage its speed to avoid crashing into walls and to stop exactly at the goal.

### The Environment
The maze is a grid of $L \times C$ cells containing:
* **Walls:** Impassable obstacles.
* **Swamp Areas:** Zones that limit the maximum speed of the vehicle (e.g., max speed 1).
* **Normal Road:** Standard movement areas.
* **Exit:** The target square where the car must park.

### The Goal
The agent must generate a sequence of actions (a plan) to:
1.  Navigate from the start point.
2.  Avoid obstacles.
3.  Reach the exit square.
4.  **Stop completely** (velocity = 0) at the exit.

## Implementation
The core logic is encapsulated in the `Labirinto` class using **Python**.

* **Search Strategy:** The solution involves modeling the problem as a graph search, exploring states (Position + Orientation + Velocity) to find the optimal path.
* **File Structure:** The main logic is contained in `Labirinto_SInt_23_24_grupoXX.py`.



---
*This project was developed for educational purposes.*
