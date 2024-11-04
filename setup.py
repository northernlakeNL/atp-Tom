from setuptools import setup, Extension
import sys
import pybind11

extensions = [
    Extension(
        'sensor_bindings',
        sources=[
            'code/sensors.cpp',
            'code/sensor_bindings.cpp'
        ],
        include_dirs=[
            pybind11.get_include(), 
            'code'
        ],  # Adjust path as needed
    ),
    Extension(
        'actuator_bindings',
        sources=[
            'code/actuator.cpp',
            'code/actuator_bindings.cpp'
        ],
        include_dirs=[
            pybind11.get_include(), 
            'code'
        ],  # Adjust path as needed
    ),
]


setup(
    name='device_bindings',
    version='0.1',
    ext_modules=extensions,
    zip_safe=False,
    options={
        'build_ext':{
            'build_lib': 'code',
        }
    }
)
