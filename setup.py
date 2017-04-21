
from setuptools import setup

setup(
    name='euler',
    version='0.0',
    py_modules=['euler'],
    install_requires=[
        'Click',
        'requests',
        'BeautifulSoup4',
        'Jinja2',
        'html2text',
    ],
    entry_points='''
        [console_scripts]
        euler=euler:cli
    '''
)