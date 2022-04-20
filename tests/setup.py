from setuptools import setup, find_packages

setup(
    name='mypackage',
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    descritption='EDSA example',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/DeonVenter547/mypacakge',
    author='DeonVenter',
    author_email='deon.venter@absa.africa'
)