from setuptools import setup

def get_from_filename(filename):
    with open(filename, "r") as fn:
        return fn.read()

setup(
    name='Dart_Backend',
    version='0.0.1',
    packages=['api', 'core', 'core.migrations', 'dart_app'],
    url='https://github.com/matisla/dart_backend.git',
    license='MIT',
    author='matisla',
    author_email='',
    description='',
    install_requires=get_from_filename("requirements.txt"),
    tests_require=[
        "pytest",
        "requests",
    ]
)
