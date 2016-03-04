"""
Twisted Websocket server that talks with mongo
"""

from setuptools import setup, find_packages

setup(name='tornadowebsocket',
      version='1.0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={'console_scripts': [
          'tornadowebsocket = tornadowebsocket.server:main']},
      install_requires=['tornado==4.3',
                        'motor==0.5'])
