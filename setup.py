
from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='zomato_rating_prediction',
    version='0.0.1',
    author='Ayan Biswas',
    author_email='biswas.ayan1997@gmail.com',
    install_requires=["scikit-learn","pandas","seaborn","numpy"],
    packages=find_packages()
)
