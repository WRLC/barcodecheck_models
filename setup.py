from setuptools import setup

setup(
    name='barcodecheck_models',
    version='0.1',
    description='A package for barcode check models',
    author='Tom Boone',
    author_email='boone@wrlc.org',
    license='MIT',
    packages=['barcodecheck_models'],
    install_requires=[
        'sqlalchemy',
    ],
    zip_safe=False
)
