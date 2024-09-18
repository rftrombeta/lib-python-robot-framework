import re
from setuptools import setup, find_packages

PACKAGE_NAME = 'lib_name'
SOURCE_DIRECTORY = 'src'
SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')

source_packages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
proj_packages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in source_packages]

setup(
    name=PACKAGE_NAME,
    packages=proj_packages,
    package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    description='Example: Useful and applicable functions in automation projects with Python and Robot Framework',
    url='https://github.com/rftrombeta/lib-python-robot-framework',
    author='Rodrigo Trombeta',
    author_email='rftrombeta@gmail.com',
    version="1.1.1",
    python_requires='>=3.12.0',
    install_requires=["robotframework",
                      "robotframework-pabot",
                      "robotframework-requests",
                      "requests",
                      "xmltodict"]
)
