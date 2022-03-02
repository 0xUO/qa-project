PROJECT DESCRIPION --

A question and answer webpage where users can ask questions/problems to the community and others can answer the asked questons.

PROJECT PLAN ---

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