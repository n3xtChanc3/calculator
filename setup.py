# setup.py

from setuptools import setup, find_packages

setup(
    name='simple-calculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # List your dependencies if any
    entry_points={},
    author='decoder',
    author_email='starsonthesky@protonmail.com',
    description='A simple calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/simple-calculator',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
