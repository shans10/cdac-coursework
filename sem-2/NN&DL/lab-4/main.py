import numpy as np


class Adaline:
    def __init__(self, input_size, learning_rate=0.01, epochs=10):
        # a. Initialize weights and bias
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = learning_rate
        self.epochs = epochs

    def net_input(self, X):
        return np.dot(X, self.weights) + self.bias

    def activation(self, X):
        # For Adaline, activation is linear (identity function)
        return self.net_input(X)

    def train(self, X, y):
        for epoch in range(1, self.epochs + 1):
            # c. Compute predictions and errors
            output = self.activation(X)
            errors = y - output

            # b. Compute Mean Squared Error (MSE)
            mse = np.mean(errors**2)

            # c. Gradient descent: update weights and bias
            self.weights += self.lr * np.dot(X.T, errors)
            self.bias += self.lr * errors.sum()

            print(
                f"Epoch {epoch}: MSE = {mse:.4f}, Weights = {self.weights}, Bias = {self.bias}"
            )

    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)


if __name__ == "__main__":
    # Simple dataset: linearly separable
    X = np.array([[1, 1], [2, 1], [1, -1], [-1, -2], [-2, -1]])
    y = np.array([1, 1, 1, -1, -1])  # Targets in {-1, +1}

    model = Adaline(input_size=2, learning_rate=0.01, epochs=10)
    model.train(X, y)

    # Predictions
    print("\nFinal predictions:")
    for xi in X:
        print(f"{xi} => {model.predict(xi)}")
