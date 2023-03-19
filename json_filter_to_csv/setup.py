from setuptools import find_packages, setup

setup(
    name='jftc',
    packages=find_packages(include=['jftc']),
    version='0.0.1',
    description='This library filters the text and summary data from the JSON file and transforms it into a CSV',
    author='Bruno Magalhães',
    license='MIT',
    install_requires=[
        "pandas==1.5.3"
    ]
)