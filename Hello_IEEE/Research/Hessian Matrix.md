# Hessian Matrix
- it's a way of representing all the information of the second partial derivatives of a function in one matrix.

$$
H_f(x) =
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

- number of rows and columns depends on the number of variables in the function.
## Some properties
- The Hessian Matrix is always symmetric in case that the function is continious

# Use of Hessian Matrix in AI
  ## it is often used for optmizing function of intreset, it encodes the curvature of the loss landscape
  - Calculates how rapidly the gradient of the loss function is changing
  - positive eigenvalues indicate locally convex directions
  - negative eigenvalues indicate directions of descent/ascent
  - near‑zero eigenvalues correspond to flat directions
  - hessian matrix guides algorithms to take wide steps in flat regions and smaller steps in steeply curved areas
  ## Applications
  - used in computer vision in image segmentation
  - understanding trained models' stability
  - in fine tuning models, Hessian matrix helps in adapting learning rate based on local curvature
