# coding: utf-8
import os
import sys

from setuptools import setup

__author__ = "Max Yao <weng.32002@gmail.como>"


install_requires = [
    "requests",
    "packaging"
]
extras_require = {}
with open("README.md") as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
elif sys.argv[-1] == "clean":
    import shutil

    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("chromedriver_autoinstaller_max.egg-info"):
        shutil.rmtree("chromedriver_autoinstaller_max.egg-info")


setup(
    name="chromedriver-autoinstaller-max",
    version="1.0.5",
    author='Max Yao',
    author_email='weng.32002@gmail.com',
    description="Automatically install chromedriver that supports the currently installed version of chrome.",
    license="MIT",
    keywords="chromedriver chrome chromium selenium",
    url="https://github.com/max32002/chromedriver-autoinstaller-max",
    packages=["chromedriver_autoinstaller_max"],
    entry_points={
        "console_scripts": [
            "chromedriver-path=chromedriver_autoinstaller_max.utils:print_chromedriver_path"
        ],
    },
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Installation/Setup",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=install_requires,
    extras_require=extras_require,
)
