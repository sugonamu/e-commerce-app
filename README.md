PBD Assignment 2
-
This is my first E Commerce Application<br>

Step by Step Method:<br>
<B>Note: Ensure that the file has been intialized so when git push is conducted, changes will occur in your github repository too</B>

Creating/Setting Up Application<br>
1. Running django-admin startproject to create the required files with settings and configuration to start a django  (This also includes downloading the requirements.txt and adding .gitignore)
2. Created a new application by running manage.py startapp main1 (I used main1 since there was an error saying main was taken already when I was working on it)
Routing
3. Added main1 into settings.py INSTALLED APPs list and urls.py
4. Created a urls.py file within the main1 app to handle app specific routing
5. Routing for the index in urls.py (main1 file)
Model Creation
6. Defined the requested model in assignment 2 (nama, harga and description)
7. Performed required migrations of the model to create the database schema for the product model
Function
8. Creating a function index containing my name, application and class that would return a html template
9. Created a new folder template containing main1.html
Uploading and Deployment (NOTE: Since currently there is an error with PWS, deployment cannot be done)
10. Create a new project on PWS and save the key code 
11. Add our PWS deployment URL into the allowed hosts
12. Perform Project Command Instruction (git remote, commit, branch. git push)

----
<b>List of Changes made in the repository:</b><br>

<b>Main1 Folder</b> 
1. README.md : To answer all these questions and give a brief explaination on how I created this project
2. Requirements.txt : Self added txt file to easily download all required libraries by running pip install -r requirements.txt
3. views.py: Added definition for variables app_name, your_name and your_class to be displayed on the html page when opened
4. urls.py: added "from . import views" to route the root url and /info/ to info_view 
5. models.py: Creating the model for the requested product to show (nama, harga, description) each of it having its own
6. main1.html: Display page of the app when opened

<br><b>e_commerce_app Folder</b><br>
1. urls.py: Added include from django.urls to include urls from the main1 app
2. settings.py: added main1 as an installed app and added 127.0.0.1 (loopback ip for local machine) and pws link for our app to be hosted 

<br><b>Other Folders</b><br>
1. main folder: was testing again whether main would work (this happened after I finished the project)
2. Env folder: to create the virtual environment folder to run a VE for running live servers



-----
<b>Files that were added</b>
- .gitignore : helps to ignore certain files to be tracked by git
- requirements.txt : running pip install -r requirements.txt will help download all required libraries for this application
<br>

<b>Libraries to download in requirements.txt</b>
- Django: To create the framework of the project
- Gunicorn: WSGI server to run Django application
- Whitenoise: Middleware to serve static file in production
- psycopg2-binary: PostgreSQL Adapter (ORM related)
- requests: Library to make HTTP requests to external services
- urllib3: HTTP client for lower-level control over HTTP connection
-----
Illustration <br>
[Client Browser]  -->  [urls.py]  -->  [views.py]  -->  [models.py] -->  [template HTML]  -->  [Client Browser]

- Client: Sends an HTTP request to the Django application.
- Urls.py: Routes the request to the appropriate view based on the URL pattern.
- Views.py: Handles the request, potentially fetching data from the models.py (database).
- Models.py: Interacts with the database and returns data to the view.
- Template HTML: The view renders an HTML template with data passed from the view, and the response is sent back to the client.
----
Purpose of Git:
Git helps to track changes within the software code and make comments when pushed into github. This helps user to maintain and organise its history, especially for other developers to know where the previous dev left off

Git Commands:
- git add _____ : adds _____ file that has experienced changes
- git add . : adds all file that has experienced changes
- git commit -m "message" = message to add beside the file on what changes has been done (useful when collaborating with other devleopers)
- git branch -M main/master: creates a new branch called main/master (depending on your repo)
- git push -u origin main: push the changes made on the files onto github
- git remote (name) (url): To use common repository that all team members use to exchange their changes
----
Why Django?<br>
Django starapp configuration has every file required for web development. It is also alot easier compared to Java or C++ with a few exceptions and some readable code. Django contains a naming system for every function and component e.g HTTP responses would fall under the views.py


Why is DJango called an ORM?<br>
ORM, defined as object-relational mapping layer, allows one's application to interact with databases such as PostgreSQL or MySQL. Instead of having to write SQL queries to pull data from the database, one could use python objects and methods, which the ORM translates to SQL commands, to conduct the user's request.


PBD Assignment 3
- 
<b>NOTE: Image current does NOT work but somehow user can upload still (Since it was optional and not required I will not fix it for now lol)</b> <br><br>
<B>Basic Checklist</B>
- Initialize your repo (git init)
- Set up your virtual environment (env\Scripts\activate)

<b>Step by Step/Walkthrough (With Explanation)</b><br>
1. Created 2 new html page (addproduct.html and base.html) . The purpose of base.html just helps to use a consitant layout between all pages, in other words, template inheritance. This also makes it easier if the basic layout of the page requires changes e.g changing from pink to blue, changing within the base would change for all pages rather than having to go through every single page to change it
2. Edited my HTML page (main1) such that it will use the model (name, price, description and images) and also a add product button which is linked towards the addproduct.html page.
3. Planned to add images, thus added an image model into models.py, conducted makemigrations and migrate to succesfully migrate the model also import uuid to give each product added a unique id e.g Toilet has an id of 1 and Zingus has an id of 4 (Refer from image on JSON or XML)
4. Added templates(seperate folder from main1 and addproduct) into 'DIRS' in settings.py so base.html would be detected as a template file
5. Created a new file called forms.py to create the structure of the form to add a new product where the fields are name, price, description and image
6. Major changes in views.py: Functions info_view has a new context (products: product) to display whatever product that has been added. Function add_product handles the form to determine if the product can be added or not and if so, redirects the user to home (purpose of import redirect). 
7. Added a URL path on URLPATTERNS in main1/urls.py to access the function add_product added in views.py earlier. <br>
<B> XML and JSON Data Stuff </B>
8. Go back to views.py to add import HttpResponse and serializers for XML files. Added the show_xml that receives a parameter request with a variable (data) to store all the newly added products. XML by ID is pretty much the same thing but instead we can return specifically the product we want e.g the info for product id 1 and if the product doesnt exist, an error message would display. The HttpResponse is to receive the data in a structured format for users who wants XML data
9. Head to main1/urls.py to add another URLPATTERN, in this case, the xml path and xml by id path (URL Routing). When opened on a local host, this will return the XML response, whether it is all products or a specific product. These are the links it can be tested in <br>http://localhost:8000/xml/ XML<br>http://localhost:8000/xml/1/ XML by ID
10. Similarly for JSON, we need to define the data (products), but JSON is more 
neater, listing out side by side products' price, name and description. JsonResponse works the same as HttpResponse but for JSON. Similarly with XML by ID, JSON by id is just tracking by product id and giving a cleaner and more specific display for x product (according to their id). Once again if product id not found, an error message will be displayed
11. Once again, head to main1/urls.py to add another URLPATTERN for json and json by id path (URLROUTING). When opened on a local host, this will return the JSON response, whether it is all products or a specific product. These are the links it can be tested <br>http://localhost:8000/json/ JSON<br>http://localhost:8000/json/1/ JSON by ID


Why do we need Data Delivery?


Which is better JSON or XML? Why?


Why is JSON more popular than XML?


What is the use of is_valid()?



Why do we need method in forms?


What is a csrf_token and why do we need it? (Explain what happens if we dont use it)










XML <br>
https://imgur.com/eWYqw8N <br>
JSON <br>
https://imgur.com/6KLzGGc<br>
XML by ID <br>
https://imgur.com/Y8hVhj6<br>
JSON by ID<br>
https://imgur.com/kyLT0Ga<br>


Created by Sugonamu (Will KKI)