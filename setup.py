from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements] # removing the newline character while reading the libraries 
        # in the requirements file as by default it is read with a newline character that is \n that why need to remove it
    # if '-e .' is present in the requirements, we will remove it
    # as it is used for editable installs and not needed in the setup.py
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    
name='mlproject',
version='0.0.1',
author='Akanksha',
author_email= 'akankshadash1@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
# entry_points={
#     'console_scripts': [
#         'mlproject=mlproject.__main__:main'
#     ]
# },
# description='A machine learning project template',
# long_description=open('README.md').read(),
# long_description_content_type='text/markdown',
# url='  
)  