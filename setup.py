from distutils.core import setup

setup(
    name='yapbol',
    version='0.1',
    packages=['yapbol',],
    license='GNU Public License v3',
    description='Yet Another PBO Library',
    #long_description=open('README.txt').read(),
    download_url = 'https://github.com/overfl0/yapbol/archive/0.1.tar.gz',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['six'],
    keywords='arma pbo',
)

# Install in "editable mode" for development:
# pip install -e .
