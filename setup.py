from setuptools import setup, find_packages

setup(
    name='LuminousUtilityKit',
    version='0.1',
    packages=find_packages(include=['LuminousUtilityKit', 'LuminousUtilityKit.*']),
    entry_points={
        'console_scripts': [
            'LuminousUtilityKit=LuminousUtilityKit.main:main',
        ],
    },
)
