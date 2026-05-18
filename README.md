# Riemann Zeta Zero Visualizer

Real-time visualization of the Riemann Zeta function on the critical line using Python and Matplotlib.

This project animates the trajectory of:

zeta(s) = 1/2 +it

inside the complex plane and highlights approximate non-trivial zeros when the trajectory approaches the origin.

---

## Features

- Real-time complex plane animation
- Visualization of the zeta function trajectory
- Approximate zero detection
- Adjustable precision with `mpmath`
- Lightweight and easy to modify

---
## Mathematical Background

The Riemann Zeta function is defined for complex numbers s by:


zeta(s)=sum(1/n^s)


This visualization evaluates the function along the critical line:


s=0.5+it


is rendered inside the complex plane in real time.

According to the Riemann Hypothesis, every non-trivial zero of the zeta function lies on the critical line:


Re(s)=1/2


When the rendered trajectory approaches the origin:

zeta(s) approx0

the script detects a potential non-trivial zero.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/theorick/zeta_zero.git
cd zeta_zero
