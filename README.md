# Riemann Zeta Zero Visualizer

Real-time visualization of the Riemann Zeta function on the critical line using Python and Matplotlib.

This project animates the trajectory of:

\[
\zeta\left(\frac12 + it\right)
\]

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

The Riemann Zeta function is defined for complex numbers \( s \in \mathbb{C} \) by:

\[
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}
\]

This visualization evaluates the function along the critical line:

\[
s=\frac12+it
\]

where:
- \( \frac12 \) is the real component
- \( t \) is a varying imaginary parameter

The trajectory of:

\[
\zeta\left(\frac12+it\right)
\]

is rendered inside the complex plane in real time.

According to the Riemann Hypothesis, every non-trivial zero of the zeta function lies on the critical line:

\[
\Re(s)=\frac12
\]

When the rendered trajectory approaches the origin:

\[
\zeta(s)\approx0
\]

the script detects a potential non-trivial zero.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/riemann-zeta-visualizer.git
cd riemann-zeta-visualizer
