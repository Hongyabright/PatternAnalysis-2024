
# NutriHive - Personalized Nutrition Management System

## Project Overview
NutriHive is a web application that provides personalized nutrition planning for co-living or small household members. It generates nutrition recommendations and cost-optimized shopping lists based on individual health goals (e.g., fat loss, muscle gain, or time-saving). The system provides personalized meal plans and recipe recommendations based on users' dietary preferences, allergens, and health conditions.

## Installing Dependencies
Before starting, please install all the required dependencies. You can use the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains all the necessary libraries:

- Flask==2.0.1
- Flask-SQLAlchemy==2.5.1
- Flask-Login==0.5.0
- Flask-Migrate==3.1.0

## How to Compile and Run
1. **Create and Activate a Virtual Environment**  
   Run the following commands in the project root to create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**  
   Use the following command to install all the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to the Flask Folder and Run the Application**  
   Navigate to the `flask` directory and run the Flask application:
   ```bash
   cd flask
   python app.py
   ```
   After running, you will see a URL. Click on the link to access NutriHive.

## Data
- **Database**: SQLite databases (`db.sqlite`, `db.sqlite1`, `db.sqlite2`), located in the `flask/instance` directory.
- **Image Resources**: Stored in the `flask/static/Coles` and `flask/static/Woolworths` directories.
- **Configuration Data**: The `config.py` file contains information about ingredients, recipes, and allergens.

**Data Sources:**
- Supermarket product information from Coles and Woolworths websites:
  - [Coles](https://www.coles.com.au/)
  - [Woolworths](https://www.woolworths.com.au/)

## Dataset and Reused Software
### Reused Software
- **Flask**: Used as the web framework for building the application. For more details, visit the [Flask project homepage](https://flask.palletsprojects.com/).
- **Flask-SQLAlchemy**: Used as the ORM framework for managing the database. For more details, visit the [Flask-SQLAlchemy project homepage](https://flask-sqlalchemy.palletsprojects.com/).
- **Flask-Login**: Used to manage user authentication and sessions. For more details, visit the [Flask-Login documentation](https://flask-login.readthedocs.io/).
- **jQuery**: Used to enhance the interactivity of the pages. For more details, visit the [jQuery project homepage](https://jquery.com/).
- **Select2**: Used to enhance the dropdown selection experience. For more details, visit the [Select2 project homepage](https://select2.org/).
- **Pillow**: Used for handling images. For more details, visit the [Pillow documentation](https://pillow.readthedocs.io/).

## Live Implementation (Optional)
If the project has been deployed to the cloud, you can use the following link to access the live implementation:
- [NutriHive Live Implementation (Optional)](http://your-live-implementation-url.com)

---

This document provides information about the dependencies, data requirements, and steps for compiling, executing, and running the NutriHive code. It also lists the reused software and their sources.
