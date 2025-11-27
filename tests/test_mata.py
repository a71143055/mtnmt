from src.mtnmt.meta_learning import MetaLearner

def test_run():
    m = MetaLearner(dim=8, seed=0)
    s = m.run(steps=5)
    assert s.shape == (8,)

