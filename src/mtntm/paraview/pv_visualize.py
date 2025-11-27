import vtk

def write_vtk(state, path):
    n = len(state)
    points = vtk.vtkPoints()
    for i, v in enumerate(state):
        points.InsertNextPoint(i, v, 0.0)
    poly = vtk.vtkPolyData()
    poly.SetPoints(points)
    arr = vtk.vtkDoubleArray()
    arr.SetName("value")
    arr.SetNumberOfComponents(1)
    arr.SetNumberOfTuples(n)
    for i, v in enumerate(state):
        arr.SetValue(i, v)
    poly.GetPointData().AddArray(arr)
    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(path)
    writer.SetInputData(poly)
    writer.Write()
