import math
import numpy as np
import matplotlib.pyplot as plt

# Enable the string 'pi' as a part of the directional input
def parsed(s):
    if ('pi' in s):
        if (s[0] == 'p'):
            s = s.replace('pi', str(math.pi))
            return eval(s)
        else:
            s = s.replace('pi', ('*' + str(math.pi)))
            return eval(s)
    return s

print('First vector\n----------')

# Magnitude
v0_mag = None
while (isinstance(v0_mag, float) == False):
    v0_mag = input('Input magnitude: ')
    try:
        v0_mag = float(v0_mag)
    except ValueError:
        v0_mag = None
        
# Direction
v0_dir = None
while (isinstance(v0_dir, float) == False):
    v0_dir = input('Input direction in radians (e.g. 3pi/2): ')
    try:
        v0_dir = float(parsed(v0_dir))
    except ValueError:
        v0_dir = None

print('\nSecond vector\n----------')

# Magnitude
v1_mag = None
while (isinstance(v1_mag, float) == False):
    v1_mag = input('Input magnitude: ')
    try:
        v1_mag = float(v1_mag)
    except ValueError:
        v1_mag = None

# Direction
v1_dir = None
while (isinstance(v1_dir, float) == False):
    v1_dir = input('Input direction in radians (e.g. 3pi/2): ')
    try:
        v1_dir = float(parsed(v1_dir))
    except ValueError:
        v1_dir = None

# Convert from polar to rectangular coordinates
v0 = np.array([(v0_mag * math.cos(v0_dir)), (v0_mag * math.sin(v0_dir))])
v1 = np.array([(v1_mag * math.cos(v1_dir)), (v1_mag * math.sin(v1_dir))])

# Add the vectors
v2 = np.array([(v0[0] + v1[0]), (v0[1] + v1[1])])

# Convert back to polar coordinates to calculate the vector's magnitude and direction
r = round(math.atan(v2[1] / v2[0]), 3)
m = round(math.sqrt(v2[0] ** 2 + v2[1] ** 2), 3)
print(f'\nThe sum of your vectors has a direction of {r} radians and a magnitude of {m}.')
print(f'Rectangular coordinates: ({round(v2[0], 3)}, {round(v2[1], 3)})')

# Graph the vectors
values = [v0[0], v0[1], v1[0], v1[1], v2[0], v2[1]]
lim = max(abs(min(values)), max(values)) * 1.1
print('\nGraphic representation:')
fig, ax = plt.subplots(figsize=(9, 9))
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.quiver(0, 0, v0[0], v0[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(v0[0], v0[1], (v2[0] - v0[0]), (v2[1] - v0[1]), angles='xy', scale_units='xy', scale=1, color='b')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='m')
plt.grid()
plt.show()
