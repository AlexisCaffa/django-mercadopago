#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='django_mercadopago',
    version=0.1,
    description='MercadoPago integration for django',
    author='Hugo Osvaldo Barrera',
    author_email='hbarrera@z47.io',
    url='https://gitlab.com/hobarrera/django-mercadopago',
    license='ISC',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    use_scm_version={'version_scheme': 'post-release'},
    setup_requires=['setuptools_scm'],
)