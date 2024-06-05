#Project : EMIS Assessment
##Description
The project aims to convert FHIR (Fast Healthcare Interoperability Resources) JSON data into a structured tabular format. It involves setting up tables in a MySQL database to store the converted data.

##Programming Language
Python is the chosen programming language for implementing this project.

##Database Layer
MySQL serves as the database layer for storing the structured data. Version 8 of MySQL is recommended.

##Installation / Requirements
MySQL Server v8: Install MySQL Server version 8 and create a database named "patient_db" using the provided SQL command.

>CREATE DATABASE patient_db;
##Python Packages: 
Install required Python packages from PyPi using pip.

>pip install pymysql

>pip install pytest

##Usage
Execute the main script main.py using Python to run the project.

>python main.py

This documentation provides a clear guide for setting up the project environment and running the conversion process. If you need further assistance or clarification on any aspect, feel free to ask!