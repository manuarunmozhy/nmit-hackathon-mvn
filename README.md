# Dayflow - Human Resource Management System

Dayflow is a simple Human Resource Management System developed as part of the NMIT Hackathon.

The project provides separate Employee and HR/Admin interfaces for managing common HR activities.

## Features

### Employee
- Employee login
- Employee dashboard
- View employee profile
- Check-in and check-out attendance
- View attendance status
- Apply for leave
- View leave request status
- View payroll information

### HR / Admin
- Admin login
- Admin dashboard
- View employee leave requests
- Approve leave requests
- Reject leave requests

## Functional Workflows

### Attendance
Employees can check in and check out through the attendance page. The attendance status is updated by the Flask backend.

### Leave Management
Employees can submit leave requests with:
- Leave type
- Start date
- End date
- Remarks

HR/Admin users can view submitted requests and approve or reject them. The updated status is then visible to the employee.

## Technologies Used

- Python
- Flask
- HTML
- Git
- GitHub
- Visual Studio Code

## Project Structure

    nmit-hackathon-mvn/
    |
    |-- app.py
    |-- requirements.txt
    |-- templates/
    |   |-- login.html
    |   |-- employee_dashboard.html
    |   |-- admin_dashboard.html
    |   |-- profile.html
    |   |-- attendance.html
    |   |-- leave.html
    |   |-- leave_approvals.html
    |   |-- payroll.html
    |
    |-- README.md

## How to Run

1. Clone the repository.

2. Create and activate a Python virtual environment.

3. Install dependencies:

       pip install -r requirements.txt

4. Run the application:

       py app.py

5. Open in the browser:

       http://127.0.0.1:5000

## Current Prototype Limitations

- Authentication is currently role-based for demonstration purposes.
- Employee data is currently sample data.
- Attendance and leave information are stored temporarily in memory and reset when the server restarts.
- A persistent database can be integrated in a future version.

## Future Enhancements

- SQLite/MySQL database integration
- Secure authentication and password hashing
- Multiple employee accounts
- Employee management for HR
- Persistent attendance records
- Payroll management
- Reports and analytics
- Email and notification system

## Hackathon Prototype

This project focuses on demonstrating the core workflow of an HRMS, particularly employee/admin role separation, attendance management, leave requests, and HR approval workflows.