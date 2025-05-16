import torch
import torch.nn as nn
import torch.optim as optim


# a. Define MLP using nn.Module
class MLP(nn.Module):
    def __init__(self, input_size=2, hidden_size=4):
        super(MLP, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, 1),
            nn.Sigmoid(),  # for binary classification
        )

    def forward(self, x):
        return self.model(x)


# Example XOR data
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Model, loss, optimizer
model = MLP()
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.1)

# b. Training loop
for epoch in range(1000):
    # Forward pass
    output = model(X)
    loss = criterion(output, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# c. Evaluation
with torch.no_grad():
    predictions = model(X)
    predicted_classes = (predictions >= 0.5).float()
    accuracy = (predicted_classes == y).float().mean()
    print("\nPredictions:", predicted_classes.view(-1).tolist())
    print(f"Accuracy: {accuracy.item() * 100:.2f}%")
