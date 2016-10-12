#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(name="PackageName",
    ext_modules=[
        Extension("arma_mod", ["Mat.cpp"],
        include_dirs = ["/Users/matthewschiavi/Documents/ResearchBase/DNR_2_0/armadillo-7.400.2/include/"],
        libraries = ["boost_python","lapack","openblas","armadillo"],
        library_dirs = ["/usr/local/lib","/usr/lib/","/usr/local/opt/openblas/lib","/Users/matthewschiavi/Documents/ResearchBase/DNR_2_0/armadillo-7.400.2"])
    ])

#open blas is in usr/local/opt
#lapack is in usr/lib
#boost is in usr local lib
# arma is in DNR