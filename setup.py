import os
import sys
import shutil
from subprocess import call
from setuptools import setup
from warnings import warn

if sys.version_info.major != 3:
    raise RuntimeError('Wishbone requires Python 3')


setup(name='wishbone',
      version='0.4.2',
      description='Wishbone algorithm for identifying bifurcating trajectories from single-cell data',
      author='Manu Setty',
      author_email='manu.talanki@gmail.com',
      package_dir={'': 'src'},
      packages=['wishbone'],
      install_requires=[
          'numpy>=1.12.0',
          'pandas>=0.19.2',
          'scipy>=0.18.1',
          'bhtsne',
          'matplotlib>=1.5.1sn',
          'seaborn>=0.7.1',
          'sklearn',
          'networkx>=1.11',
          'fcsparser>=0.1.2',
          'statsmodels>=0.8.0',
          'Cython'],
      scripts=['src/wishbone/wishbone_gui.py'],
      )
    
# install phenograph
call(['pip', 'install', 'git+https://github.com/jacoblevine/phenograph.git'])


# get location of setup.py
setup_dir = os.path.dirname(os.path.realpath(__file__))
