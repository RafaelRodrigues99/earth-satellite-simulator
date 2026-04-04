import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation


ray_earth = 6371
ray_orbit = 12000



fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15000,15000)
ax.set_ylim(-15000,15000)
ax.set_title('Satellite simulator orbiting the Earth')

#Earth

earth = plt.Circle((0,0), ray_earth, fill=True)
ax.add_patch(earth)

#Orbit

orbit = plt.Circle((0,0), ray_orbit, fill=True)
