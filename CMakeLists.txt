cmake_minimum_required(VERSION 3.14)
project(mtnmt C)

find_package(pybind11 REQUIRED)

# 소스 경로는 프로젝트 구조에 맞게 조정
pybind11_add_module(material_bindings
    src/mtnmt/bindings.cpp
    src/mtnmt/material_model.c
)
