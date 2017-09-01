# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='b3',
      version='0.0',
      description='Web browser',
      long_description='Web browser for distraction.',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP :: Browsers'
      ],
      keywords='web',
      author='Konstantin Tcholokachvili',
      author_email='konstantin.tcholokachvili@protonmail.com',
      url='https://github.com/narke/b3',
      license='MIT License',
      packages=find_packages('src'),
      package_dir={'b3': 'src/b3'},
      package_data = {
          'b3': ['*.glade'],
      },
      include_package_data=True,
      install_requires=[
          'setuptools'
      ],
      entry_points={
          'gui_scripts': ['b3=b3.gui_gtk:main']
      })
