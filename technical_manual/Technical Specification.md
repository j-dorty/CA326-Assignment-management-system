---
title: Technical Specification
---

# Technical Specification


<center> <h1>Assignment Management System (AMS)</h1> </center>

### Prepared by: Muhammad Umar (17313893) & Jack Doherty (17351591)

#### 3rd Year Project 

<!-- #### Muhammad Umar: 17313893 

#### Jack Doherty: 17351591 -->

#### Supervisor: Tomas Ward

#### Table of Contents

[Introduction](#Introduction) 

[1.1 Overview](#1.1-Overview) 

[1.2 Glossary](#1.2-Glossary) 

[1.3 Initial Design](#1.3-Initial-Design)

[System Architecture](#System-Architecture) 

[2.1 Web Application Architecture](#2.1-Web-Application-Architecture) 

[High-Level Design](#High-Level-Design) 

[3.1 Context Diagram](#3.1-Context-Diagram) 

[3.2 Data Flow Diagram](#3.2-Data-Flow-Diagram)

[3.3 Class Diagram](#3.3-Class-Diagram)

[Problems Faced & Their Solutions](#Problems-Faced-&-Their-Solutions) 

[Problem 1](#Problem-1) 

[Problem 2](#Problem-2) 

[Problem 3](#Problem-3) 

[Problem 4](#Problem-4) 

[Problem 5](#Problem-5) 

[Final Design](#Final-Design)

[Installation Guide](#Installation-Guide) 

## Introduction

### 1.1 Overview
The product that we will be developing is an Assignment Management System (AMS), which will manage the secure submission, management and distribution of assignment marks in a GDPR-compliant manner. Users in the system will have one of two roles, Teacher or Student. Ideally, user authentication will use the University’s LDAP system.

### 1.2 Glossary
**FRONTEND**
* **HTML:** Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.
* **CSS:** Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML.
* **BOOTSTRAP:** Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
* **JAVASCRIPT:** An object-oriented computer programming language commonly used to create interactive effects within web browsers.
* **JQUERY:** jQuery is a JavaScript library that allows web developers to add extra functionality to their websites especially with DOM manipulation.

**BACKEND**

* **Django:** Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern.
* **SQLite:** SQLite is a relational database management system (RDBMS)

## Hosting Platform

* **Heroku:** Heroku is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, initially it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go. We planned to use the Heroku hosting service to host our finished Rest API.



## Initial Design

* Initially the design of our system was to create a web based application available only to the students and teachers in DCU. Our initial plan was to make use the DCU LDAP system to create and verify our user accounts anf though this allow only DCU students and Teachers avail of our application.

* At first we planned to deploy and host our application on an Apache Server using a linux environment.
* The initial high level design of our system is as detailed in the diagram below

![](https://i.imgur.com/2ITYXFI.png)

* as you can see we planned to have 2 distinct seperate User types with access to different portions and hence functions of the application

*
## System Architecture

### 2.1 Web Application Architecture

![](https://i.imgur.com/GkjhIyA.jpg)


## High-Level Design


### 3.1 Context Diagram
![](https://i.imgur.com/53nEzoM.jpg)


### 3.2 Data Flow Diagram
![](https://i.imgur.com/q0XNlyq.jpg)


### 3.3 Class Diagram
![](https://i.imgur.com/P96MOw6.jpg)


## Problems Faced & Their Solutions


### Problem 1
Description: Learn how to work with *.NET CORE* framework which uses *C#* as it's language and see it's compatibility with our project.

Solution: We initially decided to research and learn more about *.NET CORE* as we saw this as an oppurtunity to learn a new and potentially very usefu; tool to both of us in our upcoming internships.


### Problem 2
Description: *.NET CORE* turned out to be more difficult and time consuming to learn.

Solution: As we had less than a month to implement our design of this project, we decided to move away from the *.NET CORE* framework to a framework that supported a more rapid development process and has less of a learnign curve. This led us to the *Django* Rest API design framework. We decided to switch our efforts from learning the *.NET CORE* framework and instead as we already had somewhat of a knowledge base under us in the python programming language decided to focus our efforts on learning to develope using the Django* Rest API design framework. 

### Problem 3
Description: Create custom User models within the Django REST API framework.

Solution: *Django* gives you a built-in models which lets you create users with it's default template/definition of a user. In our case we need different users (Teachers/Students) with their own attributes. We researched in *Django* documentation on custom user models and we were able to make users with our own defined models.

### Problem 4
Description: The management and correct querying of our database.

Solution: Our system consists of multiple data types, that all realte to one another. These are  Users of two different types those being a student user type and a teacher user type, Modules which are groups that consist of a Teacher and ID and gives membership to student user types through a data type we have implemented called Membership. The Membership data type maps the relation from one Student user to one module instance, and though multiple instances of this memberhsip model we were able to populate our module instances with multiple student users. 

### Problem 5
Description: Authenticate Users as adviced

Solution: Our project description told us to verify the user with DCU LDAP system but when we attempted to followed up on this requirement we were informed by the ISS team that students are not permitted access to the the DCU LDAP system. In spite of this we decided to act as though we already had thsi information and manually add users to our system, giving them pre-assigned passwords and usernames in a similar vein to how DCU students interact with the Loop assignment submission system.


## Final Design

* The final design and implementation of our sytem was alrgely in line with what we had initially designed, however there ares some differences from the orginal design. Initkially we had planned to have 2 distinct different user types and use there different attributes to dtermine permissions and there access to functions. Instead we decided to implement a single user type but with some differing attributes and instead of deciding permissions based off of a specific user type instead we check this in built user attribute to determine permissions and acces to functions 



## Installation Guide
First install PIP

* sudo apt-get install -y python3-pip

Once pip is installed run

* pip install requirement.txt

This file will install all the dependencies needed inorder to run this project locally.