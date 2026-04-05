from vpython import sphere, vector, color, rate, canvas, curve, textures
import math

#-----------Simulations Values-------------

ray_earth        = 6371   # km
ray_orbit        = 42164  # km
angle_step       = 0.02   # degreed per frame
scale            = 1/1000 # scale of visual to 3D
ray_earth_visual = ray_earth * scale #earth size in scale
ray_orbit_visual = ray_orbit * scale #orbit size in scale


#-----------Create figure and axes-------------

scene = canvas(
    title = 'Earth Satelites Simulator 3D ',
    width  = 4500,
    height = 4500,
    background = color.black
)




#-----------Earth-------------

earth = sphere(
    pos=vector(0,0,0),
    radius= ray_earth_visual,
    texture=textures.earth

)




#-----------Orbit-------------

orbit_path = curve(color=color.white, radius=0.02)

for angle in range(0, 361, 2):
    theta = math.radians(angle)
    x = ray_orbit_visual * math.cos(theta)
    z = ray_orbit_visual * math.sin(theta) 
    orbit_path.append(vector(x,0,z))




#------------Satelite------------

satelite = sphere(
    pos= vector(ray_orbit_visual,0,0),
    radius = 0.18,
    color=color.red,
    make_trail=False
)




#------------Initialisation------------

def init():
    satelite.set_data([], [])
    return satelite,




#------------Animation Cicle 'loop'------------

theta = 0

while True:
    rate(100)

    x = ray_orbit_visual * math.cos(theta)
    z = ray_orbit_visual * math.sin(theta) 

    satelite.pos = vector(x,0,z)
    theta += angle_step

    