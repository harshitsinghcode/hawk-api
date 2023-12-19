# Hawk - The Django REST API  🚀

## Overview 🪟

This project is a Django REST API that manages information about companies and employees. It includes models for `Company` and `Employee`, along with serializers for API interactions. The API is exposed through the endpoints `/companies/` and `/employees/`.

## Installation🔽

1. **Clone the Repository:
   - git clone https://github.com/yourusername/your-repo.git
   - cd your-repo

2. **Create a Virtual Environment (Optional but in my case, i've done it):
- python -m venv venv
- Activate the Virtual Environment:

### On Windows:
- .\venv\Scripts\activate
### On Linux/Mac:
- source venv/bin/activate
- pip install -r requirements.txt

## Configuration & Database Setup 🪛

1. Ensure Django settings are properly configured, including database settings, secret key, etc.
2. Run migrations to create the database tables:

- python manage.py makemigrations
- python manage.py migrate

## API Endpoints 🔚

1. Companies
 - /companies/: List and create companies.
 - /companies/{id}/: Retrieve, update, and delete a company.
 - /companies/{id}/employees/: List employees of a specific company.

2. Employees
 - /employees/: List and create employees.
 - /employees/{id}/: Retrieve, update, and delete an employee.

## Usage ⛷️

1. Run the development server:

- python manage.py runserver
- Visit http://localhost:8000/admin/ to access the Django admin panel.

2. Use the following API endpoints:

- Companies: http://localhost:8000/companies/
- Employees: http://localhost:8000/employees/

3. Postman Collection 📬

- Use Postman to test the API. Import the provided Postman collection here.

- The Postman collection includes pre-configured requests for various API endpoints.

## Contributing 🤝
I welcome contributions to make this project even better! 

1. Fork the repository
2. Create a feature branch (git checkout -b feature/awesome-feature)
3. Commit your changes (git commit -m 'blah-blah-blah')
4. Push to the branch (git push origin feature/blah)
5. Open a pull request

## License 📜
This project is licensed under the MIT Liscence.

Always Onwards and Upwards! 🚀
