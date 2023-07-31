from setuptools import setup, find_packages

setup(
    name='BookLover',
    version='1.0.0',
    url='https://github.com/aowen18/booklover/tree/main',
    author='Alexa Owen',
    author_email='amo9f@virginia.edu',
    description='Package allows the user to add books they have read and see the name, and number of books they read',
    packages=find_packages(),
    install_requires=['pandas >= 2.0.0']
)