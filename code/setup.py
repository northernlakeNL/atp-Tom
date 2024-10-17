from setuptools import setup, Extension
import pybindpi11
import os

sensor_include_dir = os.path.join(os.path.abspath(__file__))

ext_modules = [
    Extension(
        'sensor_bindings',
        ['C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/bindings.cpp', 'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/sensors.cpp'],
        include_dirs=[
            pybind11.get_include(),
            sensor_include_dir,],
        language='c++'
    ),
]

setup(
    name='sensor_bindings',
    ext_modules=ext_modules,
    zip_safe=False,
)

#C:\users\tomno\appdata\local\programs\python\python37\lib\site-packages\pybind11