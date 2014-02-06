from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='pynotify_daemon',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Aur\xc3\xa9lien Matouillot',
      author_email='a.matouillot@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'SQLAlchemy',
        'zope.sqlalchemy',
        'sqla_declarative',
        'python-daemon',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      notificator_daemon = pynotify_daemon.notification_daemon:main
      notificator_server = pynotify_daemon.server:main
      notificator_client = pynotify_daemon.client:main
      """,
      )
