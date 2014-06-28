# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from scraper import __version__

setup(
    name=u'webscraper-core',
    version=__version__,
    description=u"Just an easy way to get Facebook and Twitter Profiles",
    long_description=u'''
    Just an easy way to get Facebook and Twitter Profiles
    ''',
    keywords='twitter facebook profile scrap',
    author=u'Victor Pantoja',
    author_email='victor.pantoja@gmail.com',
    url='https://github.com/victorpantoja/scraper',
    license='MIT',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python'],
    packages=find_packages(),
    package_dir={"scraper": "scraper"},
    include_package_data=True,

    install_requires=[
        "nose==1.1.2",
        "coverage==3.5.1",
        "simplejson",
        "pybreaker==0.2.2",
        "pymongo==2.7.1",
        "requests==2.3.0"
    ]
)
