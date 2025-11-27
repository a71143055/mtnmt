# src/mtnmt/main.py
import numpy as np
from mtnmt.meta_learning import MetaLearner
from mtnmt.paraview.pv_visualize import write_vtk

def main():
    learner = MetaLearner(dim=64, seed=42)
    state = learner.run(steps=20)

    # C 바인딩이 빌드되어 있으면 호출하여 상태를 추가 변형
    try:
        import material_bindings
        # material_bindings.update_state은 in-place로 동작
        material_bindings.update_state(state, 0.9, 0.01)
    except Exception:
        # 바인딩이 없으면 무시하고 계속 진행
        pass

    write_vtk(state, "data/sample_state.vtk")
    print("Wrote data/sample_state.vtk")

if __name__ == "__main__":
    main()
