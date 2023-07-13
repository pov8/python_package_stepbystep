from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("module", ["module.pyx"])
]

setup(
    name="python_package_stepbystep",
    ext_modules=cythonize(extensions),
)