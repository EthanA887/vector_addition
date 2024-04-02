import numpy as np
import math
import matplotlib.pyplot as plt

def get_float_input(var, prompt, direction):
    while (isinstance(var, float) == False):
        var = input(f'{prompt}')
        if (direction == True):
            try:
                var = float(parsed(var))
            except ValueError:
                var = None
        else:
            try:
                var = float(parsed(var))
            except ValueError:
                var = None
    return var

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
v0_mag = None
v0_mag = get_float_input(v0_mag, 'Enter magnitude: ', direction=False)
v0_dir = None   
v0_dir = get_float_input(v0_dir, 'Enter direction in radians (e.g. 3pi/2): ', direction=True)

print('\nSecond vector\n----------')
v1_mag = None
v1_mag = get_float_input(v1_mag, 'Enter magnitude: ', direction=False)
v1_dir = None   
v1_dir = get_float_input(v1_dir, 'Enter direction in radians (e.g. 3pi/2): ', direction=True)

v0 = np.array([(v0_mag * math.cos(v0_dir)), (v0_mag * math.sin(v0_dir))])
v1 = np.array([(v1_mag * math.cos(v1_dir)), (v1_mag * math.sin(v1_dir))])

v2 = np.array([(v0[0] + v1[0]), (v0[1] + v1[1])])

r = round(math.atan(v2[1] / v2[0]), 3)
m = round(math.sqrt(v2[0] ** 2 + v2[1] ** 2), 3)
print(f'\nThe sum of your vectors has a direction of {r} radians and a magnitude of {m}.')
print(f'Rectangular coordinates: ({round(v2[0], 3)}, {round(v2[1], 3)})')

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
