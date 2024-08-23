# OracleDBAAssistant
Use the master branch.
To set up and use the `OracleDBAAssistant` project, which is designed to manage day-to-day repetitive DBA tasks and run commands, follow these steps:
![Screenshot](docs/dba-1.png)
![Screenshot](docs/dba-2.png)
![Screenshot](docs/dba-3.png)
![Screenshot](docs/dba-4.png)
### Overview

`OracleDBAAssistant` is a Django web application that helps automate and manage routine DBA tasks and execute commands related to Oracle databases. 
This application aims to simplify daily database administration tasks.

### Step-by-Step Installation and Usage Guide

#### 1. Clone the Repository

Begin by cloning the `OracleDBAAssistant` repository from GitHub to your local machine.

**Command:**
```bash
git clone https://github.com/eduhapi/OracleDBAAssistant.git
```

This command will create a local copy of the repository on your computer.

#### 2. Navigate to the Project Directory

Change your current directory to the `OracleDBAAssistant` project folder.

```bash
cd OracleDBAAssistant
```

#### 3. Set Up a Virtual Environment

It’s essential to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

**Create a virtual environment:**

- **Windows:**
  ```bash
  python -m venv venv
  ```

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  ```

**Activate the virtual environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 4. Install the Required Dependencies

With the virtual environment activated, install the necessary dependencies specified in the `requirements.txt` file.

**Command:**
```bash
pip install -r requirements.txt
```

This will install all required libraries and packages needed for the application.

#### 5. Configure the Database

You will need to connect to your database instance that you inted to deploy the DBA Assistant  with the appropriate Oracle database connection details.
For an Oracle Express Edition (XE) database installed on Windows with default settings, you might enter the following details:

- **Instance Name**: `XE`
- **DSN**: `localhost:1521/XE`
- **Username**: `system`
- **Password**: `oracle`

#### 6. Apply Database Migrations

Apply migrations to set up the database schema for the application.

**Command:**
```bash
python manage.py migrate
```

This command initializes the database tables required by `OracleDBAAssistant`.

#### 7. Create a Superuser

To access the Django admin interface and manage the application, create a superuser account.

**Command:**
```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

#### 8. Run the Development Server

Start the Django development server to run the application locally.

**Command:**
```bash
python manage.py runserver
```

Open a web browser and navigate to `http://127.0.0.1:8000/` to access the application.

#### 9. Use the Application

1. **Log In:**
   - Log in to the Django admin interface using the superuser account you created.

2. **Manage DBA Tasks:**
   - Use the web interface to access various DBA management features and run commands.
   - The application allows you to automate and manage routine database administration tasks.

#### 10. Customize the Application

You can customize `OracleDBAAssistant` to better fit your specific needs:

- **Add New Features:** Implement additional DBA tasks or commands as required.
- **Enhance UI/UX:** Improve the user interface and user experience based on feedback.
- **Configure Alerts:** Set up notifications and alerts for specific database events or issues.

By following these steps, you will have a functional `OracleDBAAssistant` application that helps in managing and automating Oracle database administration tasks.
