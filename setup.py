from setuptools import setup, find_packages
from setuptools_scm import get_version

# Dynamically write the version to _version.py
def write_version_file():
    version = get_version()
    with open('src/event_listener/_version.py', 'w') as f:
        docstring = '""" version of package """'
        f.write(f"{docstring}\nVERSION = '{version}'\n")

if __name__ == "__main__":
    write_version_file()
    setup(
        name='SpectrogramUtils',
        use_scm_version=True,
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        author='Sacha Renault',
        author_email='',
        description='Have c# event handler',
        long_description=open('readme.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/sacha-renault/event-listener',
        license='MIT',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
    )