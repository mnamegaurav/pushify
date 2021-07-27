# Pushify Notification System

## Features :information_source: 

:heavy_check_mark: Login, Logout, Password Reset <br>

:heavy_check_mark: Can send push notification to multiple users on multiple websites. <br>

:heavy_check_mark: Manage Websites (Add websites, Delete websites) <br>

:heavy_check_mark: Push notification queue stats. <br>

:heavy_check_mark: Dashboard for some analytics. <br>

### Set this project locally :computer:

1. Clone this repository or download the zip file.<br>

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

    - On Linux or Mac or any Unix based system-
    
        ```bash
        $ source venv/bin/activate
        ```
    
    - On Windows based OS-
        ```
        > venv\Scripts\activate
        ```

5. Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```

6. Creating local settings:
    
    There is a file in the notification directory where your `settings.py` resides, named `local_settings.example.py`.

    Just rename this file to `local_settings.py`.
    
7. Creating `.env` file:
    
    There is a file in the base directory where your `manage.py` resides, named `.env.example`.

    Just rename this file to `.env`.

8. Start RabbitMQ server:

    - On Linux or Mac or any Unix based system:
    
        Install `rabbitmq-server` package in your local system, start the background service by running this command on Linux.

        ```bash
        $ sudo systemctl start rabbitmq
        ```

    - On Windows based OS:

        Please follow this link for setting up the rabbitmq server in your local system.
        https://www.rabbitmq.com/install-windows.html

9. Run these commands command before starting the development server:

    ```bash
    $ python manage.py migrate
    $ python manage.py createcachetable
    $ python manage.py collectstatic
    ```

10. Run celery server with this command:

    ```bash
    $ celery -A notification worker -l info
    ```

11. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```

# Thanks
