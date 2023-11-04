# User Management System 
### Objective: Create a simple user management system backend using Firebase. The system will provide APIs to perform user registrations, user logins, and the ability to retrieve, update, and delete user profiles.
___
### Setting up  
Create a Firebase account and start a new project setup it and create api_token from the profile section.

Clone the repository:
```
git clone https://github.com/Shankar-1212/UserManagementSystem.
```
Install the required dependencies:
```
cd UserManagentSystem
pip install -r requirements.txt
```
Set up your Django environment variables, including the Firebase API key.
Run the application:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Endpoints list :
* /register/
* /login/
* /profile/
* /update/
* /delete/
___
```POST``` ``` http://localhost/register/```
### Request Body
{
    "email": "user@example.com",
    "password": "userpassword",
    "full_name": "User Full Name",
    "username": "username123"
}
### Request Response
{
    "message": "User registered successfully"
}
___
```POST``` ``` http://127.0.0.1:8000/login/```
### Request Body
{
    "email": "user1@example.com",
    "password": "userpassword"
}
### Request Response
{
    "idtoken": " "
}
___
```POST``` ``` http://127.0.0.1:8000/profile/```
### Request Body
{
    "email": "shankar1@gmail.com"
}
### Request Response
{
    "email": "shankar1@gmail.com",
    "full_name": "Shankaar",
    "username": "shank"
}
___
```PUT``` ``` http://127.0.0.1:8000/update/```
### Request Body
{
    "email": "shankar1@gmail.com",
    "full_name": "Shankar",
    "username": "shank"
}
### Request Response
{
    "message": "User profile updated successfully"
}
___
```DELETE``` ``` http://127.0.0.1:8000/update/```
### Request Body
{
    "email": "shankar1@gmail.com"
}
### Request Response
{
    "message": "User account deleted successfully"
}
__________________


