from src.meta_learning import MetaLearner
def test_run():
    m = MetaLearner(dim=8)
    s = m.run(steps=5)
    assert len(s) == 8
