# src/mtnmt/paraview/pv_script.py
# 이 스크립트는 pvpython 또는 pvbatch로 실행하도록 설계되었습니다.
from paraview.simple import *
import sys
import os

def pv_render(vtk_path: str, screenshot_path: str = "render.png"):
    """
    Legacy VTK 파일을 로드하고 간단히 렌더링한 뒤 스크린샷을 저장합니다.
    사용 예: pvpython pv_script.py data/sample_state.vtk render.png
    """
    if not os.path.exists(vtk_path):
        raise FileNotFoundError(f"{vtk_path} not found")

    data = LegacyVTKReader(FileNames=[vtk_path])
    view = GetActiveViewOrCreate('RenderView')
    display = Show(data, view)
    ColorBy(display, ('POINTS', 'value'))
    display.SetRepresentationType('Surface')
    Render()
    # 카메라/컬러맵 조정은 필요에 따라 추가
    SaveScreenshot(screenshot_path, view)
    print(f"Saved screenshot to {screenshot_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pvpython pv_script.py <vtk_path> [screenshot_path]")
    else:
        vtk_path = sys.argv[1]
        screenshot = sys.argv[2] if len(sys.argv) > 2 else "render.png"
        pv_render(vtk_path, screenshot)
