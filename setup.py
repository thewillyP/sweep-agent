# sweep_agent/setup.py
from setuptools import setup, find_packages

setup(
    name='sweep_agent',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'sweep-agent = sweep_agent.agent:main',
        ],
    },
)