import numpy as np
from meta_learning import MetaLearner
from paraview.pv_visualize import write_vtk
import material_bindings

def main():
    learner = MetaLearner(dim=64, seed=42)
    state = learner.run(steps=20)

    try:
        material_bindings.update_state(state, 0.9, 0.01)
    except Exception:
        pass

    write_vtk(state, "data/sample_state.vtp")
    print("Wrote data/sample_state.vtp")

if __name__ == "__main__":
    main()
