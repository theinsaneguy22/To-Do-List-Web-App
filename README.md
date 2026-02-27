# Daily-To-Do-List-Web-App
A full-stack web application built using Django that allows users to manage their daily tasks efficiently. The application supports user authentication, date-wise task management, and complete CRUD operations in a clean, modern UI.
This project demonstrates backend development, authentication handling, database relationships, and front-end UI design using Django.

# Project Overview
This project is a personal productivity tool where:
User Authentication -> Date-based Task Creation -> CRUD Operations -> Organized Daily Planner Dashboard

# It focuses on:
- Secure login & registration
- User-specific task management
- Date-wise task organization
- Clean and responsive UI design

# Technologies Used
1. Python
2. Django
3. SQLite (Default Django Database)
4. HTML
5. CSS
6. Django Authentication System

# Project Workflow
- User registers an account
- User logs in securely
- Dashboard displays today's tasks
- User can:
  - Add tasks
  - Update tasks
  - Delete tasks
  - Mark tasks as completed
- Tasks are stored date-wise
- Each user sees only their own tasks

# Project Features
1. User Authentication
- Secure Login & Registration system
- Password validation using Django’s built-in authentication
- Logout functionality
- User-specific data isolation

2. Date-wise Task Management
- Tasks are stored with a specific date
- Dashboard displays tasks for selected day
- Organized daily planning system

3. CRUD Operations
- Create new tasks
- Read/view tasks
- Update task details
- Delete tasks
- Mark tasks as completed

4. User-Specific Data Access
- Each user can only view and manage their own tasks
- Tasks linked to authenticated user
- Protected routes using @login_required

5. Modern UI Design
- Custom login & registration pages
- Styled navigation bar with username & logout
- Clean dashboard layout
- Responsive and beginner-friendly interface

# Database Structure
- User Model (Django built-in)
- Task Model
  - Title
  - Description
  - Date
  - ForeignKey to User

# Concepts Demonstrated

- Django Models & ORM
- User Authentication System
- Template Rendering
- Form Handling
- URL Routing & Namespaces
- CRUD Implementation
- Date-based Filtering
- User-based Data Filtering

