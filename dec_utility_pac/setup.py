from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="dec_utility_pac",
    version="0.0.1",
    description="Demo Package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/skyzhou01/hsz-python-package-creation-",
    author="Sky Zhou",
    author_email="hsz@gmail.com",
    keywords="demo project",
    license="MIT",
    packages=["dec_utility_pac"],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)