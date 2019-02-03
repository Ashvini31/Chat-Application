# Chat-Application

1.  Download and Install Python 3.6
2.  Install virtualenv 
3.  Create a virtual environment and activate it.
4.  Make migrations $ python manage.py makemigrations
5.  Migrate the changes to the database $ python manage.py migrate
6.  Run the server $ python manage.py runserver
7.  Copy the port address to browser and write /admin after it to open the database.
8.  Write /login after port address to login.
9.  Write /userreg after port address to register as user.
10. Write /adminreg after port address to register as new admin.
11. On logging in with admin id, you will be directed to adminhome.
12. On logging in with user id, you will be directed to userhome.
13. Logout will redirect to login page.
