from setuptools import setup, find_packages

setup(
    name='hackapackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Larona-Suping/hackapackage',
    author='Larona-Suping',
    author_email='pride4suping@gmail.com'
)
