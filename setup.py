from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str) -> List[str]:
    ''''
    Es funcion devuellve la lista de requirements
    '''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
    name='mlproject1',
    version='0.0.1',
    author='Ivan',
    author_email='ivanvk96@gmail.com',
    packages=find_packages(),
    install_requieres=get_requirements('requirements.txt')

)