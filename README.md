# Chat-Application

1. Download and Install Python 3.6
2. Install virtualenv 
  1. on Ubuntu: $ sudo apt install python-virtualenv
  2. on Windows: >pip install virtualenv
3. Create a virtual environment
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
