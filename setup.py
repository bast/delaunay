#!/usr/bin/env python

from distutils.core import setup
import distutils.spawn as _spawn
import distutils.command.build as _build
import distutils.dir_util as _dir_util
import setuptools.command.install as _install
import os
import sys
from distutils.sysconfig import get_python_lib
from shutil import copy2


def run_cmake():
    """
    Runs CMake to determine configuration for this build.
    """
    if _spawn.find_executable('cmake') is None:
        print("CMake is required to build this package.")
        print("Please install/load CMake and re-run setup.")
        sys.exit(-1)

    _build_dir = os.path.join(os.path.split(__file__)[0], 'build_setup_py')
    _dir_util.mkpath(_build_dir)
    os.chdir(_build_dir)

    try:
        _spawn.spawn(['cmake', '..'])
    except _spawn.DistutilsExecError:
        print("Error while running CMake")
        sys.exit(-1)


class build(_build.build):

    def run(self):
        cwd = os.getcwd()
        run_cmake()

        try:
            _spawn.spawn(['make'])
            os.chdir(cwd)
        except _spawn.DistutilsExecError:
            print("Error while running Make")
            sys.exit(-1)

        _build.build.run(self)


class install(_install.install):
    def run(self):
        cwd = os.getcwd()
        _install.install.run(self)
        _target_path = os.path.join(get_python_lib(), 'delaunay')

        if not os.path.exists(_target_path):
             os.makedirs(_target_path)

        if sys.platform == "darwin":
            suffix = 'dylib'
        else:
            suffix = 'so'

        for f in [os.path.join('build_setup_py', 'lib', 'libdelaunay.{0}'.format(suffix)),
                  os.path.join('build_setup_py', 'delaunay_export.h'),
                  os.path.join('delaunay.h')]:
            copy2(os.path.join(cwd, f), _target_path)


_this_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(_this_path, 'VERSION'), 'r') as version_file:
    version = version_file.read().strip()


setup(name='delaunay',
      version=version,
      description='Relatively Robust Divide and Conquer 2D Delaunay Construction Algorithm in O(n log n).',
      author='Wael El Oraiby',
      url='https://github.com/eloraiby/delaunay',
      packages=['delaunay'],
      license='AGPL-v3.0',
      install_requires=['cffi'],
      cmdclass={'install': install, 'build': build})
