import os

from setuptools import setup, find_packages

VERSION = '0.4.5'


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid',
            'SQLAlchemy',
            'transaction',
            'pyramid_tm',
            'pyramid_debugtoolbar',
            'six',
            'zope.sqlalchemy']

setup(name='pyramid_cas',
      version=VERSION,
      description='A CAS client for use with the Pyramid web framework',
      long_description=README + '\n\n' + CHANGES,
      classifiers=['Programming Language :: Python',
                   'Framework :: Pyramid',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                   'License :: OSI Approved :: Apache Software License'],
      author='Ryan Fox',
      author_email='ryan@foxrow.com',
      url='https://github.com/ryanfox/pyramid_cas',
      keywords='web pyramid pylons cas authentication',
      license='Apache license',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite='pyramid_cas',
      entry_points="""\
      [paste.app_factory]
      main = pyramid_cas:main
      """,
      paster_plugins=['pyramid'])
