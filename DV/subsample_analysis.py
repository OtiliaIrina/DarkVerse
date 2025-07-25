import numpy as np
from scipy.integrate import quad
import scipy.integrate as integrate
from astropy.cosmology import Planck15


from astropy.coordinates import SkyCoord
from astropy import units as u

from astropy.cosmology import FlatLambdaCDM
from DarkVerse.cosmology import Cosmology


# class that calculates the comoving correlation length (R_0) for a subsample based on its properties

class SubsampleAnalysis:
    def __init__(self, delta, A, z_mean, delta_z, H_gamma=3.68, c=299792.458):
        self.delta = delta
        self.A = A
        self.z_mean = z_mean
        self.delta_z = delta_z
        self.H_gamma = H_gamma
        self.c = c


        # Create a Cosmology object using the imported class
        #self.cosmo = Cosmology(H0=70, Omega0=0.3)
        #self.cosmo = Planck15
        self.cosmo = Cosmology(H0=67, Omega0=0.3)





    def calculate_r0(self):
        print(type(self.A))
        gamma = 1.8
        #gamma = (self.delta * -1) + 1
        print(gamma)
        numerator = self.c * self.A * self.delta_z

        denominator = self.cosmo.H0 * self.H_gamma * self.cosmo.x(self.z_mean) ** (1 - gamma) * self.cosmo.P(self.z_mean) *self.cosmo.F(self.z_mean)
        r0 = (numerator / denominator) ** (1 / gamma)
        
        return r0
