from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'sensor_bindings',
        ['bindings.cpp', 'sensors.cpp'],
        include_dirs=[pybind11.get_include()],
        language='C++'
    ),
]

setup(
    name='sensor_bindings',
    ext_modules=ext_modules,
    zip_safe=False,
)