from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from setuptools import find_packages
from setuptools import setup

description="Perform High Energy Physics with Numpy"

setup(
    name="npana",
    version="0.0.1",
    description=description,
    long_description=description,
    author="Xiangyang Ju",
    license="Apache License, Version 2.0",
    keywords=["numpy", "HEP", "analysis", "cupy", "ROOT"],
    url="https://github.com/xju2/npana",
    packages=find_packages(),
    install_requires=[
        'numba',
        'cupy-cuda101',
        "root_numpy",
        "future",
        "numpy",
        "scipy",
        "pandas",
        "setuptools",
        "six",
        "matplotlib",
        "sklearn",
        'pyyaml>=5.1',
    ],
    setup_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    scripts=[
        'scripts/ana_CONF_Hbb',
        'scripts/ana_CONF_Hbb_presel',
        'scripts/ana_CONF_Hbb_numba',
        'scripts/ana_CONF_Hbb_gpu',
        'scripts/tree2histo_gpu',
        'scripts/tree2histo',
        'scripts/ana_CONF_Hbb_ray',
    ],
)
