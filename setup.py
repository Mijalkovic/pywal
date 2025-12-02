from setuptools import setup

setup(
    name="stefan-pywal",
    version="3.8.12+stefan",
    author="Stefan Mijalkovic",
    author_email="stefan.mijalkovic94@gmail.com",
    description="A customized version of pywal that generates colorschemes from images.",
    url="https://github.com/Mijalkovic/pywal",
    license="MIT",
    # This is the crucial change: we explicitly list the packages to install.
    packages=["pywal", "pywal.backends"],
    # This tells the installer to include non-python files inside the package (like templates).
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "wal=pywal.__main__:main",
        ],
    },
    classifiers=[
        "Environment :: X11 Applications",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
