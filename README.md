# vp-api-drf
# Prerequisite :
Python 3.8

# Steps to execute
1] Clone the project in your local machine

2] Create virtual environment with Python 3.8 and activate it

3] Install dependencies from requirements.txt
 
     $ pip install -r requirements.txt
4] Once all the libraries are installed successfully then run

     $ python manage.py makemigrations
5] Write changes into database

    $ python manage.py migrate
6] Load playlist.json data into database

    i] From virtual environment activated console go to vp-api-drf/VPDataAPI/scripts
    ii] Execute following command to parse json data and load into sqlite database. 
    If existing datat is there then it will overwrite exsting data
        $python json_data_parser.py
7] Execute Unit test case

    i] Go to vp-api-drf/VPDataAPI directory and execute following command
     to perform unit test 
        $python manage.py test
8] Execute project

    i] Go to vp-api-drf/VPDataAPI directory and execute following command to perform 
       $python manage.py runserver
9] Access api in browser:

      http://localhost:8000/api/schema/swagger-ui/