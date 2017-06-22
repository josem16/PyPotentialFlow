import numpy as np

class Uniform2D(object):
    """
    Class method for modeling 2D uniform potential flows.
    """

    def __init__(self, magnitude, direction):
        self.flow_type = 'uniform'
        self.magnitude = magnitude
        self.direction = direction

    def get_velocity(self, xVals, yVals):
        """
        Computes the veocity induced at a point(s)
        """
        # Compute and return velocities
        mx, my = self.magnitude*self.direction
        Vx = mx*np.ones(xVals.shape)
        Vy = my*np.ones(yVals.shape)
        return Vx,Vy

    def get_stream_function(self, xVals, yVals):
        """
        Computes the stream function at a point(s)
        """
        mx, my = self.magnitude*self.direction
        psi = mx*yVals + my*xVals
        return psi

    def get_velocity_potential(self, xVals, yVals):
        """
        Computes the velocity potential at a point(s)
        """
        mx, my = self.magnitude*self.direction
        phi = mx*xVals + my*yVals
        return phi

