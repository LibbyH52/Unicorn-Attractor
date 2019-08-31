[![Build Status](https://travis-ci.org/LibbyH52/Unicorn-Attractor.svg?branch=master)](https://travis-ci.org/LibbyH52/Unicorn-Attractor)

# Issue Tracker
The primary goal of this milestone was to create a Django project containing several reusable applications. I chose to go with the brief and develop an Issue Tracker that allows registered users to create bug reports, comment on other bugs and submit feature requests. A user can upvote a feature by paying a fee of €10. In return for this payment fifty percent of the company time will be spent working on developing the feature with the highest number of votes.    

## UX

#### User Stories
* As a user, I would like to be able to create an account, so that I can create a user profile.
* As a user, I would like to be able to create an account, so that I can file a bug report.
* As a user, I would like to be able to create an account, so that I can comment on bug reports and feature requests.
* As a user, I would like to be able to create an account, so that I can view available features.
* As a user, I would like to be able to create an account, so that I can see what features have been requested by others.
* As a user, I would like to be able to create an account, so that I can request features.
* As a user, I would like to be able to create an account, so that I can vote for features that I would like to see being developed.
* As a user, I would like to be able to create an account, so that I can keep track of my feature requests and bug reports.

#### Wireframes
My wireframes were developed using Balsamiq and can be found here:
* [Bugs Page](wireframes/allBugs.png)
* [Single Bug Page](wireframes/bugsingle.png)
* [Features Page](wireframes/features.png)
* [Add Bug or Feature](wireframes/reportBugRequestFeature.png)
* [Add Comment](wireframes/comment.png)
* [User Profile](wireframes/profile.png)
* [Shopping Cart](wireframes/cart.png)
* [Checkout](wireframes/checkout.png)

   
## Features

#### Existing Features

##### Navbar
An unauthorised user will see the following links:
* UnicornAttractor (Navbar brand that links to the Homepage)
* Statistics (page containing graphs)
* Register
* Login

A logged in user will see the following links:
* UnicornAttractor
* Statistics
* Bugs
* Features
* Shopping Cart
* Profile
* Logout

* User Registration
To create an account a user must enter an email address, username and password. This functionality was implemented using Django's authentication system. Once they have created an account the user is redirected to the login page. 

* Login
A registered user can login using their username and password. Once a user has successfully logged in, they will be redirected to their profile page.

* Logout
A user can log out at any time by clicking on the Logout link on the right-hand side of the navbar. Once logged out the user will be redirected to the Homepage.

* User Profile
A logged in user will be able to visit their profile page by clicking on the relevant link in the navbar. A user's profile page displays their email address, sign-up date, last log in date, as well as details of any bug reports they've filed and feature requests they've made.

* Reset Password
A user who has forgotten their password can request to have it reset by clicking on the 'forgot password' link below the log in form. They will be then redirected to a form where they should enter the email address that was used when creating their account. An email will be sent to that email address with instructions on how to create a new password. 

* View Bugs
If a user clicks on the 'Bugs' link in the navbar they will be taken to a page containing a list of all the bugs that have been found. The colour-coded badges (ToDo, Doing and Done) that appear beside the bug title provide the user with visual cues regarding the fix status of a bug.

* Add a Bug
Clicking on the 'Report a Bug' button allows a user to send details of any issues or difficulties they've had while accessing the site. When a user clicks on this button, they will be taken to a page containing a form where they can enter a description of the issue and submit their bug report.

* View a single bug
The title of each bug is a clickable link that takes the user to a page containing details of the bug report. It is also possible to view any comments that other users have posted regarding this bug.

* Edit/ Delete Bug
It is possible to edit a bug by clicking on the relevant icons (pen and trash can) beside the bug description. These features are only available to the author of the bug report. Deleting a bug will also delete any associated comments.

* Comment on a Bug/ Feature
All logged in users can post comments on a bug report or feature request. This can be done by clicking on the 'Add Comment' button underneath the comments section. The author of a comment can also edit or delete any comment that they have posted.  

* Features
A user can view a list of features that other users have requested. The colour-coded badges (ToDo, Doing and Done) that appear beside the feature title provide the user with visual cues as to what stage of development the feature is at. The thumbs-up icon to the right of the feature title tells a user how many votes that feature has received.

* Request a Feature
A user can submit a feature request by clicking on the 'Request Feature' button on the top right of the list of features. When this button is clicked the user is taken to a form where they fill in details of the feature that they would like to see added to the site. The request is then added to the top of the list on the Features page. It is free to request a feature.

* View Feature Details
This can be done by clicking on the name of any feature. A user is then taken to a page where they can view more details about a feature and upvote any feature that has not yet been developed.

* Vote for a Feature
To vote for a feature a user should click on the thumbs-up icon to the right of the feature title. When this icon is clicked a pop-up modal appears informing the user that there is a fee of €10 per vote. If the user agrees to this and clicks on the 'Vote' button, then that feature is added to their shopping cart. Each feature can only be added once, but a user can add as many features as they wish.

* Edit / Delete Feature
A user can edit or delete a Feature by clicking on the relevant icons beside the description text. A feature can only be deleted while it is in the 'to do' phase of development. Deleting a feature will also remove any associated comments. 

* View Cart
Clicking on the cart icon in the navbar will allow a user to view their cart. It is here that the user will see a list of the features they have voted for. It is possible to adjust the quantity of votes that a user wishes to purchase for each feature. A maximum of ten votes can be purchased per feature. If the user decreases the quantity to zero that item is removed from the cart.
When a user is satisfied with the number of items in their cart they can click on the 'Checkout Now' button underneath their shopping cart. The user is then taken to a checkout page.

* Checkout
 On the checkout page the user should fill in a form detailing their full-name, credit card number (Stripe recommends a test number of 4242 4242 4242 4242, do not enter any real credit card information), an expiry month and year, a CVV number (three random digits) and country of residence. 
 The user's shopping cart is also visible here. Upon completion the user should click on the Pay Now button where they will be re directed back to the Features page and can view the increase in up votes. 

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
This project was created using Visual Studio Code text editor. Version control was carried out entirely using git. The GitHub repository can be found [here:] 
(https://github.com/LibbyH52/Unicorn-Attractor)

The project was hosted on Heroku. The running application is available [here:]
(https://unicorn-attractor-milestone-4.herokuapp.com/)

#### To deploy to Heroku I took the following steps:
* Created a requirements.txt file to hold a list of the dependencies needed to run the project
* Created an env.py file, and added it to .gitignore, to store any environment variables that I didn't want pushed to GitHub
* Created a new GitHub repository
* Created a Heroku app with a unique name
* Connected my GitHub repository to my Heroku app and enabled automatic deploys
* Under the Deploy tab I scrolled down to add-ons and connected to the Postgres database
* Under the settings tab, I clicked on Reveal Config Vars and stored the relevant environment variables as cofig variables
* Ensured all existing migrations were pushed to the new Postgres database by running:
    python manage.py makemigrations
    python manage.py migrate
* Created a Procile at the top level of my project to tell Heroku what kind of app was being deployed
* Added the Heroku app to ALLOWED_HOSTS in settings.py file


#### Local Deployment
To deploy this could locally you should:
* Clone the [GitHub repository](https://github.com/LibbyH52/Unicorn-Attractor.git)
* Install Python on your machine (if it isn't already there)
* Create a folder to store the project
* Install a virtual environment
* Create a new virtual environment and activate it
* Install Django inside your new virtual environment
* Create a new Django project
    django-admin startproject projectname
* Install the dependencies listed in requirements.txt
    pip install -r requirements.txt
* Add each app to the list of INSTALLED_APPS in settings.py
* Run make migrations to create the database
    python manage.py makemigrations
    python manage.py migrate
* To run your new django project use the following command:
    python manage.py runserver


## Testing

* Views, models and forms were validated using the PEP8 checker, there were a couple of warnings regarding line length (pattern for credit card number and a form validation error for UserRegistrationForm), but the code would not function if those lines were split up.

* All templates were validated using a HTML validator. The only warnings were when the validator failed to recognise the Django template tags.

CSS was validated using the Jigsaw Validator:
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!">
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!">
    </a>
</p>

The site was tested for responsiveness using the DevTools and the following devices:

* iPhone6
* iPhone 6/7/8 plus
* iPhone X/XS
* Galaxy Note 9
* Galaxy S9/ S9+
* iPad
* iPad Mini
* iPad pro 10.5 inch
* Kindle Fire
* Nexus 10
* iPad Pro 12.5
* Laptop with MDPI
* Laptop with HiDpi
* Laptop with Touch
* 720p HD Television
* 1080p Full HD Television
* 4k Ultra HD Television

##### Registration
To test the registration functionality I created several accounts. I ensured that password validation worked correctly by typing mismatched passwords and attempting to sign up. I also tried to create two different users with the same username and/ or email address to see if this was allowed, it wasn't. 

##### Login
To test the login functionality I used the wrong username/ password combination to see if I could access an account. I also logged in using the correct credentials to make sure I was redirected to the user profile page.

##### Logout
I made sure the logout view redirected me to the home page and that I could only see the appropriate navbar links.

##### Add Bug/ Feature/ Comment
I added new bugs features and comments using several different accounts to ensure this functionality was working correctly, and the user was redirected back to the appropriate page where the relevant data would be displayed. I also made sure this functionality could not be accessed by unauthorised users through the url.

##### Edit Bug/ Feature/ Comment
I used the accounts I created to test the edit functionality. I made sure the pen icon was only visible to the appropriate user. I entered the url into the address bar to ensure that only the relevant user had access and all other users were redirected to a blank form with a message stating that they did not have permission to edit that bug/ feature/ comment. 

##### Delete Bug/ Feature/ Comment
I checked that the trash can was only visible to the appropriate user and that clicking on it rendered a modal to confirm delete. Upon confirming delete I checked to make sure that the data was longer visible on the page, I also clicked the 'Cancel' button to close the modal and take no further action. I entered the url into the address bar to ensure that only the relevant user had access and all other users received a message informing them that they did not have permission to delete the bug/ feature/ comment. 

##### Upvote Feature
I upvoted several features to make sure that the modal was rendered asking the user to confirm their purchase. I checked the relevant data was displayed regarding the price of an upvote. I made sure that confirming the purchase would take a user to their shopping cart where they could increase or decrease the number of votes. I also ensured that decreasing the number of votes to zero would remove the item from the cart.

##### Payment Form and Checkout
I confirmed that clicking on the checkout button would take me to a payment from asking for the following details: name, credit card number, expiry date and month and country. I filled out the form several times making sure that the relevant error messages were displayed and that the form could not be submitted with blank fields. I also checked that upon successful submission of the form I was redirected back to the 'Features' page.  


## Credits

#### Content
To create navbar links on the right I used the second answer from this [thread](https://stackoverflow.com/questions/53339351/how-to-create-navigation-bar-with-login-sign-up-button-in-bootstrap-4) on stackoverflow

The paginator came from the Django documentation and Corey Schafer's YouTube Django tutorials

Xavier from tutor support reminded me that to render comments to my Bugs and Features template I had to return them in my view

The code for toggling a modal using a font-awesome icon is from the first answer in this [thread]
(https://stackoverflow.com/questions/52777550/how-to-make-font-awesome-icon-clickable-to-open-a-modal-in-bootstrap-3)

The code for rending on modal on page load came from the first answer [here]
(https://stackoverflow.com/questions/47486339display-this-bootstrap-modal-on-page-load)

The code for removing bullets from inside modal I got from [here]
(https://github.com/twbs/bootstrap/issues/15875)

The pattern for the payment form credit card number came from [here]
(http://html5pattern.com/Cards)

#### Media
My background image came from [pixabay](https://pixabay.com/illustrations/singapore-web-network-ball-2064905/)

#### Acknowledgements
Thanks to my course mates on Slack who helped solve errors during development and for reviewing my almost finished project and providing constructive feedback.  
Thank you to my mentor Moosa Hassan for his help and support throughout development of the project.
