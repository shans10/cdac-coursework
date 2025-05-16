import numpy as np
import matplotlib.pyplot as plt


# Loss and gradient
def loss(w):
    return w[0] ** 2 + w[1] ** 2


def grad(w):
    return 2 * w


# SGD optimizer
def sgd(w, lr):
    return w - lr * grad(w)


# RMSprop optimizer
def rmsprop(w, lr, grad_func, cache, beta=0.9, epsilon=1e-8):
    g = grad_func(w)
    cache = beta * cache + (1 - beta) * g**2
    w -= lr * g / (np.sqrt(cache) + epsilon)
    return w, cache


# Adam optimizer
def adam(w, lr, grad_func, m, v, t, beta1=0.9, beta2=0.999, epsilon=1e-8):
    g = grad_func(w)
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g**2

    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)

    w -= lr * m_hat / (np.sqrt(v_hat) + epsilon)
    return w, m, v


def run_optimizer(name, steps=50, lr=0.1):
    w = np.array([2.0, 1.5])
    trajectory = [w.copy()]

    # optimizer-specific variables
    cache = np.zeros_like(w)
    m, v = np.zeros_like(w), np.zeros_like(w)

    for t in range(1, steps + 1):
        if name == "sgd":
            w = sgd(w, lr)
        elif name == "rmsprop":
            w, cache = rmsprop(w, lr, grad, cache)
        elif name == "adam":
            w, m, v = adam(w, lr, grad, m, v, t)
        trajectory.append(w.copy())

    return np.array(trajectory)


# Generate trajectories
traj_sgd = run_optimizer("sgd", lr=0.1)
traj_rmsprop = run_optimizer("rmsprop", lr=0.01)
traj_adam = run_optimizer("adam", lr=0.05)

# Plot loss surface
w1 = np.linspace(-3, 3, 100)
w2 = np.linspace(-3, 3, 100)
W1, W2 = np.meshgrid(w1, w2)
Z = W1**2 + W2**2

plt.figure(figsize=(10, 7))
plt.contour(W1, W2, Z, levels=30, cmap="viridis")
plt.plot(traj_sgd[:, 0], traj_sgd[:, 1], "o-", label="SGD", color="red")
plt.plot(traj_rmsprop[:, 0], traj_rmsprop[:, 1], "o-", label="RMSprop", color="blue")
plt.plot(traj_adam[:, 0], traj_adam[:, 1], "o-", label="Adam", color="green")
plt.scatter(0, 0, c="black", marker="x", s=100, label="Minimum")
plt.title("Optimizer Trajectories on f(w) = w1² + w2²")
plt.xlabel("w1")
plt.ylabel("w2")
plt.legend()
plt.grid(True)
plt.show()
