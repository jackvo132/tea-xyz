from setuptools import setup

setup(
    author='jackvo',
    author_email='jackvo132@gmail.com',
    name='tea-xyz-jackvo',
    version='1.0.6',
    description='A simple package for https://app.tea.xyz/. Example tea-xyz-jackvo - https://github.com/jackvo132/tea-xyz',
    url='https://github.com/jackvo132/tea-xyz',
    project_urls={
        'Homepage': 'https://github.com/jackvo132/tea-xyz',
        'Source': 'https://github.com/jackvo132/tea-xyz',
    },
    py_modules=['hello_tea'],
    entry_points={
        'console_scripts': [
            'hello-tea=hello_tea:hello_tea_func'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'tea-xyz-jackvo',
    ],
)
