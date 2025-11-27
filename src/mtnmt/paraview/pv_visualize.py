import numpy as np
import vtk

def write_vtk(state: np.ndarray, path: str) -> None:
    n = int(state.size)
    points = vtk.vtkPoints()
    for i, v in enumerate(state):
        points.InsertNextPoint(float(i), float(v), 0.0)

    poly = vtk.vtkPolyData()
    poly.SetPoints(points)

    arr = vtk.vtkDoubleArray()
    arr.SetName("value")
    arr.SetNumberOfComponents(1)
    arr.SetNumberOfTuples(n)
    for i, v in enumerate(state):
        arr.SetValue(i, float(v))
    poly.GetPointData().SetScalars(arr)

    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(path)
    writer.SetInputData(poly)
    writer.SetFileTypeToASCII()
    writer.Write()
