"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50

Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]
        self.theta_points=[self.theta]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.

        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps

        Return:
            x, y, theta (float): final pose 
        """
        
        
        
        i=0
        for i in range(n):
            self.theta+=w*(self.dt)
            self.x+=v*np.cos(self.theta)*self.dt
            self.y+=v*np.sin(self.theta)*self.dt
            self.x_points.append(self.x)
            self.y_points.append(self.y)
            self.theta_points.append(self.theta)

        
        return self.x_points,self.y_points,self.theta_points

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        #plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")
    Object1=Unicycle(0,0,0,.1)
    Final_pose1=Object1.step(1,.5,25)
    Object1.plot(1,.5)
    print("The final pose for 1 is:   ",Final_pose1)
    Object2=Unicycle(0,0,1.57,.2)
    Final_pose2=Object2.step(.5,1,10)
    Object2.plot(.5,1)
    print("The final pose of 2 is:   ",Final_pose2)
    Object3=Unicycle(0,0,0.77,.05)
    Final_pose3=Object3.step(5,4,50)
    Object3.plot(5,4)
    print("The final pose of 3 is:   ",Final_pose3)      
          

    # make an object of the robot and plot various trajectories
