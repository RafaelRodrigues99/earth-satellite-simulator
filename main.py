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
ax.add_patch(orbit)

#Satelite

satelite, = ax.plot([], [], 'o')


#Initialisation

def init():
    satelite.set_data([], [])
    return satelite,

#Animation Atualization

def update(frame):
    theta = np.radians(frame)
    x = ray_orbit * np.cos(theta)
    y = ray_orbit * np.sin(theta)
    satelite.set_data([x], [y])
    return satelite,

#Animation

anim = FuncAnimation(
    fig,
    update
    frames=np.arange(0,360,2),
    init_func=init,
    interval=50,
    blit=True
)


plt.show()