This is my first E Commerce Application

PBD Assignment 1

Step by Step Method:
Creating/Setting Up Application
1. running django-admin startproject to create the required files with settings and configuration to start a django project
2. created a new application by running manage.py startapp main1 (I used main1 since there was an error saying main was taken already)
Routing
3. added main1 into settings.py INSTALLED APPs list and urls.py
4. created a urls.py file within the main1 app to handle app specific routing
5. Routing for the index in urls.py (main1 file)
Model Creation
6. defined the requested model in assignment 2 (nama, harga and description)
7. Performed required migrations of the model to create the database schema for the product model
Function
8. Creating a function index containing my name, application and class that would return a html template
9. Created a new folder template containing main1.html
Uploading and Deployment (NOTE: Since currently there is an error with PWS, deployment cannot be done)
10. Create a new project on PWS and save the key code 
11. Add our PWS deployment URL into the allowed hosts
12. Perform Project Command Instruction (git remote, commit, branch)

Illustration
[Client Browser]  -->  [urls.py]  -->  [views.py]  -->  [models.py] (optional)  -->  [template HTML]  -->  [Client Browser]

Client: Sends an HTTP request to the Django application.
urls.py: Routes the request to the appropriate view based on the URL pattern.
views.py: Handles the request, potentially fetching data from the models.py (database).
models.py: Interacts with the database and returns data to the view.
Template HTML: The view renders an HTML template with data passed from the view, and the response is sent back to the client.

Purpose of Git:
Git helps to track changes within the software code and make comments when pushed into github. This helps user to maintain and organise its history, especially for other developers to know where the previous dev left off

Why Django?
Django starapp configuration has every file required for web development. It is also alot easier compared to Java or C++ with a few exceptions and some readable code. Django contains a naming system for every function and component e.g HTTP responses would fall under the views.py

Why is DJango called an ORM?
ORM, defined as object-relational mapping layer, where it allows one's application to interact with databases such as PostgreSQL or MySQL. Instead of having to write SQL queries to pull data from the database, one could use python objects and methods, which the ORM translates to SQL commands, to conduct the user's request.


Created by Sugonamu