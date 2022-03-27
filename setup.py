from setuptools import find_packages, setup
setup(
    name='yaml_keygen',
    packages=["yaml_keygen"],
    version='0.1.5',
    description='A Python module for extracting keys from a YAML file.',
    author='Faisal Ali',
    author_email='fzl.ali33@gmail.com',
    url='https://github.com/fa1zali/yaml_keygen',
    install_requires=['ruamel.yaml'],
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    license='MIT',
)
