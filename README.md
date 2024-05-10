# **Web Services and Application Big Project**

This repository stores the Web Services and Application project assigned as part of the Web Services and Application module.

The Web Services and Application module was undertaken in the third semester of Higher Diploma in Science in Computing in Data Analytics, January-May 2024.

## **Table of Contents**

- [Introduction](#introduction)
- [Project Contents](#project-contents)
    - [playerDAO](#playerdaopy)
    - [server](#serverpy)
    - [create_table](#create_tablepy)
    - [config file](#config-file)
    - [playerviewer](#playerviewerhtml)
    - [clubviewer](#clubviewerhtml)
- [Online Hosting](#online-hosting)
- [Running the Program](#running-the-program)
- [References](#references)

## **Introduction**
A web application was created for a database containing tables of football players and football clubs, hosted online using PythonAnyhere (https://rachelking.eu.pythonanywhere.com/playerviewer.html). The application allows the user to view both tables in the database, and make changes to the tables by creating, updating or deleting data.

## **Project Contents**
The repository contains a number of files required to create and host the web application. The files contained in the repository are:

    - playerDAO.py
    - server.py
    - playerviewer.html
    - clubviewer.html
    - create_table.py
    - config file

### **playerDAO.py**
The playerDAO.py file contains the python code for the application that acts as the link between the database and the main application. The DAO (Date Access Object) looks after adding, updating, retrieving and deleting data from the MySQL database. [[1]](#1)

### **server.py**
The server.py file is a Flask application which acts as the backend server. The server sets the route the returns specific text when the root url is accessed. Flask is a Python web framework, and is used to deploy a simple web application to a local server. [[2]](#2)

### **create_table.py**
This file contains code to access a database and create a table in the database. The code in this file can be adapted to create any type of table required.

### **config file**
The config file contains the details required to access the database (host name and password), in this case the MySQL database contained in my online development environment on PythonAnywhere.

### **playerviewer.html**
The playerviewer file is a html (HyperText Markip Language) file which is the core language of the world wide web. The html file defines the content and basic structure of the web page for viewing football players in the database. Styles were applied to the html page to improve the aesthetics of the page. [[3]](#3)

### **clubviewer.html**
Similar to the playerviewer file, the clubviewer file defines the content and basic structure of the web page for viewing football clubs in the database. Styles were applied to the html page to improve the aesthetics of the page. [[3]](#3)


## **Online Hosting**
The application is hosted online using the online web hosting service PythonAnywhere. A Github repostitory, containing all the required code, is used to deploy the application to the server.

## **Running the Program**
The files above were deployed to PythonAnywhere using a repository on Github named "deploytogithub" - https://github.com/rachel-king4/deploytogithub (should be named deploytopythonanywhere, this was named incorrectly in error).  This repository, wsaa_bigproject, contains the files in the deploytogithub repository demonstrating how the code was written to produce the web application visible at https://rachelking.eu.pythonanywhere.com/playerviewer.html. The web application was set up on PythonAnywhere by setting the source code and working directory to reference the applicable directory. This can be viewed at https://eu.pythonanywhere.com/user/rachelking/webapps/#tab_id_rachelking_eu_pythonanywhere_com.

To view the player table, the following link can be pasted into a web browser:

https://rachelking.eu.pythonanywhere.com/playerviewer.html

Similarly, to view the club table, the following link can be pasted into a web browser:

https://rachelking.eu.pythonanywhere.com/clubviewer.html

The club table viewer is accessible through a button on the player viewer html page, and vice versa. The html pages contain buttons whereby players can be created, updated and deleted and clubs can be created and deleted. 

The list of players in the player table in json format can be accessed at https://rachelking.eu.pythonanywhere.com/players. Similarly, the list of clubs in the club table in json format can be accessed at https://rachelking.eu.pythonanywhere.com/clubs.

To view a player or club by its ID, add the id number to the end of https://rachelking.eu.pythonanywhere.com/players/ or https://rachelking.eu.pythonanywhere.com/clubs/ (e.g. https://rachelking.eu.pythonanywhere.com/players/1).


## **References**

The main reference for this project was material provided through lectures and code by module lecturer Andrew Beatty [[4]](#4)

<a id="1">[1]</a>
(Stackoverflow.com [2021](https://stackoverflow.com/questions/69677507/data-access-object-dao-in-python-flask-sqlalchemy))

<a id="2">[2]</a>
(Codeacademy.com [n.d.](https://www.codecademy.com/article/deploying-a-simple-python-script-with-flask))

<a id="3">[3]</a>
(Mozilla.org [n.d.](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Styling_tables))

<a id="4">[4]</a>
(Github.com [2024](https://github.com/andrewbeattycourseware/wsaa-course-material))