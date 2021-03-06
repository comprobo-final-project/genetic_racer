#!/usr/bin/env python


"""
The Supervisor class is needed to create a single package that can be sent to all Chromosomes to allow them
to each calculate their own fitness using the simulation components in this class
"""


from simulator.robot import Robot
from robot_controller import RobotController


class Supervisor(object):
    """
    evaluator class that holds the components needed for simulation and
    determining fitness
    """

    def __init__(self):

        self.robot = Robot()
        self.robot.pose.position.x = 3.0
        self.robot.pose.position.y = 5.0
        self.robot_controller = RobotController(self.robot)


    def use_genes(self, genes):
        """
        receives this current iteration of the genes
        """

        self.robot_controller.set_genes(genes)


    def reset(self):
        """
        resets the simulation for the next usage
        """

        # Give the robot a random position r meters away from the goal
        self.robot.set_random_position(r=5.0)

        # Give the robot a random direction
        self.robot.set_random_direction()


    def run(self):
        """
        main run function
        """

        return self.robot_controller.run(20)


if __name__ == '__main__':

    node = Supervisor()
    genes = [1.0, 2.0, 3.0, 4.0]
    node.use_genes(genes)
    node.run()
