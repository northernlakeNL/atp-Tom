from setuptools import setup, Extension
import sys
import pybind11

ext_modules1 = [
    Extension(
        'sensor_bindings',
        sources=[
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/sensors.cpp',
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/sensor_bindings.cpp'
        ],
        include_dirs=[
            pybind11.get_include(), 
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code'
        ],  # Adjust path as needed
    ),
]


setup(
    name='sensor_bindings',
    version='0.1',
    ext_modules=ext_modules1,
    zip_safe=False,
    options={
        'build_ext':{
            'build_lib': 'code',
        }
    }
)
