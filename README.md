# Cropper-app

## Author

- Created by **Collins Kanyiri** on 10/10/2021

### Description

This is a Django web application that is for displaying my photos taken from different locations and then put into different categories for viewing and searching.

### Prerequisites

Before you begin, ensure you have met the following requirements:

You have installed the latest version of python 3.8
You have a Linux machine

### Live site

*view site from the link below*
<https://imagecroppercollo.herokuapp.com/>

## Technologies Used

- Django
- Python-3.8.12
- Bootstrap
- Heroku

## Interactive Input

View photos from different categories.

View photos from different Locations.

Search photos by categories

## Development Installation

To get the code..

1. Cloning the repository:

  on the terminal
  $ git clone <https://github.com/Collinskanyiri/ImageCropper.git>

2. Creating virtual environment:

  $ pip install --user pipenv

3. Activate virtual environment:

  $ pipenv shell

4. Move into the folder and install requirements

  $ pip install -r requirements.txt

5. Run migrations

  $ python manage.py makemigrations Cropper
  $ python manage.py sqlmigrate 0001
  $ python manage.py migrate

6. Running the application

  $ python manage.py runserver

7. Testing the application

  $ python manage.py test photos

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact

If you want to contact me you can reach me at [collinskanyiri@gmail.com]()

## License

This project uses the following license:MIT License

- Copyright (c) 2021 **Collins Kanyiri**
