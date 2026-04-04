import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation



#-----------Simulations Values-------------

ray_earth      = 6371  #km
ray_orbit      = 42164  #km
angle_step     = 2  #degreed per frame
frame_interval = 50  #milliseconds

#-----------Create figure and axes-------------

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-45000,45000)
ax.set_ylim(-45000,45000)
ax.set_title('Satellite simulator orbiting the Earth')





#-----------Earth-------------

earth = plt.Circle((0,0), ray_earth, fill=True)
ax.add_patch(earth)





#-----------Orbit-------------

orbit = plt.Circle((0,0), ray_orbit, fill=False, linestyle='--', linewidth=1.5)
ax.add_patch(orbit)




#------------Satelite------------

satelite, = ax.plot([], [], 'o', markersize=8)




#------------Initialisation------------

def init():
    satelite.set_data([], [])
    return satelite,




#------------Animation Atualization------------

def update(frame):
    theta = np.radians(frame)
    x = ray_orbit * np.cos(theta)
    y = ray_orbit * np.sin(theta)
    satelite.set_data([x], [y])
    return satelite,




#-----------Animation-------------

anim = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 360, angle_step),
    init_func=init,
    interval=frame_interval,
    blit=True
)

plt.show()