from meta_learning import MetaLearner
from paraview.pv_visualize import write_vtk

if __name__ == "__main__":
    learner = MetaLearner(dim=64)
    state = learner.run(steps=20)
    write_vtk(state, "data/sample_state.vtk")
    print("Done: sample_state.vtk written")
