# Hotel Room Booking System

[![Python Version](https://img.shields.io/badge/python-3.9-brightblue.svg)](https://python.org)
![Django version](https://img.shields.io/badge/Django-4.2-7?colorB=blue)

## Description:

The Hotel Room Booking System is a web application designed to streamline the process of hotel room reservations and management. The system caters to both users and hotel staff, providing an easy-to-use interface for booking rooms, checking availability, and generating reports for staff members. Some initial data added for hotels and rooms.<br>

<br>

# Table of contents

- [Technologies Used](#Technologies-Used)
- [Installation](#Installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Run Project](#run-project)
- [APIs](#apis)
- [Limitations](#Limitations)
- [Contact](#contact)

<br>

# Technologies Used:

**Django Framework:** Backend development and handling business logic.<br>
**Django REST Framework:** Building APIs for communication between the frontend and backend.<br>
**Database:** Sqlite

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

Some more important APIs include:

```bash
127.0.0.1:8000/booking/
127.0.0.1:8000/booking/available-rooms/
127.0.0.1:8000/listing-owner/hotels/
127.0.0.1:8000/listing-owner/rooms/
127.0.0.1:8000/listing-owner/report/hotel/
```

<br>

# Limitations

- Authentication / Authorization is not in the scope of this project
- No localization is applied

<br>

# Contact

### Masoud Gheisari

- linkedin: [https://linkedin.com/in/masoud-gheisari](https://linkedin.com/in/masoud-gheisari)
- email: masoud.gh20@gmail.com
