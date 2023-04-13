# Responsible in creating machine learning application as a package for others to use as well. 
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

# Returns a list of strings
def get_requirements(file_path:str) -> List[str]: 
    """
    This function will return the list of python requirement packages
    Note that -e. in requirments.txt automatically triggers setup.py
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)

    return requirements 

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Rupesh",
    author_email = "rkdey95@gmail.com",
    packages = find_packages(),     # finds the __init__.py file in any of the folders. For us it's src. 
    install_requires = get_requirements("requirements.txt")
)
# IF setup.py runs successsfully then egg-info file / folder should come. 