PROJECT DESCRIPION --

The breif for this porject was to design and produce a web app of my choice. 
The requirements for the application; included CRUD (create, read update and delete) functionality,
Flask micro-framework, and had to store inofrmation into a MySQL database with a minimum of two tables sharing a one-to-many ralationship:
The Structure is displayed below:

-Insert Picture Here

App Design ---

I have chosen to build a question-bank app, which allows users to write questions to the bank(create functionality).
View questions that have been posted by other users(read functionality).
Update the status of questions whether they have been answered or not (update functionality).
Delete questions(delete functionality).

The database for this program comprises of a Users table and a Questions table which assiciates with multiple questions to one user(One-To-Many relationship).
The ERD is displayed below:

-Insert ERD Here

The target for future modifications of the project will be an answers category that directly stores users answers for questions though an answers table.
With this modification, the ERD would look like so:

- Insert What New ERD owuld look like here

CI Pipeline ---



Trello Board:  https://trello.com/b/5dGh4hhf/todo

RISK ASSESSMENT --
---
1:
Description:
 - Application's virtual machine goes down
Evaluation:
 - Application goes offline
Likelihood:
 - Low
Impact Level:
 - High
Responsibility:
 - Google
Response:
 - Recreate infrastucture on another machine
Control Measures:
 - Use infrastructure as code to quickly recreate machine & store all code in VCS
---
 2:
Description:
 - Broken version deployed onto production
Evaluation:
 - Deployed service may have issues or missing requirements
Likelihood:
 - Medium
Impact Level:
 - High
Responsibility:
 - Developer
Response:
 - Revert production to most recent stable version
Control Measures:
 - Automate tests before any deployment & restrict access to production branch
---
 3:
Description:
 - website misued by rogue user 
Evaluation:
 - anyone can contribute to the website
Likelihood:
 - Medium
Impact Level:
 - Medium
Responsibility:
 - Developer
Response:
 - delete duplicates or inputs that are not questions
Control Measures:
 - make a login page that allows only registered users to ask questions 
---
 4:
Description:
 - users can ask the same question m
Evaluation:
 - what would happen if this scenario occurred?
Likelihood:
 - High/Medium/Low
Impact Level:
 - High/Medium/Low
Responsibility:
 - who's responsibility is it to mitigate this risk?
Response:
 - what would we do if the scenario occurred?
Control Measures:
 - what can we do to decrease the likelihood and/or impact?


 User Stories

 As a.. [User]

 I want.. [Feature]

 So that.. [Details]