import re

from setuptools import setup

# Get version without importing
with open('qr_code/__init__.py', 'rb') as f:
    VERSION = str(re.search('__version__ = \'(.+?)\'', f.read().decode('utf-8')).group(1))

setup(
    name='django-qr-code',
    version=VERSION,
    packages=['qr_code', 'qr_code.qrcode', 'qr_code.templatetags'],
    url='https://github.com/dprog-philippe-docourt/django-qr-code',
    license='BSD 3-clause',
    author='Philippe Docourt',
    author_email='philippe@docourt.ch',
    maintainer='Philippe Docourt',
    description='An application that provides tools for displaying QR codes on your Django site.',
    long_description="""This application provides tools for displaying QR codes on your `Django <https://www.djangoproject.com/>`_ site.

This application depends on the `qrcode <https://github.com/lincolnloop/python-qrcode>`_ python library which requires the `Pillow <https://github.com/python-pillow/Pillow>`_ library in order to support PNG image format. The Pillow library needs to be installed manually if you want to generate QR codes in PNG format; otherwise, only SVG is format is supported.

This app makes no usage of the Django models and therefore do not use any database.

Only Python >= 3.5 is supported.""",
    install_requires=['qrcode', 'django'],
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Natural Language :: English'
    ],
    keywords='qr code django',
)
