# FastAPI Template
This is a template for building web applications using FastAPI framework. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Getting Started
To get started with this template, follow the steps below:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/suhairshareef/fastapi-template.git
   ```

2. Navigate to the project directory:
   ```bash
   cd fastapi-template
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:
   ```bash
   python server.py
   ```
You should see the FastAPI application running at http://localhost:8000 in your browser.


## Project Structure
The project structure is organized as follows:

```css
fastapi-template/
    ├── migrations/
    │   └── __init__.py
    ├── models/
    │   └── __init__.py
    ├── routes/
    │   ├── __init__.py
    │   └── routes.py
    ├── schemas/
    │   └── __init__.py
    ├── helpers/
    │   └── __init__.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_main.py
    ├── utils/
    │   └── definitions.py
    ├── .env
    ├── server.py
    ├── settings.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```

* The `models` directory contains the data models for your application.
* The `routes` directory contains the API routes implementation.
* The `schemas` directory contains the schemas for request/response validation.
* The `helpers` directory contains any helper functions or utilities.
* The `tests` directory contains the test cases for the application.
* The `utils` directory contains utility functions or classes.
* The `.env` file contains environment variables for the application.
* The `server.py` file is the entry point of the application.
* The `settings.py` file contains application settings and configurations.
* The `.gitignore` file specifies the files and directories to be ignored by Git.
* The `README.md` file contains information about the template and instructions for getting started.
* The `requirements.txt` file lists the Python dependencies required by the application.

## API Routes
API routes are defined in the `./routes/` directory. You can add your own routes and handlers in this directory.

Here's an example route that responds with "Hello, World!":

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```
You can add more routes by following the same pattern.

## Testing
The template includes a basic test case for the main application. You can add more test cases in the tests directory. To run the tests, use the following command:

```bash
pytest
```

## Deployment
To deploy the FastAPI application, you can use any hosting provider or deploy it on your own server. Make sure to configure the appropriate deployment settings based on your chosen deployment method.


## License
This template is licensed under the MIT License. See the LICENSE file for more details.
