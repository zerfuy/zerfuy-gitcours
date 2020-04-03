# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='easy-pytube',
    version='1.0',
    description='easy console interface for pytube',
    author='lefeRittuelle',
    author_email='pasTesOignons',
    url='',
    install_requires=[
        'pytube3',
        'ffmpeg-python',
        'moviepy'
    ],
    packages=find_packages(),
    package_data={'': ['conf.ini', "ffmpeg.exe"]},
    entry_points={
            'console_scripts': [
                'getvideo=easy_pytube.scripts.runner:run',
            ],
        }
    )