#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(name="PackageName",
    ext_modules=[
        Extension("hello", ["hellomodule.cpp"],
        include_dirs = [" /Users/Matthew/ResearchBase/DNR_2_0/armadillo-7.400.1/include/"],
        libraries = ["boost_python","lapack","openblas","armadillo"],
        library_dirs = ["/usr/lib/","/Users/Matthew/ResearchBase/DNR_2_0/OpenBLAS","/Users/Matthew/ResearchBase/DNR_2_0/armadillo-7.400.1"])
    ])