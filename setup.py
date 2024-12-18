


#### `setup.py`
from setuptools import setup, find_packages

setup(
    name='ExpertSystem_GrapesGuava',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow==2.12.0',
        'scikit-learn==1.2.0',
        'numpy==1.23.0',
        'pandas==1.5.0',
        'opencv-python==4.7.0',
        'matplotlib==3.6.0'
    ],
)
