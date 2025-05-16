import numpy as np


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        # a. Initialize weights and bias
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = learning_rate
        self.epochs = epochs

    # b. Activation function: Sign
    def activation(self, x):
        return 1 if x >= 0 else -1

    def predict(self, x):
        linear_output = np.dot(self.weights, x) + self.bias
        return self.activation(linear_output)

    # c. Training
    def train(self, X, y):
        for epoch in range(1, self.epochs + 1):
            print(f"\nEpoch {epoch}")
            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred
                self.weights += self.lr * error * xi
                self.bias += self.lr * error
            print(f" Weights: {self.weights}, Bias: {self.bias}")


# Linearly separable dataset
X = np.array([[2, 1], [1, -1], [-1, -2], [-2, -1]])
y = np.array([1, 1, -1, -1])  # Labels: +1 or -1

# Train
p = Perceptron(input_size=2, learning_rate=0.1, epochs=10)
p.train(X, y)

# Final predictions
print("\nFinal predictions:")
for xi in X:
    print(f"{xi} => {p.predict(xi)}")
