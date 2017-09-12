import numpy as np  #external library for numerical calculations
import matplotlib.pyplot as plt # plotting library

# derived quantities

nt = 100
nx = 100   # number of points in space
u = 1.
dx = 1./nx
dt = 1
t = nt * dt
k= 1*10**(-5) # diffusion coefficient
d= k*dt/dx**2
# Function defining the initial and analytical solution

def initialBell(x):
    return np. where(x%1. <0.5, np.power(np.sin(2*x*np.pi), 2), 0)

# setup space, initial phi profile and Courant number



# spatial variable going from zero to one inclusive

x = np.linspace(0.0, 1.0, nx+1)

# three time levels of the dependent variable, phi

phi = initialBell(x)
phiNew = phi.copy()
phiOld = phi.copy()

# FTCS for the first time-step
# loop over space

for j in range (1, nx):

    phi[j] = phiOld[j] + d*(phiOld[j+1] +phiOld[j-1] -2*phiOld[j])

# apply periodic boundary conditions

phi[0] = phiOld[0] + d*(phiOld[1] + phiOld[nx-1] -2*phiOld[0])
phi[nx] = phi[0]

# Loop over remaining time-steps (nt) using CTCS

nt = 20

for n in xrange (1, nt):
    # loop over space
    for j in xrange (1, nx):
         phiNew[j] = phiOld[j] + d*(phi[j+1] + phi[j-1] -2*phi[j])
    #apply periodic boundary conditions

    phiNew[0] = phiOld[0] + d*(phi[1] + phi[nx-1] -2*phi[0])
    phiNew[nx] = phiNew[0]

    #update phi for the next time-step
    phiOld = phi.copy()
    phi = phiNew.copy()



# Plot the solution in comparison to the analytic solution

plt.plot(x, initialBell(x - u*t), 'k' , label = 'analytic')
plt.plot(x,phi, 'b', label='CTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':',color='black')
plt.show()


