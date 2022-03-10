## PROJECT DESCRIPION: ---

The brief for this project was to design and produce a web app of my choice. 
The requirements for the application included; CRUD (create, read update and delete) functionality, flask micro-framework, and had to store information into a MySQL database with a minimum of two tables sharing a one-to-many ralationship:

## APP DESIGN: ---

I have chosen to build a question-bank app, which allows users to write questions to the bank(create functionality).
View questions that have been posted by other users(read functionality).
Update the status of questions whether they have been answered or not (update functionality).
Delete questions(delete functionality).

The database for this program comprises of a Users table and a Questions table which associates with multiple questions to one user(One-To-Many relationship).
The ERD is displayed below: 

![ERD](figures/ERD.png)

The target for future modifications of the project will be to add an answers category that directly stores users answers for questions through an answers table.
With this modification, the ERD would look like so:

![ERD2](figures/ERD2.png)

## CI Pipeline: ---

-Trello: Project Tracking: 

In addition to the requirements, the project required implementation of some stages of a typical CI pipeline. These included project tracking, version control, development environment and a build server. I used Trello to track my project by creating a tracking board. Story points were assigned and MoSCoW prioritisation was used to review and complete functions as the project progressed. 

Example of a User story would be;
As a [User]
I want to be able to view all the questons everyone post
So that i can see other poeple contributions to the webpage

Here is the trello board at the start of the project along with a link to view the board. 


![TrelloBoard](figures/TrelloBoard.png)

Trello Board:  https://trello.com/b/5dGh4hhf/todo

-Venv: Python Virtual Environment:

A python3 virtual evironnment running ubuntu was used to develop the program. This was connected to through an SSH remote connection to write code in the environment. Flask is a python based frame-work that was also used in developing the program.

-Git: Version Control:

Git was used for the version control of the project, the repository was hosted on github. 
Version Control with git allows changes to be make and commited to the project with access of commit history to access earlier versions. Using github provided webhooks which sends http POST requests to a build server to automate building and testing on Jenkins.
Functions were created and updated via different branches then merged into dev then into main. Below is a network graph of how this flowed.

![Network Graph](figures/NetworkGraph.png)

-Jenkins: Build Server:

Jenkins was used as a build server, this provided automation of building and testing. The automation was achieved through setting up a freestyle project which executes the test.sh script when it recieves a webhook from github when a commit is pushed from the main branch. 

The full pipeline used in this project is

 Trello <---> Python <---> Git <---> Jenkins 

## RISK ASSESSMENT: ---

Before and after building the app, a risk assessment was drawn up/updated to identify the risks that could occur during the evolution of the project and how to control these risks.
The risk assessment is displayed below with how the measures could be implemented in the app. 

![Risk Assessment](figures/RiskAssessment.png)

## TESTING: ---

Testing the application was an essential portion of the development process. 
Pytest was used for Unit testing the functions/functionality of the app. Unit tests were written to ensure the Create, Read, Update and Delete functions worked correctly.

These functions were tested because they were the core requirements of the program and it needed to be ensured that these functions work as intended before deploying the live application.

Tests were written in the file called test_app.pywhich was within a test folder and a test was written for each of the different functions to ensure each aspect was fit for purpose. 

When writing the test file, this started with creating a TestBase class thats connects the environment to a new test database
- This is so that our tests do not affect the same database connected to the project that already exists with data.

A setUp and tearDown function was made to create a test user that would be tested whether it creates the user correctly and then to tear down the data that was created after we are done with the tests.
- Creating users is a functionality of our app so we would want to ensure that we can connect to our database and also ensure that users can be successfully created and stored within that database.

We then go on to test the GET requests of each page to ensure that the correct data is displayed onto the page with no errors.

Testing the POST requests on relevant pages followed testing the GET requests, this was to ensure that no errors occured when trying to store data. These tests also  ensured that relevant pages were redirected to a different page upon submission if required it.

- All the tests were successful and each test contributed to a percentage of the overall test coverage.

Tests were automated through Jenkins using webhooks.
A Coverage report shows what percentage of statements were included in the tests, this was outputted as HTML files produced on Jenkins.
Below is a visualisation of the coverage report.

![CoverageReport](figures/CoverageReport.png)

Another form of testing that could be used is Intergration testing. This would be used to also test the the functions of the program in a fake live environment. This form of testing would be able to simulate keyboard input and mouse clicks to ensure these elements of the program work as intended. 

Intergration test would be written for all the form fields within the app to test their functionality as we would need to test whether our components work together when intergrated together.

We have already partially used integration testing to ensure our app communicates with our database and that it connects by creating new entries, updating our entries and deleting our entries etc. 

With integration testing, we can simulate a user using our app/interface we provide to check it integrates properly with our backend.

The steps to Integration test the application using Selenuim would go as followed:

- Download Selenium on our venv
- Download Chromium Browser
- scp ~/ install chromium.sh travz@34.105.200.77:/home/travz/qa-project
- Install the required drivers
- Create a newfile and call it test_int.py
- We would then need to import some modules as described below.
- from flask_testing import LiveServerTestCase
- from selenuim import webdriver
- from urllib.request import urlopen
- from flask import url_for
- Also we would import the app and database from the application folder
- Our forms and models would also need to be imported into this file
- We would then need to;
- Create a TestBase class
- Create a setUp and tearDown function
- We would then create a class that would test given sample data that would be inputted into the fields 
- This would be followed by a method to define our submit function pulls data from wherever it is
- This would be done by opening up the inspect element and locating the desired input field and copying the full Xpath to place inside our function and within that function we would use the 'send_keys' method to simulate typing something in
-We would the do this process for all of our form fields 

These would is the steps that would be taken to integration test our forms/app

## The APP: ---

When navigating the app, the user is presented with the Homepage which gives a breif description on how the app works.

![HomePage](figures/homepage.png)

The navbar provides links which allow users to add questions, view questions, register a new user and view all the registered users.

![NavBar](figures/navbar.png)

Before adding a new question, the user would likely want to create a user for themselves first using the register page.
this page will allow the user to create a username and password for their user.

![RegisterPage](figures/registerpage.png)

However if a user does not want to create a custom user, the first default user created in the program is an 'Anonymous' named account that allows users to ask questions with the username 'anonymous'. However, they would still have to use their own email when creating a question to get a response.
- Users can also view all the current created users to know the total amount of users of the application.

![UsersPage](figures/userspage.png)

Users can post any questions they like using the ask page, this requires users to input data in all the fields. Some fields have data validation meaning those specific fields can not be left empty or an error message will be thrown prompting the user to fill in that specific field for the post to be created, this includes the email field as currently, viewers would have to contact the creator of any post via email address to answer a question until future modifications of the porgram allows users to directly answer question on the same page. 

![AskPage](figures/askpage.png)

Users can view all the posts that have been created on the questions page and have the ability to delete any post which removes the question from the database.
Users also has the abiliy to update any post which changes the state of the question as to whether the question has been answered or not.

![QuestionPage](figures/questionspage.png)

## UPDATES: ---

- Change colour scheme 
- Categorise questions

## ISSUES: ---

- Any user is able to update the status of any question whether they asked the question or not.
- Any user is able to delete any question whether they asked the question or not.

## FUTURE WORK: ---

- In future sprints, i would like to add a feature that allows users to answer questions directly under each post rather than only having the option to mark if a question has been answered through a true or false button, as it currently stands, questions can only be answered through the email address contact information the asker leaves on the page. The program was only desgined this way to meet requirements but has room the upgrade and scale all functions in the future. 
- I would also like to add a chat page where users can chat amongst each other in one big group chat.
- Lastly I would like to update the register/user page to give more security and validation upon creating user accounts.
- Furthermore, i would like to add user profile where users have have their own profile dedicated to them with all the questions they have asked and answered along with a points system for their amount of contribution.

## SUMMARY: ---

Checklist Breakdown:

- Good evolution of designs which are evident as the project progressed
- In depth READNME that explores the application to a high level
- Fully functional in all relevant areas, (imporvements can  be made to increase practicality (specifically thorugh the update function and answering questions)
- All tools and workflows have been discussed in documentation and are implemented successfully throughout the project at a high level 
- All areas of the software have been tested through pypest(99% coverage for functionality with all tests passing)(Refer to coverage report)
- Analysis as to what was tested and why (Create, Read, Update , Delete)
- Jenkins server was successfully installed and built software with a test.sh config file to make build jobs portable between servers
- Instructions on how to run integration tests was included
- A formal Risk assessment process was followed and updated displaying the Hazrards, Risks, Impact Level, Responsibility, Response, Control Measure and Likelyhood of occurance, this is followed by a key to show what the different colours mean for the Impact Level and Likelyhood column.

