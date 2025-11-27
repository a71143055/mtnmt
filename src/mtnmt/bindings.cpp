// src/mtnmt/bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

extern "C" void update_state(double*, int, double, double);

namespace py = pybind11;

void py_update(py::array_t<double> arr, double a, double b){
  auto buf = arr.request();
  if (buf.ndim != 1) throw std::runtime_error("Input array must be 1-D");
  double *ptr = static_cast<double*>(buf.ptr);
  int n = static_cast<int>(buf.size);
  update_state(ptr, n, a, b);
}

PYBIND11_MODULE(material_bindings, m){
  m.doc() = "C bindings for material model";
  m.def("update_state", &py_update, "Update state in C (in-place)",
        py::arg("arr"), py::arg("a"), py::arg("b"));
}
