from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function takes a file path as input and returns a list of strings containing the names of the packages.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='prashant',
    author_email='prashant@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
