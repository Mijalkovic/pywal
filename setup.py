from setuptools import setup, find_packages

setup(
    name="stefan-pywal",
    version="3.8.12+stefan",
    author="Stefan Mijalkovic",
    author_email="stefan.mijalkovic94@gmail.com",
    description="A customized version of pywal that generates colorschemes from images.",
    url="https://github.com/Mijalkovic/pywal",
    license="MIT",
    packages=find_packages(),
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
