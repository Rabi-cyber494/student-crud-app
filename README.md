Open PowerShell / Terminal
Navigate to your project folder where manage.py is located

 Set Execution Policy (Only for PowerShell)
 Run this command every time you open a new terminal:
 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
 
  Activate Virtual Environment:
  .\CRUDenv\Scripts\activate
  Your terminal will show (CRUDenv) indicating the environment is active
  
  Navigate to the Project Folder (where manage.py exists):
  cd CRUD
  
  Run Migrations (to set up the database):
  python manage.py makemigrations
  python manage.py migrate

Start the Development Server
python manage.py runserver
Done!
Open your browser and go to:
http://127.0.0.1:8000
to view and test the application.

📌 Features:
Create new student records
Read / View all students
Update existing student data
Delete student entries
GitHub Repository:
[https://github.com/Rabi-cyber494/student-crud-app
]
