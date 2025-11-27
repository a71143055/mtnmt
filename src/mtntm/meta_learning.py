# src/mtnmt/meta_learning.py
import numpy as np

class MetaLearner:
    """
    간단한 프로토타입 메타러너.
    - dim: 상태 벡터 차원
    - seed: 재현성 확보용 시드
    """
    def __init__(self, dim: int = 64, seed: int | None = None):
        if seed is not None:
            np.random.seed(seed)
        self.dim = dim
        # 작은 초기 가중치로 시작
        self.W = np.random.randn(dim, dim) * 0.1

    def step(self, x: np.ndarray) -> np.ndarray:
        """
        한 스텝 업데이트: 비선형 활성화 적용
        """
        return np.tanh(x @ self.W)

    def run(self, steps: int = 10) -> np.ndarray:
        """
        랜덤 초기 상태에서 여러 스텝 반복
        """
        x = np.random.randn(self.dim)
        for _ in range(steps):
            x = self.step(x)
        return x
