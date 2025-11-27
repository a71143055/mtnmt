from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "material_bindings",
        sources=["src/mtnmt/bindings.cpp", "src/mtnmt/material_model.c"],
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="material_bindings",
    version="0.1",
    ext_modules=ext_modules,
)
