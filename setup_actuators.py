from setuptools import setup, Extension
import sys

# Optional: Add the site-packages path if needed
sys.path.append(r'c:\users\tomno\appdata\local\programs\python\python38\lib\site-packages')
import pybind11

ext_modules2 = [    
    Extension(
        'actuator_bindings',
        sources=[
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/actuator.cpp',
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code/actuator_bindings.cpp'
        ],
        include_dirs=[
            pybind11.get_include(), 
            'C:/Users/tomno/Documents/inno/atp/atp-code/atp-Tom/code'
        ],  # Adjust path as needed
    ),
]

setup(
    name='actuator_bindings',
    version='0.1',
    ext_modules=ext_modules2,
    zip_safe=False,
    options={
        'build_ext':{
            'build_lib': 'code',
        }
    }
)