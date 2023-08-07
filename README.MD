#Steps to run this sample project

**1. Create python virtual environment in any folder:**
'''
python3.9 -m venv my_env , run this command in terminal
then --> source/my_env/bin/activate (to activate your environment)
'''

**2. Clone the following repo in that folder where environment is created:**
'''
git clone https://github.com/Ashu2ei/sample_project.git
'''

**3. Switch to sample_project and run following command:**
'''
pip install -r requirements.txt
'''

**3. Then Switch to sample_project/sample_project(contains manage.py) and run following commands:**
'''
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
'''

**4. Open your postman and pass these values to url and data to body:**
'''
http://127.0.0.1:8000/myapi/simple-post/

{
    "value_of_x":10,
    "value_of_y":20 
}
'''

**4. Output will be:**
'''
{
    "message": "Data received successfully.",
    "input_data": {
        "value_of_x": 10,
        "value_of_y": 20
    },
    "output_is": 30
}
'''