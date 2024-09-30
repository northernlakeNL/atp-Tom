cmake_minimum_required(VERSION 3.5)

# Project name and version
project(TOM_ATP VERSION 0.1.0 LANGUAGES C CXX)

# Find the PyBind11 package
list(APPEND CMAKE_PREFIX_PATH "C:/Users/tomno/AppData/Local/Programs/Python/Python37/Lib/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

# Set C++ standard to at least C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# Add the library (Python extension module) that will be built
add_library(sensor_bindings MODULE bindings.cpp sensors.cpp)

# Link PyBind11 with the target
target_link_libraries(sensor_bindings PRIVATE pybind11::module)

# Ensure the output module file is named properly (with '.pyd' suffix)
set_target_properties(sensor_bindings PROPERTIES SUFFIX ".pyd")

# Optional: Enable testing
include(CTest)
enable_testing()
