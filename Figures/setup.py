from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='FiguresLib',
    version='0.0.1',
    author='i_love_natasha',
    author_email='diekilljoyzz@gmail.com',
    description='Calculating the area of shapes',
    long_description=readme(),
    logn_description_content_type='text/markdown',
    url='https://github.com/Dr1DeX/figures',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='figures lib',
    project_urls={
        'GitHub': 'https://github.com/Dr1DeX/figures'
    },
    python_requires='>=3.6'
)
