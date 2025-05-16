import numpy as np
import matplotlib.pyplot as plt


# a. Define 2D quadratic loss surface: f(w) = w1² + w2²
def loss(w):
    return w[0] ** 2 + w[1] ** 2


def grad(w):
    return 2 * w  # gradient of the loss


# Gradient Descent function
def gradient_descent(start, lr=0.1, steps=20):
    path = [start]
    w = start.copy()

    for _ in range(steps):
        g = grad(w)
        w = w - lr * g
        path.append(w.copy())

    return np.array(path)


# Generate path
start = np.array([2.0, 1.5])  # starting point
trajectory = gradient_descent(start, lr=0.1, steps=20)

# b. Plot the loss surface and the path
w1 = np.linspace(-3, 3, 100)
w2 = np.linspace(-3, 3, 100)
W1, W2 = np.meshgrid(w1, w2)
Z = W1**2 + W2**2

plt.figure(figsize=(8, 6))
plt.contour(W1, W2, Z, levels=30, cmap="viridis")
plt.plot(
    trajectory[:, 0], trajectory[:, 1], "o-", color="red", label="Gradient Descent Path"
)
plt.scatter(0, 0, c="black", marker="x", s=100, label="Minimum")
plt.title("Gradient Descent on 2D Loss Surface")
plt.xlabel("w1")
plt.ylabel("w2")
plt.legend()
plt.grid(True)
plt.show()
