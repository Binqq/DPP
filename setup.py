from setuptools import setup, find_packages

setup(
    name='DPP',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/Binqq/DPP',
    author='Michał Bojzan',
    author_email='m-michal-b@wp.pl'
)