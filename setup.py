from setuptools import setup

version = "1.7"

setup(
    name="hcsr04sensor",
    version=version,
    description="Module to access the HCSR04 sensor on a Raspberry Pi",
    long_description_content_type="text/markdown",
    long_description=open("./README.md", "r").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Topic :: Home Automation",
        "License :: OSI Approved :: MIT License",
    ],
    author="Al Audet",
    author_email="alaudet@linuxnorth.org",
    url="https://www.linuxnorth.org/hcsr04sensor/",
    download_url="https://github.com/alaudet/hcsr04sensor/releases",
    license="MIT License",
    packages=["hcsr04sensor"],
    scripts=["bin/hcsr04.py"],
)
