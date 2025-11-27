cmake_minimum_required(VERSION 3.14)
project(mtnmt C)

find_package(pybind11 REQUIRED)

pybind11_add_module(material_bindings
    src/mtnmt/bindings.cpp
    src/mtnmt/material_model.c
)
