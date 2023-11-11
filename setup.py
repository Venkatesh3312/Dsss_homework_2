# setup.py

from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='3.11.6'
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.quiz:math_quiz',
        ],
    },
    install_requires=[
        # Add any dependencies your project might have
        'random',
    ],
    test_suite='tests',
)
