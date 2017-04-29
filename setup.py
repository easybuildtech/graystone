from setuptools import setup

setup(name='graystone',
      version='0.1',
      description='Robotic Toolbox',
      url='http://github.com/easybuildtech/graystone',
      author='Easy Build Tech',
      author_email='ben@easybuildtech.com',
      license='MIT',
      packages=['graystone'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)