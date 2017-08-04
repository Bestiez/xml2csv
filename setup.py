"""
writes setup.py in distutils to create a zip file
command to run this python setup.py sdist --format zip
"""

from distutils.core import setup

setup(
    name="xml2csv",
    version='1.0',
    data_files = ['files/xml_file.xml','files/csv_file.csv','xml2csv.py'],

    #metadata
    author='Ritesh Kumar',
    author_email='rithu.ritesh@gmail.com',
    description='Parse a complicated xml and convert that to a csv file.',
    license='Public Domain',
)