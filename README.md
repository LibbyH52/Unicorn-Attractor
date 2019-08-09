[![Build Status](https://travis-ci.org/LibbyH52/Unicorn-Attractor.svg?branch=master)](https://travis-ci.org/LibbyH52/Unicorn-Attractor)

# Issue Tracker
The primary goal of this milestone was to create a Django project containing several reusable applications. I chose to go with the brief and develop an Issue Tracker that allows registered users to create bug reports, comment on other bugs and submit feature requests. It is also possible for the a user to upvote a particular feature by paying a fee of €10. In return for this payment fifty percent of the company time will be spent working on developing the feature with the most upvotes.    

## UX
#### User Stories
* As a user, I would like to be able to create an account, so that I can:
* create a user profile.
* file a bug report.
* comment on bug reports.
* view available features.
* see what features have been requested by others.
* request features.
* vote for features that I would like to see being developed.
* keep track of my feature requests and bug reports.

#### Wireframes
My wireframes were developed using Balsamiq and can be found [here](wireframes/)

   
## Features
#### Existing Features

##### Navbar
An unauthorised user will see the following links:
* UnicornAttractor (Navbar brand that links to the HomePage)
* Register
* Login

A logged in user will see the following links:
* UnicornAttractor (Navbar brand that links to the HomePage)
* Bugs
* Features
* Shopping Cart
* Profile
* Logout

* User Registration
To create an account a user must enter an email address, username and password. This functionality was implemented using Django's authentication system. Once they have created an account the user is redirected to the login page. 

* Login
A registered user can login using their username and password. Once a user has successsfully logged in they will be redirected to a list of feature requests.

* Logout
A user can log out at any time by clicking on the Logout link in the navbar. Once logged out hte user will be redirected to the HomePage.

* User Profile
A logged in user will be able to visit their profile page by clicking on the relevant link in the navbar. A user's profile page contains displays their email address, sign-up date, last log in date as well as details of any bug reports they've filed and feature requests they've made.

* Reset Password
A user who has forgotten their password can request to reset it by clicking on the 'forgot password' link below the log in form. They will be then redirected to a form where they should enter the email address that was used when creating their account. An email will be sent to that email address with a with instructions on creating a new password. 

Clicking on the link in the email will take the user to a form where they can enter a new password. The user will then be redirected back to the login page and can sign in using their username and bew password. 

* View Bugs
If a user clicks on the Bugs link in the navbar they will be taken to a page containing a list of all the bugs that have been found. The colour-coded badges (ToDo, Doing and Done) that appear beside the bug title provide the user with visual cues regarding the fix status of a bug. 

* Add a Bug
Clicking on the Report a Bug button allows a user to send details of any issues or difficulties they've had while accessing the site. When a user clicks on this button they will be taken to a page containing a form where they enter a description of this issue and submit their bug report.

* View a single bug
The title of each bug is a clickable link which takes the user to a page containing details of the bug report. It is also possible to view any comments that the other users have posted regarding this bug.

* Edit Bug
It is possible to edit a bug by clicking on the pen icon beside the bug description. This feature is only available to the author of the bug report. 

* Comment on a bug
All logged in users are able to post comments on a bug report. This can be done by clicking on the Add Comment button underneath the comments section. The author of a comment also has the ability to edit or delete any comment that they have posted.  

* Features
A user can also view a list of features that other users have requested. The user can also see the number of votes that have been given to each feature and what stage of development that particular feature is at. This cna be seen in the top left hand corner of the feature request.

* Request a Feature
It is also possible for a user to request a particular feature. This can be done by clicking on the Request Feature button at the top of the list of features. When this button is clicked the user is taken to a form where they can fill in details of the feature that they would like to see added to the site. The feature is then added to the top of the list on the Features page. It is free to request a feature.

* Vote for a Feature
To vote for a feature a user should click on the thumbs up icon to the right of the feature title. When this icon is clicked a modal pops up informing the user that there is a fee of €10 per vote. If the user agrees to this and clicks on the Vote button then that particular feature is added to their cart. Each feature can only be added once but a user can add as many features as they wish.

* View Cart
Clicking on the cart icon in the navbar will allow a user to view their cart. It is here that the user will see a list of the features they have voted for. It is possible to adjust the quantity of votes that a user wishes to purchse for each feature. A maximum of ten votes can be purchased per feature. If the user decreases the quantity to zero that item is removed from the cart.
When a user is satisfied with the number of items in their cart they can click on the Pay Now button underneath their shopping cart. The user is then taken to a checkout page.

* Checkout
 On the checkout page the user should fill in a form containing their full-name, credit card number (Stripe recommends a test number of 4242 4242 4242 4242, do not enter any real credit card information), an expiry year and month, a CVV number (three random digits) and country of residence. 
 The user's shopping cart is also visible here. Upon completion the user should click on the Pay Now button where they will be re directed back to the Features page where they can see the increase in upvotes

## Technologies Used
* HTML
* CSS
* Bootstrap
* Font Awesome
* JavaScript/ jQuery
* Django
* Python
* Stripe
* Whitenoise
* Postgres/ Sqlite3

## Deployment
This project was created using the Visual Studio Code text editor. Version control was carried out entirely using git.  
Before deploying to Heroku I created a requirements.txt file to list all the dependencies used in this project. 
The following were set as config variables in Heroku, and as environment variables for local coding:
DATABASE_URL
SECRET_KEY

Procfile
Add Heroku to ALLOWED_HOSTS

## Testing
Checked views.py file using PEP8 online code checker

## Credits

#### Content
navbar right https://stackoverflow.com/questions/53339351/how-to-create-navigation-bar-with-login-sign-up-button-in-bootstrap-4
First answer by Razvan Zamfir

paginator code from documentation


#### Media
https://pixabay.com/illustrations/singapore-web-network-ball-2064905/

#### Acknowledgements
Thanks to my coursemate John Longgately for providing this line of code 'dist: xenial' to solve the issue with Travis integration.


