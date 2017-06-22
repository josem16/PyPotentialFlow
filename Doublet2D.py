import numpy as np

class Doublet2D(object):
    """
    Class method for modeling 2D doublet potential flow singularities.
    """

    def __init__(self, location, strength):
        self.flow_type = 'doublet'
        self.location = location
        self.strength = strength

    @property
    def xs(self):
        return self.location[0]

    @xs.setter
    def xs(self, value):
        self.location[0] = value

    @property
    def ys(self):
        return self.location[1]

    @ys.setter
    def ys(self, value):
        self.location[1] = value

    def get_velocity(self, xVals, yVals):
        """
        Computes the veocity induced at a point(s)
        """
        # Multipliers
        m1 = self.strength/(2*np.pi)
        m2 = 1./((xVals - self.xs)**2 + (yVals - self.ys)**2)**2

        # Compute and return velocities
        Vx = m1*m2*((yVals - self.ys)**2 - (xVals - self.xs)**2)
        Vy = m1*m2*-2*(xVals - self.xs)*(yVals - self.ys)
        return Vx,Vy

    def get_stream_function(self, xVals, yVals):
        """
        Computes the stream function at a point(s)
        """
        m1 = self.strength/(2*np.pi)
        psi = m1*-1*(yVals - self.ys)/((xVals - self.xs)**2 + (yVals - self.ys)**2)
        return psi

    def get_velocity_potential(self, xVals, yVals):
        """
        Computes the velocity potential at a point(s)
        """
        m1 = self.strength/(2*np.pi)
        phi = m1*(xVals - self.xs)/((xVals - self.xs)**2 + (yVals - self.ys)**2)
        return phi
