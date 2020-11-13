import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
print(HERE)
# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pipmate",
    version='0.1.1-alpha.1',
    license='MIT',
    description = 'Move between pipfiles, pyproject.toml and requirements.txt with ease!',
    long_description=README,
    long_description_content_type="text/markdown",
    url = 'https://github.com/srujandeshpande/pipmate',
    download_url = 'https://github.com/srujandeshpande/pipmate/releases/tag/v0.1.0',
    author = 'Srujan Deshpande',
    author_email = 'srujan.deshpande@gmail.com',
    keywords = ['Poetry', 'PyPip', 'Dependencies'],
    install_requires=[
            'cleo',
            'toml',
        ]
    #packages=["reader"],
    #include_package_data=True,
    #install_requires=["feedparser", "html2text"],
    #entry_points={
    #    "console_scripts": [
    #        "realpython=reader.__main__:main",
    #    ]
    #},
)
