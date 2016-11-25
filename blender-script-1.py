bpy.ops.wm.open_mainfile(filepath=“/Users/bacheletlab/Downloads/stereo_equirectangular_base.blend")


import bpy
from numpy.random import RandomState
import numpy as np


count = 200
rs = RandomState(1234)

min_pt = 0
max_pt = 10
cube_size = 0.1

# Generate some data from a multivariate normal distribution
# (http://stackoverflow.com/questions/16024677/generate-correlated-data-in-python-3-3)
mu = np.array([0.0, 5.0, 5.0])
r = np.array([[5.5, 0.3, 4.3],
              [0.4,  1., 0.5],
              [4.8, 0.5, 5.0]])
data = rs.multivariate_normal(mu, r, size=count)
print(data)

for x, y, z in data:
    print("xyz", x, y, z)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    bpy.ops.transform.resize(value=(cube_size, cube_size, cube_size))

bpy.data.scenes['Scene'].render.filepath = '/Users/bacheletlab/Downloads/output.png'
bpy.ops.render.render(write_still=True)