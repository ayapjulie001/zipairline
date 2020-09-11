# zipairline
ZipHR Assessment 


Note: virtual env not pushed to git. 

Follow instruction as below or use virtual env that is already installed to your local machine.

1. install below libraries for virtual env in CMD 
  virtualenv==20.0.7
  virtualenvwrapper-win==1.2.6
2. once installed, run below commands in CMD
  mkvirtualenv <your choice of virtual env name>
2.a. to manually activate the virtual env, run below commands in CMD
  workon <your virtual env name created>
3. install requirements.txt using commands below, make sure you have pip and python3 installed and working venv is activated
  pip install -r requirements.txt
4. run below commands to migrate databse on sqlite3
  python manage.py migrate
5. run serverlet
  python manage.py runserver
