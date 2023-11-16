# Hotel Booking

[![Python Version](https://img.shields.io/badge/python-3.9-brightblue.svg)](https://python.org)
![Django version](https://img.shields.io/badge/Django-4.2-7?colorB=blue)

A simple django project for booking room in hotel.
`Room` and `Booking` tables and their relevant serializers and APIs to show available rooms in a specific time range.

<br>

# Table of contents

- [Installation](#Installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Run Project](#run-project)
- [APIs](#apis)
- [Contact](#contact)

<br>

# Installation

## Prerequisites

Only python and its packages are needed to run this project.

## Clone the Repository

```bash
git clone https://github.com/masoudgheisari92/hotel-booking.git
```

## Run Project

1. Create virtual environment and install required packages:

   ```bash
   # create virtual environment
   python -m venv venv
   # activate virtual environment
   venv/Scripts/activate
   pip install -r requirements.txt
   ```

2. Run the migrations

   ```bash
   cd booking_project
   python manage.py migrate
   ```

3. Create superuser (admin)

   ```bash
   python manage.py createsuperuser
   ```

4. Run server
   ```bash
   python manage.py runserver
   cd ..
   ```

# APIs

APIs can be tested with swagger throught `docs` endpoint:

```bash
127.0.0.1:8000/docs/
```

# Contact

### Masoud Gheisari

- linkedin: [https://linkedin.com/in/masoud-gheisari](https://linkedin.com/in/masoud-gheisari)
- email: masoud.gh20@gmail.com
