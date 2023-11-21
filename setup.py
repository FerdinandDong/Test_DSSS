from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 这里可以列出任何依赖，例如 'numpy>=1.13.3'
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=Test_DSSS.math_quiz:main_function'
        ]
    }
)
