from setuptools import setup, find_packages


setup(name='cyberhead',
    version='1.0',
    description='modular automated trading',
    url='cyberhead.uk',
    author='cyberhead',
    author_email='info@cyberhead.uk',
    license='MIT',
    packages=find_packages('modules'),
    zip_safe=False)
