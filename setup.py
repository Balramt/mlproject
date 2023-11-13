from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # Here each line of requirments.txt file is read along with /n (new line characters )
        requirements=[req.replace("\n","") for req in requirements]

        # Now we added '-e.' into requirments.txt file to trigger the setup.py, so we need to remove the '-e.' so that other package are installed properly 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name= 'mlproject',
    version = '0.0.1',
    author = 'Balram',
    author_email='balramt02@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)