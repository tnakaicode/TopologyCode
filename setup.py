
from setuptools import setup

setup(name='topologicpy',
      version='0.3.4',
      description='Topologic',
      license='GPL',
      url="https://github.com/wassimj/topologicpy.git",
      author="wassimj",
      author_email="jabiw@cardiff.ac.uk",
      packages=['topologicpy'],
      package_dir={'topologicpy': 'topologicpy'},
      package_data={'topologicpy': ['assets/*',
                                    'bin/linux/topologic/*',
                                    'bin/windows/topologic/*']},
      zip_safe=False
      )

# python setup.py bdist_wheel
# pip install .\dist\topologicpy-0.2.2-py3-none-any.whl --force-reinstall
