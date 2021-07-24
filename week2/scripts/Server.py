#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from week2.srv import ReturnPoses,ReturnPosesResponse
import numpy as np


class Unicycle:
    def _init_(self, x, y, theta, dt=0.05):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v, w, n=50):
    
        for i in range(n):
            self.theta += w*self.dt   # angle = angle + angular_velociy * delta
            self.x += v*np.cos(self.theta)*self.dt # X = X + horizontal_velocity * delta
            self.y += v*np.sin(self.theta)*self.dt # Y = Y + vertical_velocity * delta
            self.x_points.append(self.x)
            self.y_points.append(self.y)

        return self.x_points, self.y_points


def handle_return_traj(req):
    uni = Unicycle(req.x, req.y, req.theta)
    resp = uni.step(req.v, req.w)
    return ReturnPosesResponse(resp[0], resp[1])


def return_traj_server():
    rospy.init_node('return_traj_server')
    s = rospy.Service('return_poses', ReturnPoses, handle_return_traj)
    rospy.loginfo('Available to return Trajectory')
    rospy.spin()


if __name__ == "__main__":
    return_traj_server()
