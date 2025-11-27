from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "material_bindings",
        sources=[
            "bindings.cpp",
            "material_model.c"
        ],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["/std:c++17"],  # Windows MSVC 컴파일러 옵션
    ),
]

setup(
    name="material_bindings",
    version="0.1",
    description="C bindings for material model using pybind11",
    ext_modules=ext_modules,
)
