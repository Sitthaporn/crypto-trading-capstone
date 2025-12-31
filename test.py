import torch
import torch.nn as nn

device = torch.device("cpu")

model = nn.Linear(10, 1).to(device)
data = torch.randn(5, 10).to(device)
output = model(data)

print("Output:", output)
print("Device:", output.device)


