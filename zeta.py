import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpmath import zeta, mp

mp.dps = 30  # précision

# Fenêtre complexe
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

ax.axhline(0, color='gray')
ax.axvline(0, color='gray')

point, = ax.plot([], [], 'ro')
trail, = ax.plot([], [], lw=1)

xs = []
ys = []

# t initial
t = 0.0

def update(frame):
    global t

    s = 0.5 + 1j * t
    z = complex(zeta(s))

    x = z.real
    y = z.imag

    xs.append(x)
    ys.append(y)

    # garder historique limité
    if len(xs) > 1000:
        xs.pop(0)
        ys.pop(0)

    point.set_data([x], [y])
    trail.set_data(xs, ys)

    # distance à zéro
    dist = abs(z)

    # détection approximative d'un zéro
    if dist < 0.05:
        print(f"ZERO proche : t = {t}")

    t += 0.02
    return point, trail

ani = FuncAnimation(fig, update, interval=20)

plt.show()