
# NutriHive - Family Budget and Healthy Eating Website

## Project Overview
NutriHive is a static website designed to help low-income households, especially co-living students, bridge the gap between health management and budget optimization. It offers a user-friendly solution for balanced nutrition at minimal cost. Key features include multi-member management, tailored recipe suggestions, and optimized shopping lists, ensuring individualized recommendations for each person while facilitating collaborative shopping.

## How to Compile and Run

### Step One: Installing Dependencies
Before starting, please install all the required dependencies. Use the following commands:

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Login
pip install Flask-Migrate
pip install SQLAlchemy
```

### Step Two: Navigate to the Flask Folder
First, change your working directory to the folder named `Flask`, which contains the Flask application code:

```bash
cd path/to/Flask
```

### Step Three: Run the Application
To start the Flask server, run the command below:

```bash
python app.py
```

### Step Four: Access the Application
After running the above command, you will see a URL, typically something like `http://127.0.0.1:5000/`. Click on the link or enter it in your browser to access NutriHive.

## Data Dependencies
This section provides information on all the data required by the project, including data sources and storage locations.

### Data
- **Database**: SQLite databases (`db.sqlite`, `db.sqlite1`, `db.sqlite2`), located in the `flask/instance` directory, are used to manage user data, track dietary preferences, and generate personalized recommendations.

- **Image Resources**: 
  - **Supermarket Products**: Images are stored in `flask/static/Coles` and `flask/static/Woolworths`.
  - **Recipe Images**: Located in `flask/static/images`.

- **Configuration Data**: The `config.py` file contains details about ingredients, recipes, and allergens.

### Data Sources
- **Supermarket Product Information**: Product data is sourced from Coles and Woolworths:
  - [Coles](https://www.coles.com.au/)
  - [Woolworths](https://www.woolworths.com.au/)

- **Recipe Information and Images**: Recipe details are provided by:
  - [Dietitians Australia Recipes](https://dietitiansaustralia.org.au/health-advice/recipes)
  - [VegKit Recipes](https://www.vegkit.com/recipes/?filters%5BrecipeType%5D%5B0%5D)

The product data and recipe images are stored in respective directories (`flask/static/Coles`, `flask/static/Woolworths`, and `flask/static/images`), while the recipe information is in `config.py`.

## Software and Libraries Used
The following software and libraries are used in this project. For your convenience, we have provided the relevant source links:

1. **Flask** - A micro web framework for Python.
   - Source: [Flask on GitHub](https://github.com/pallets/flask)
   - Documentation: [Flask Documentation](https://flask.palletsprojects.com/)

2. **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask applications.
   - Source: [Flask-SQLAlchemy on GitHub](https://github.com/pallets/flask-sqlalchemy)
   - Documentation: [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

3. **Flask-Login** - A user session management for Flask.
   - Source: [Flask-Login on GitHub](https://github.com/maxcountryman/flask-login)
   - Documentation: [Flask-Login Documentation](https://flask-login.readthedocs.io/)

4. **Flask-Migrate** - Handles SQLAlchemy database migrations for Flask applications using Alembic.
   - Source: [Flask-Migrate on GitHub](https://github.com/miguelgrinberg/flask-migrate)
   - Documentation: [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)

## Summary
This document provides information about the dependencies, data requirements, and steps for compiling, executing, and running the NutriHive code. It also lists the reused software and their sources.
