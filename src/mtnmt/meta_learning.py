import numpy as np

class MetaLearner:
    def __init__(self, dim: int = 64, seed: int | None = None):
        if seed is not None:
            np.random.seed(seed)
        self.dim = dim
        self.W = np.random.randn(dim, dim) * 0.1

    def step(self, x: np.ndarray) -> np.ndarray:
        return np.tanh(x @ self.W)

    def run(self, steps: int = 10) -> np.ndarray:
        x = np.random.randn(self.dim)
        for _ in range(steps):
            x = self.step(x)
        return x
