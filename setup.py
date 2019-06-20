import setuptools

from threadsafevariable import __version__

setuptools.setup(
    name = "threadsafevariable",
    version = __version__,
    url = 'https://github.com/web2py/threadsafevariable',
    license = 'BSD',
    author = 'Massimo Di Pierro',
    author_email = 'massimo.dipierro@gmail.com',
    maintainer = 'Massimo Di Pierro',
    maintainer_email = 'massimo.dipierro@gmail.com',
    description = 'A library to make object attributes that are thread safe',
    content_type = "text/markdown",
    packages = ['threadsafevariable'],
    include_package_data = True,
    zip_safe = False,
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
)
