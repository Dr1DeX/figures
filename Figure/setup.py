from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()
    

setup(
    name='figure',
    version='0.0.1',
    author='i_love_natasha',
    author_email='diekilljoyzz@gmail.com',
    description='Calculating the area of ​​shapes',
    url='https://github.com/Dr1DeX/figures',
    packages=find_packages(),
    requires=['requests>=2.25.1'],
    keywords='files figures',

)