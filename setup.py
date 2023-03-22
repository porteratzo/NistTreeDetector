from setuptools import setup

setup(
    name='treetool',
    version='1.0.0',    
    description='Python package for tree detection, segmentation and extraction of DBH',
    url='https://github.com/porteratzo/treetool',
    author='Omar Montoya',
    author_email='omar.alfonso.montoya@hotmail.com',
    license='MIT License',
    packages=[],
    install_requires=['open3d', 'lsq-ellipse'],
    classifiers=[
    ],
)