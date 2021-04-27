from setuptools import find_packages
from setuptools import setup

setup(
    name="hello-world",
    version="1.0.0",
    description="This package contain sample hello world code",
    author="Sachin",
    email="vi**.*@gmail.com",
    url="https://github.com/svijay87/Learning-Program-python",
    # install_requires=[],
    packages=find_packages(exclude=('tests*','testing*')),
    entry_points={
      'console_scripts': [
          'hello-world-cli = hello_world.main:main',
      ],
    },
)