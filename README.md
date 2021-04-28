# APlusTopper Notification System

## Features :information_source: 

:heavy_check_mark: Login, Logout, Password Reset <br>

:heavy_check_mark: Can send push notification to multiple users on multiple websites. <br>

:heavy_check_mark: Manage Websites (Add websites, Delete websites) <br>

:heavy_check_mark: Push notification queue stats. <br>

:heavy_check_mark: Dashboard for some analytics. <br>
<br><br>

### Set this project locally :computer:

1. Go to the [project repo](https://github.com/) and clone it or download the zip file.<br>

2. Go inside the project root directory.
  
3. Create a python3 virtual environment:

    ```bash
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    $ virtualenv venv
    ```

4. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```bash
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

5. Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```

6. Creating local settings:
Create a `local_settings.py` file in the same directory where your `settings.py` resides.

    Copy this code in your `local_settings.py` file -
    ```
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    ```
    
7. Creating `.env` file:
Create a `.env` file in the same directory where your `manage.py` resides.

    Copy this text in your `.env` file -
    ```
    SECRET_KEY = 'secretkey'
    ```

8. Run the `migrate` command:

    ```bash
    $ python manage.py migrate
    ```

9. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```

# Thanks