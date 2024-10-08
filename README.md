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
**Why Django?**<br>
Django starapp configuration has every file required for web development. It is also alot easier compared to Java or C++ with a few exceptions and some readable code. Django contains a naming system for every function and component e.g HTTP responses would fall under the views.py


**Why is DJango called an ORM?**<br>
ORM, defined as object-relational mapping layer, allows one's application to interact with databases such as PostgreSQL or MySQL. Instead of having to write SQL queries to pull data from the database, one could use python objects and methods, which the ORM translates to SQL commands, to conduct the user's request.


PBD Assignment 3
- 
<b>NOTE: Image current does NOT work but somehow user can upload still (Since it was optional and not required I will not fix it for now lol)</b> <br><br>
<B>Basic Checklist</B>
- Initialize your repo (git init)
- Set up your virtual environment (env\Scripts\activate)

<b>Step by Step/Walkthrough (With Explanation)</b><br>
1. Created 2 new html page (`addproduct.html` and `base.html`) . The purpose of `base.html` just helps to use a consitant layout between all pages, in other words, template inheritance. This also makes it easier if the basic layout of the page requires changes e.g changing from pink to blue, changing within the base would change for all pages rather than having to go through every single page to change it
2. Edited my HTML page (`main1`) such that it will use the model (name, price, description and images) and also a add product button which is linked towards the `addproduct.html` page.
3. Planned to add images, thus added an image model into `models.py`, conducted makemigrations and migrate to succesfully migrate the model also import uuid to give each product added a unique id e.g Toilet has an id of 1 and Zingus has an id of 4 (Refer from image on JSON or XML)
4. Added templates(seperate folder from main1 and addproduct) into 'DIRS' in settings.py so `base.html` would be detected as a template file
5. Created a new file called `forms.py` to create the structure of the form to add a new product where the fields are name, price, description and image
6. Major changes in `views.py`: Functions `info_view` has a new context (products: product) to display whatever product that has been added. Function `add_product` handles the form to determine if the product can be added or not and if so, redirects the user to home (purpose of import redirect). 
7. Added a URL path on URLPATTERNS in `main1/urls.py` to access the function `add_product` added in `views.py` earlier. <br>
<B> XML and JSON Data Stuff </B>
8. Go back to `views.py` to add import HttpResponse and serializers for XML files. Added the show_xml that receives a parameter request with a variable (data) to store all the newly added products. XML by ID is pretty much the same thing but instead we can return specifically the product we want e.g the info for product id 1 and if the product doesnt exist, an error message would display. The HttpResponse is to receive the data in a structured format for users who wants XML data
9. Head to `main1/urls.py` to add another URLPATTERN, in this case, the xml path and xml by id path (URL Routing). When opened on a local host, this will return the XML response, whether it is all products or a specific product. These are the links it can be tested in <br>`http://localhost:8000/xml/ `XML<br>`http://localhost:8000/xml/1/ `XML by ID
10. Similarly for JSON, we need to define the data (products), but JSON is more 
neater, listing out side by side products' price, name and description. JsonResponse works the same as HttpResponse but for JSON. Similarly with XML by ID, JSON by id is just tracking by product id and giving a cleaner and more specific display for x product (according to their id). Once again if product id not found, an error message will be displayed
11. Once again, head to `main1/urls.py` to add another URLPATTERN for json and json by id path (URLROUTING). When opened on a local host, this will return the JSON response, whether it is all products or a specific product. These are the links it can be tested <br>`http://localhost:8000/json/` JSON<br>`http://localhost:8000/json/1/` JSON by ID

-----

**Why do we need Data Delivery?**  
Data delivery is crucial for enabling users to interact with platforms by submitting or receiving data. In e-commerce, for instance, users submit data to add new products or make transactions. Effective data delivery ensures seamless data flow between users and the platform, enhancing functionality and user experience.

**Which is better JSON or XML? Why?**  
JSON is generally considered better than XML for most web applications due to its lightweight nature, ease of parsing, and human-readability. While XML supports more complex data structures, JSON is simpler, less verbose, and better suited for modern web applications, especially those dealing with APIs.

**Why is JSON more popular than XML?**  
JSON's popularity stems from its simplicity, smaller size, and ease of use compared to XML. JSON integrates seamlessly with JavaScript, making it a preferred format for web applications. Additionally, JSON's concise syntax makes data transmission faster and more efficient.

**What is the use of `is_valid()`?**  
In Django forms, `is_valid()` is used to check whether the submitted form data conforms to the validation rules defined in the form. If the form is valid, it returns `True`, allowing further processing of the data. Otherwise, it returns `False`, indicating errors in the form fields.

**Why do we need the method in forms?**  
The `method` attribute in forms specifies how the data is submitted to the server (either `GET` or `POST`). It determines how the form data is sent: `POST` for secure data submission like passwords or personal information, and `GET` for retrieving data. Choosing the correct method ensures proper handling of the data.

**What is a `csrf_token` and why do we need it?**  
A `csrf_token` (Cross-Site Request Forgery token) is a security measure that prevents malicious attacks where unauthorized commands are submitted on behalf of a user. Without it, attackers could exploit vulnerabilities by making requests to your server on behalf of the logged-in user, potentially compromising data integrity.




XML <br>
https://imgur.com/eWYqw8N <br>
JSON <br>
https://imgur.com/6KLzGGc<br>
XML by ID <br>
https://imgur.com/Y8hVhj6<br>
JSON by ID<br>
https://imgur.com/kyLT0Ga<br>


PBD Assignment 4
-
<b>Step by Step Explanation</b><br>
1. Imported usercreatorform and messages while also adding functions to `register (request)` so users do not need to keep creating new forms from scratch and message is just to display messages.
2. Create `register.html` for the register page where user can create an account together with having a password.
3. Import register in urls and add its path so users can be redirected to the page
4. Import login, authenticate and authenticationform while also adding function to login user where it will autheticate users trying to login. If the user is valid, meaning their account exists within the database, they will be shown the main page however if fail, it will return back to the login page 
5. Create `login.html` for the login page for users to login to their account with products theyve added
6. import login_user in urls and add its path so users can be redirected to the page
7. Similar concept with register and login: import logout in `views.py` and create the function where logging out would redirect to the login page. Add the logout button in the main1.html page, importing logout in urls and its path so users can be redirected 
8. Added the @login_required decorator to restrict access to logged-in users only. Users attempting to access the page were redirected to the login page if they were not authenticated.
9. Modified the login function to set a cookie named last_login with the timestamp of the user's login. This information was displayed on the main page to show when the user last logged in.
10. Updated the logout function to delete the last_login cookie when the user logged out, ensuring no stale cookie data remained.
11. Added a small HTML snippet to display the last_login cookie value on the main page, allowing users to see their last login session details.
12. Linked the Products model to the User model using a ForeignKey, so each mood entry was associated with the logged-in user who created it.
13. Modified the mood entry creation logic to assign the logged-in user to the user field before saving the mood entry to the database.
14. Adjusted the main page logic to display only the mood entries belonging to the logged-in user by filtering Products objects based on the current user.
15. During migration, assigned a default user (user ID 1) to existing Products records to prevent migration errors related to missing user data.
16. Updated the DEBUG setting in `settings.py` to toggle between production and development modes based on an environment variable for better security in a live environment.


 What is the difference between `HttpResponseRedirect()` and `redirect()`? <br>
- `HttpResponseRedirect()` is a method that directly returns an HTTP 302 response with a redirection URL, while `redirect()` is a more flexible shortcut that internally calls `HttpResponseRedirect()` and can take URLs, view names, or arguments. This makes `redirect()` more convenient and commonly used.

Explain how the MoodEntry model is linked with User!<br>
- The MoodEntry model is linked with the User model using a foreign key, ensuring that each mood entry is associated with a specific user. This relationship allows tracking which user created each entry, providing personalization and accountability within the application.

What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.<br>

- Authentication involves verifying a user's identity (e.g., checking credentials), while authorization determines what the authenticated user is allowed to access or do. When a user logs in, Django authenticates their credentials and creates a session using cookies to remember the logged-in state, enabling authorized actions.

How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use. <br>
- Django uses session cookies to remember logged-in users by storing a session ID on the client side and mapping it to a session object on the server. Cookies can also store preferences and track user behavior, but not all cookies are safe—if not secured properly, they can be exploited, leading to session hijacking.


PBD Assignment 5
-
<b>Step by Step Explanation</b><br>
1. added viewport and script tailwind: viewport allows the website to suit for mobile users and tailwind is for css (page aesthetics mainly)
2. added function for edit_product in `views.py`: function works by getting the id of the product then change it into a form where features can be edited and saved.
3. created `editproduct.html`: the page to edit the product
4. connected the url path in `urls.py`: html file can be accessed by main:edit_product now
5. added function for delete_product in `views.py`: function by getting the id of the product and deleting it completely from the database.
6. connected the url path in `urls.py`: clicking on anything with the path delete_product would run the function, deleting the product
7. button for edit product and delete product were added onto main.html
8. created a navigation bar which has cart, categories, products, home and logout in templates (same folder as `base.html`)
9. added {% include 'navbar.html' %} to `addproduct.html`,`editproduct.html` and `main1.html`
10. added whitenoise middleware to settings.py and a static folder to manage static files e.g images
11. created a global.css which is the universal look for certain features e.g forms
12. making all the other pages look aesthetically pleasing
13. added `card_info.html` to display app name, class and name
14. added `error.html` to display pages that are still unworked on (carts and categories)
15. added error function so user would be brought to error.html when carts or categories in navbar is clicked



 If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

1. **Inline styles**: These have the highest specificity and override other styles.
2. **IDs**: Selectors that target an ID (e.g., `#example`) are more specific than class selectors.
3. **Classes, attributes, and pseudo-classes**: Selectors that target classes (e.g., `.example`), attributes (e.g., `[type="text"]`), and pseudo-classes (e.g., `:hover`) have a lower priority than IDs.
4. **Elements and pseudo-elements**: These selectors (e.g., `div`, `p`, `::before`) have the lowest specificity.
5. **Universal selector**: The `*` selector applies to all elements but has the lowest specificity.

This hierarchy ensures that more specific styles override more general ones.

 Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!

- Responsive design is crucial in web application development because it ensures that applications function well on a variety of devices and screen sizes. With the increasing use of smartphones and tablets, having a responsive design helps improve user experience, accessibility, and engagement. An example of applications with responsive designs could be Gojek, an application without a responsive design would be time.gov, which is a government website. 


 Explain the differences between margin, border, and padding, and how to implement these three things!

- Margin is space outside the box, border is the line surrounding the box and padding is within the box/border.

 - `.example` { <br>
   ` margin: 20px; `  Space outside the border<br>
    `border: 1px solid black;` The border itself <br>
    `padding: 10px; `  Space inside the border *<br>



 Explain the concepts of flex box and grid layout along with their uses! <br>
- Flexbox is for one-dimensional layouts. Allowing items within a container to be aligned and distributed along a single axis (either horizontal or vertical) whereas grid layout is for two-dimensional layouts. Creating complex layouts using rows and columns.



Assignment 6
-

# Web Application Development

### Benefits of Using JavaScript in Web Development
JavaScript allows for dynamic, interactive, and responsive web applications. It runs on the client-side, reducing the load on servers, and enables asynchronous actions like loading data without refreshing the page. Additionally, it works across all modern browsers and offers extensive libraries and frameworks like React, Vue.js, and Node.js, streamlining both front-end and back-end development.

### Importance of Using `await` with `fetch()`
The `fetch()` function returns a promise, which represents an asynchronous operation. Using `await` pauses the execution of the code until the promise is resolved or rejected. If `await` is not used, the code would continue to run without waiting for the response, which could result in undefined data being used or errors in the application.

### Need for `csrf_exempt` with AJAX POST
Django includes Cross-Site Request Forgery (CSRF) protection, which prevents unauthorized actions on behalf of a logged-in user. When using AJAX POST, the CSRF token is usually required. By using the `csrf_exempt` decorator, we bypass this protection for the specific view, allowing the AJAX POST request to go through without needing the token. However, this should be used cautiously to avoid security risks.

### Why User Input Sanitization Cannot be Done Only in the Front-End
Sanitization on the front-end can be easily bypassed by malicious users, as they can manipulate the data sent to the server directly via developer tools or scripts. Therefore, back-end sanitization is crucial to ensure that no harmful input (e.g., SQL injection, XSS attacks) is processed by the server. Both layers of sanitization—front-end and back-end—are essential for robust security.

### Step-by-Step Implementation of Checklist
1. **JavaScript and AJAX Integration**: integrated JavaScript with AJAX to dynamically add new products without refreshing the page. I used `fetch()` to send data asynchronously.
2. **Handling CSRF Tokens**: applied the `csrf_exempt` decorator to the view handling AJAX POST requests. While this weakens CSRF protection, it simplifies the interaction for this demo.
3. **Input Sanitization in Backend**:added input validation and sanitization in the back-end to ensure that any input from users is checked before being processed.
4. **Modal for Adding Products**: created a modal that interacts with the JavaScript function to asynchronously send data to the server, add the product, and update the product list dynamically without page reloads.
5. **AJAX GET Request**: modified the main page to retrieve the latest product data using an AJAX GET request and displayed the updated list on the page.



Created by Sugonamu (Will KKI)