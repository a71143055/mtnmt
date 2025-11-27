import numpy as np

class MetaLearner:
    def __init__(self, dim=64):
        self.dim = dim
        self.W = np.random.randn(dim, dim) * 0.1

    def step(self, x):
        return np.tanh(x @ self.W)

    def run(self, steps=10):
        x = np.random.randn(self.dim)
        for _ in range(steps):
            x = self.step(x)
        return x
