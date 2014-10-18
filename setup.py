from setuptools import setup
import os
version = '0.0.1'


setup(name='hcsr04sensor',
      version=version,
      description='Simple module to access HCSR04 sensor on RaspiPi',
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7",
          "Topic :: Home Automation",
          "License :: OSI Approved :: MIT License",
          ],
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='http://www.linuxnorth.org/',
      download_url='https://github.com/alaudet/',
      license='MIT License',
      packages=['hcsr04sensor'],
      install_requires=['RPi.GPIO']
      )
