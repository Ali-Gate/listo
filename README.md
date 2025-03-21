# Listo! App To-Do List
Listo! APP

## Problem Statement: 
In today's fast-paced world, individuals and teams struggle to manage tasks efficiently. They often lose track of priorities, deadlines, and important activities, leading to decreased productivity and increased stress.
Purpose: 
The purpose of the Listo! App To-Do List is to provide users with an intuitive and organized platform for managing their tasks and activities. The app aims to enhance productivity, to promote timely completion of tasks, and stress reduction by offering features such as task deadlines, reminders, progress tracking and categorization.
Target Audience: 
The app is designed for busy professionals, students, and the general public who seek an intuitive and efficient task management solution.
For future iterations I aim to extend the features for project teams and  organizations.

## App description
### **User accounts**
### MVP
The user will be able to register, log in and log out for the first iteration 
### Future iterations
Users will be able to edit their account details and reset their passwords, as well as receiving a confirmation email after any account specific activity.
Users will be able to access a team account using their personal account with authorisation to securely access team privileges through invitation.
### **Tasks App usage**
### MVP
The user will be able to create, edit, set the stage of progression of their tasks and once completed they will be able to delete them for the first iteration.
The user will see a notification after every of the above actions including a confirmation prompt when deleting tasks.

### Future iterations
Users will be able to categorise tasks by topic, priority and deadline as well as access specific views.
Users will be able to move the tasks from to-do to done views.
Users will be able to access team to-do lists which team members will be able to access from their personal accounts 
Users will be able to use a calendar/planner which could also be accessed by teams.

## User Stories
### User for Registration and Login
- As a new user, I want to create an account, so that I can have a personalized experience and securely save my tasks. MUST

- As a user, I want to log in to my account, so that I can access my personalized tasks and settings. MUST

- As a user, I want to log out of my account, so that I can ensure the security of my information when I'm not using the app. MUST

- As a user, I want to reset my password, so that I can regain access to my account if I forget my password. COULD

- As a user, I want to update my account information, so that I can keep my profile details current. COULD

### User Stories for to-do list features

- As a user, I want to create a new task, so that I can keep track of things I need to do. MUST

- As a user, I want to view all my tasks, so that I can see what needs to be done. MUST

- As a user, I want to update a task, so that I can change its details if needed. MUST

- As a user, I want to delete a task, so that I can remove tasks that are no longer relevant. MUST

- As a user, I want to see a confirmation prompt before deleting a task, so that I don’t accidentally remove important tasks. MUST

- As a user, I want to mark a task as completed, so that I can visually track my progress. SHOULD

- As a user I want to filter the views of my tasks so that I can view tasks listed per category. COULD

### Admin Panel User Stories 
- As an admin, I want to view a list of all registered users, so that I can monitor user activity and manage accounts.

- As an admin, I want to view and manage all tasks in the system, so that I can ensure data integrity and address any issues.

- As an admin, I want to generate reports on user activity and task completion, so that I can analyze app usage and improve user experience.

- As an admin, I want to manage app settings and configurations, so that I can customize the app's behavior and features.



## Initial site folder structure


### **User Flow Diagram**

### **Entities/Models**

### Task model class (models.py)
The association between users and tasks ensures privacy and personalization
This connection allows for tailored task management features, such as personalized notifications. By maintaining this association, the app can provide a more organized and efficient task management experience, enhancing overall user satisfaction.

### Task Form model class (forms.py)
The association between tasks and task forms ensures structured data entry and consistency in task management.
This relationship helps maintain the integrity of task information and provides a user-friendly way to input and update task details.




### User  model class
The User entity represents individuals who register and interact with the Listo! app. 
Each user has unique attributes such as a username, email, and password, ensuring secure access and personalized task management. 
This association allows users to manage their tasks independently, maintaining privacy and organization, while also enabling features like personalized notifications and progress tracking.


## Views
- **Landing Page: base.html **
Base.html hol;ds the content of the other views
- Home
- Log in
- Register
- Logged in/Dashboard View:
- Add task
- Task list
- Admin View
- Users
- Tasks
- Categories
- Templates
- Index with header and footer
- To be retrieved and inserted using python
- Register 
- Log in 
- Dashboard
