# Chat-Application

1. Download and Install Python 3.6
2. Install virtualenv
  -on Ubuntu: $ sudo apt install python-virtualenv
  -on Windows Powershell $ pip install virtualenv
Create a virtual environment
on Ubuntu: $ virtualenv env -p python3.6
on Windows: $ virtualenv env
Activate the env:
on Ubuntu: $ source env/bin/activate
on Windows: $ ./env/scripts/activate
Install the requirements: $ pip install -r requirements.txt
Change directory to FusionIIIT $ cd FusionIIIT
Make migrations $ python manage.py makemigrations
Migrate the changes to the database $ python manage.py migrate
Run the server $ python manage.py runserver
