from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Data_Science_Project",
    version="0.1",
    author="Bhumil Kheni",
    author_email="bhumilkheni24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
