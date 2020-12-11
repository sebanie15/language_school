"""The setup script."""

from setuptools import setup, find_packages


def read_readme():
    with open('README.rst') as readme_file:
        return readme_file.read()


def read_history():
    with open('HISTORY.rst') as history_file:
        return history_file.read()


def read_requirements():
    with open('requirements.txt') as req:
        return req.read().split('\n')


setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sebastian Nieciąg",
    author_email='sebanie15@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'lang_school=lang_school.cli:cli',
        ],
    },
    install_requires=read_requirements(),
    license="MIT license",
    long_description=read_readme() + '\n\n' + read_history(),
    include_package_data=True,
    keywords='lang_school',
    name='lang_school',
    packages=find_packages(include=['db', 'db.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sebanie15/language_school',
    version='0.1.0',
    zip_safe=False,
)
