'''
The setup.py file is essential for packaging and distributing Python projects.
It is used by setuptools to define the configuration of your project such as meta data, 
dependencies, and entry points.

Metadata = information that describes your project’s data, files, and structure.

Why metadata is important:
  Helps others understand your project quickly
  Makes the project reproducible
  Avoids confusion about columns, files, versions, and sources
  Very important in data science, ML, and software projects
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """ 
    This function will return the list of requirements.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:

            #read lines fromm the file
            lines = file.readlines()
            #process each line
            for line in lines:
                #strip whitespace and newlines
                requirement = line.strip()  
                #ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt File not found error')
    
    return requirement_lst

print(get_requirements())

setup(
    name = 'Network Security',
    version = '0.0.1',
    author= 'Ganesh Gunjal',
    author_email= 'ganeshgunjal118@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements()
)
