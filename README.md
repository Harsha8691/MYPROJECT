#Bank Application Programming Interface

An API service powered by Django offers a list of banks together with information about each branch. The bank and branch information may be easily retrieved thanks to the RESTful nature of the API.


## Features

- Obtain a list of banks and their branch locations.
- Obtain information about a certain branch.

## Requirements

- Django 3.2+ - Python 3.9+
- Django REST Framework - dj-database-url 

## Installation

1. Make a clone of the repository using the following commands: ``{bash git clone https://github.com/yourusername/bank-api.git cd bank-api {{{

2. Establish a virtual environment and activate it using the following commands: ```bash python -m venv venv source venv/bin/activate # On Windows, use `venv\Scripts\activate} {}

3. Install the necessary packages using the following command: pip install -r requirements.txt

4. Create the database using the following commands: python manage.py migrate

5. Make a superuser (optional) to gain access to the Django administration panel:
    python manage.py createsuperuser

6. Run the development server: python manage.py runserver

## API Endpoints

### Get List of Banks

- **URL:** `/api/banks/`
- **Method:** `GET`
- **Response:**
    json
    [
        {
            "name": "Bank A",
            "branches": [
                {
                    "name": "Branch A1",
                    "address": "Address A1"
                },
                {
                    "name": "Branch A2",
                    "address": "Address A2"
                }
            ]
        },
        {
            "name": "Bank B",
            "branches": [
                {
                    "name": "Branch B1",
                    "address": "Address B1"
                }
            ]
        }
    ]
  

### Get Branch Details

- **URL:** `/api/branches/<branch_name>/`
- **Method:** `GET`
- **Response:**
    json
    {
        "name": "Branch A1",
        "address": "Address A1"
    }


## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
   
