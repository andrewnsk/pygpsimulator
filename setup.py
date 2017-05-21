from distutils.core import setup
from pygpsimulator import constants

setup(
    name='pygpsimulator',
    version=constants.PYGPSIMULATOR_VERSION,
    packages=['pygpsimulator'],
    url='',
    license='GNU GPL v3',
    author='Andrew Dorokhin',
    author_email='andrew@dorokhin.moscow',
    description='pygpsimulator',
    install_requires=['pyserial'],
    test_suite='tests'
)
