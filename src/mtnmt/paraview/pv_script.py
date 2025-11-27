from paraview.simple import *
import sys, os

def pv_render(vtk_path: str, screenshot_path: str = "render.png"):
    if not os.path.exists(vtk_path):
        raise FileNotFoundError(f"{vtk_path} not found")

    data = LegacyVTKReader(FileNames=[vtk_path])
    view = GetActiveViewOrCreate('RenderView')
    display = Show(data, view)
    ColorBy(display, ('POINTS', 'value'))
    display.SetRepresentationType('Surface')
    Render()
    SaveScreenshot(screenshot_path, view)
    print(f"Saved screenshot to {screenshot_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pvpython pv_script.py <vtk_path> [screenshot_path]")
    else:
        vtk_path = sys.argv[1]
        screenshot = sys.argv[2] if len(sys.argv) > 2 else "render.png"
        pv_render(vtk_path, screenshot)
