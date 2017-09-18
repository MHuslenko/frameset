from setuptools import setup

import frameset


def read(filename):
    with open(filename) as f:
        return f.read()


def get_requirements_tests():
    with open('requirements-tests.txt') as f:
        return f.readlines()


setup(
    name='django-frameset',
    version=frameset.__version__,
    packages=['frameset'],
    author='Nikita Guslenko',
    author_email='nik.nout1@gmail.com',
    license='BSD',
    description='Frameset Django utility',
    long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    url='https://github.com/guayard/frameset.git',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=get_requirements_tests(),
    test_suite='tests',
    zip_safe=False
)