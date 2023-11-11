from setuptools import setup, find_packages

setup(
    name='dsss_homework_2',
    version='3.11.6',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.quiz:math_quiz_game',
        ],
    },
    install_requires=[
        'random',
    ],
    test_suite='tests',
)
