from setuptools import setup, find_packages

setup(
    name='mage2-behave',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'behave',
        'selenium',
        'splinter>=0.21.0',
        'waiting',
        'mariadb',
        'webdriver-manager',
        'sshtunnel',
        'stere>=0.31.0'
    ],
    python_requires='>=3.8',
)
