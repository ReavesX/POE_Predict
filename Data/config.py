"""
    File: config.py
    Author: Donald Jackson
    Date Modified: 06/17/2024

    Desc: File contains the configuration settings for the POE Price Database; 
          The user will have to set their system environment variables to whatever 
              their value is for the program to run properly;
          This utilizes a MongoDB database.
"""

DB_URL = f'{MongoDB_Address}'
Name = f'{DB_Name}'
Collection = f'{Collection_Name}'