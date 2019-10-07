from setuptools import setup

setup(
    name='{{cookiecutter.project}}',
    version='1.0',
    py_modules=['{{cookiecutter.project}}'],
    install_requires=[
        'Click',
        'os',
        'pathlib',
    ],
    entry_points='''
        [console_scripts]
        {{cookiecutter.project}}={{cookiecutter.project}}:cli
    '''
)