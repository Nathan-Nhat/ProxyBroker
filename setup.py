from setuptools import setup, find_packages #  find_package_data

PACKAGE = "pyproxychecker"
NAME = PACKAGE
DESCRIPTION = "Asynchronous proxy checker. Support: HTTP, CONNECT(HTTPS), SOCKS4, SOCKS5"
AUTHOR = "Constverum"
AUTHOR_EMAIL = "constverum@gmail.com"
URL = "https://github.com/constverum/PyProxyChecker"
VERSION = __import__(PACKAGE).__version__

with open("README.rst", 'r') as f:
    longDescr = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=longDescr,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    packages=find_packages(), # exclude=["tests.*", "tests"]
    install_requires=[],
    platforms="any",
    # package_data=[PACKAGE],
    # package_data=find_package_data(
    #         PACKAGE,
    #         only_in_packages=False),
    # include_package_data=True,
    package_data = {
        '': ['data/*.txt', 'data/*.mmdb', 'data/*.dat', 'LICENSE'],},
#     data_files=[
# #               ('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
#         ('/opt/local/myproject/etc', ['myproject/config/settings.py', 'myproject/config/other_settings.special']),
#         ('/opt/local/myproject/etc', [os.path.join('myproject/config', 'cool.huh')]),
# #
#         ('/opt/local/myproject/etc', [os.path.join('myproject/config', 'other_settings.xml')]),
#         ('/opt/local/myproject/data', [os.path.join('myproject/words', 'word_set.txt')]),
#     ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Proxy Servers",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords='async asynchronous proxy checker http https connect socks socks4 socks5',
    zip_safe=False,
)