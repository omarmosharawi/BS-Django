# BS-Django: Book Store Application
Welcome to the BS-Django repository! This project is a book store application built using Django—a powerful Python web framework.


## Project Overview
The BS-Django repository hosts a book store application. While the current version is in its early stages, it aims to provide features like book catalog management, user authentication, and order processing.


## Installation and Setup
To run this project locally, follow these steps:

1. Clone the Repository:
```git clone https://github.com/omarmosharawi/BS-Django.git```

2. Navigate to the Project Directory:
```cd BS-Django```

3. Install Dependencies:
```pip install -r requirements.txt```

4. Database Setup:
- Create a PostgreSQL database (or use SQLite for development).
- Update the database settings in `book_store/settings.py.`

5. Run Migrations:
```python manage.py migrate```

6. Create a Superuser (for admin access):
```python manage.py createsuperuser```

7. Start the Development Server:
```python manage.py runserver```


## Usage
- Access the application at ```http://localhost:8000/```.
- Use the admin interface at ```http://localhost:8000/admin/``` (login with superuser credentials).


## Contributing
Contributions are welcome! If you’d like to contribute, please follow our guidelines for pull requests.

---
