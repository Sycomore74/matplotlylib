# try:
#     from setuptools import setup
# except ImportError:
from distutils.core import setup

DESCRIPTION = "Matplotlib to Plotly Converter"
LONG_DESCRIPTION = open('README.md').read()
NAME = "matplotlylib"
AUTHOR = "Andrew Seier"
AUTHOR_EMAIL = "andseier@gmail.com"
MAINTAINER = "Andrew Seier"
MAINTAINER_EMAIL = "andseier@gmail.com"
URL = 'http:/mpld3.github.com'
DOWNLOAD_URL = 'https://github.com/mpld3/matplotlylib'
LICENSE = 'MIT'
VERSION = '0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      install_requires=['plotly', 'matplotlib'],
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['matplotlylib',
                'matplotlylib/mplexporter',
                'matplotlylib/mplexporter/renderers'])
