import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    sx = sigmoid(x)
    return sx * (1 - sx)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


class MLP:
    def __init__(self, input_size, hidden_size, learning_rate=0.1):
        # a. Initialize weights and biases
        self.w1 = np.random.randn(input_size, hidden_size)  # (2, 2)
        self.b1 = np.zeros((1, hidden_size))  # (1, 2)
        self.w2 = np.random.randn(hidden_size, 1)  # (2, 1)
        self.b2 = np.zeros((1, 1))  # (1, 1)
        self.lr = learning_rate

    def forward(self, X):
        # b. Forward propagation
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = relu(self.z1)  # c. ReLU activation in hidden layer

        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = sigmoid(self.z2)  # c. Sigmoid activation in output

        return self.a2

    def backward(self, X, y):
        # d. Backpropagation

        # Output layer error
        output_error = self.a2 - y  # dL/da2
        output_delta = output_error * sigmoid_derivative(self.z2)

        # Hidden layer error
        hidden_error = np.dot(output_delta, self.w2.T)
        hidden_delta = hidden_error * relu_derivative(self.z1)

        # Gradient descent updates
        self.w2 -= self.lr * np.dot(self.a1.T, output_delta)
        self.b2 -= self.lr * np.sum(output_delta, axis=0, keepdims=True)

        self.w1 -= self.lr * np.dot(X.T, hidden_delta)
        self.b1 -= self.lr * np.sum(hidden_delta, axis=0, keepdims=True)

    def train(self, X, y, epochs=1000):
        for epoch in range(1, epochs + 1):
            output = self.forward(X)
            self.backward(X, y)
            if epoch % 100 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

    def predict(self, X):
        output = self.forward(X)
        return (output > 0.5).astype(int)


if __name__ == "__main__":
    # Input features
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # XOR-like targets
    y = np.array([[0], [1], [1], [0]])

    mlp = MLP(input_size=2, hidden_size=2, learning_rate=0.1)
    mlp.train(X, y, epochs=1000)

    print("\nPredictions:")
    for xi in X:
        print(f"{xi} => {mlp.predict(np.array([xi]))[0][0]}")
