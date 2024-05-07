# **Web Services and Application Big Project**

This repository stores the Web Services and Application project assigned as part of the Web Services and Application module.

The Web Services and Application module was undertaken in the third semester of Higher Diploma in Science in Computing in Data Analytics.

## **Table of Contents**

- Introduction
- Project Contents
    - playerDAO
    - server
    - create_table
    - config file
    - playerviewer
    - clubviewer
- Online Hosting
- Running the Program
- References

## **Introduction**
Web application for a database containing table of football players and football clubs, hosted online using PythonAnyhere (https://rachelking.eu.pythonanywhere.com/)

## **Project Contents**
The repository contains a number of files required to create and host the web application. The files contained in the repository are:

    - playerDAO.py
    - server.py
    - playerviewer.html
    - clubviewer.html
    - create_table.py
    - config file

### **playerDAO.py**
The playerDAO.py file contains the python code for the application that acts as the link between the database and the main application. The DAO (Date Access Object) looks after adding, updating, retrieving and deleting data from the MySQL database.

### **server.py**
The server.py file is a Flask application which acts as the backend server. The server sets the route the returns specific text when the root url is accessed. Flask is a Python web framework, and is used to deploy a simple web application to a local server.

### **create_table.py**
This file contains code to access a database and create a table in the database. The code in this file can be adapted to create any type of table required.

### **config file**
The config file contains the details required to access the database (host name and password), in this case the MySQL database contained in my online development environment on PythonAnywhere.

### **playerviewer.html**
The playerviewer file is a html (HyperText Markip Language) file which is the core language of the world wide web. The html file defines the content and basic structure of the web page for viewing football players in the database.

### **clubviewer.html**
Similar to the playerviewer file, the clubviewer file defines the content and basic structure of the web page for viewing football clubs in the database.


## Online Hosting
The application is hosted online using the online web hosting service PythonAnywhere. A Github repostitory, containing all the required code, is used to deploy the application to the server.

## **Running the Program**


## **References**



## Project Plan

- Create a web application in Flask that has a RESTfull API
- application link to one or more database tables
- create web page that can consume the API (performs CRUD operations on the data)
- host the server on a cloud hosting site (Azure, pythonanywhere)

Extra marks:
- looks nice
- more than one database table
- link to outside data source and analyse data in real time
- host online 