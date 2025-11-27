#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

extern "C" void update_state(double*, int, double, double);

namespace py = pybind11;

void py_update(py::array_t<double> arr, double a, double b){
  auto buf = arr.request();
  double *ptr = (double*)buf.ptr;
  int n = (int)buf.size;
  update_state(ptr, n, a, b);
}

PYBIND11_MODULE(material_bindings, m){
  m.def("update_state", &py_update, "Update state in C");
}
