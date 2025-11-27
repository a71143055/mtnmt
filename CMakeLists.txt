cmake_minimum_required(VERSION 3.14)
project(mtnmt)
find_package(pybind11 REQUIRED)
pybind11_add_module(material_bindings bindings.cpp material_model.c)
