# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='audioprep',
    version='1.1.3',
    description=(
        'AI audio preparation tools, including audio trimming, duration calculation, and subtitle correction.'
    ),
    keywords=(
        "audio, audio processing, audio trimming, audio duration, subtitle correction, AI tools"),
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding='utf-8').read(),
    author='abo123456789',
    author_email='abcdef123456chen@sohu.com',
    maintainer='abo123456789',
    maintainer_email='abcdef123456chen@sohu.com',
    license='MIT License',
    install_requires=[
        "pydub>=0.25.1",
        "librosa>=0.10.0",
        "wave>=0.0.2",
    ],
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ])
