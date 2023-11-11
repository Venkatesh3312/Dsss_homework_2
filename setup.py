from setuptools import setup, find_packages

setup(
    name='Dsss_homework_2',
    version='3.11.6',
    packages=find_packages(),
    entry_points=[
        'console_scripts': [
            'math_quiz = math_quiz.quiz:math_quiz_game',
        ],
    ],
    test_suite='tests',
)
