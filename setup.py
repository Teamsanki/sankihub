
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'sankihub',        
  packages = ['sankihub'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'sankihub Logo Generator', 
  author = 'TEAM SANKI',                  
  author_email = 'teamsanki001@gmail.com',     
  url = 'https://github.com/Teamsanki/sankihub',   
  download_url = 'https://github.com/Teamsanki/sankihub/archive/1.2.tar.gz',    
  keywords = ['sankihub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
