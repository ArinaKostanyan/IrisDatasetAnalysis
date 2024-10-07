# Iris Statistics and SQL Projects

## Overview

This project comprises two main components:

1. **Iris Statistics Project**: Computes summary statistics for the Iris dataset using an Object-Oriented Programming (OOP) approach in Python. The statistics include basic metrics like mean, median, and custom metrics such as the coefficient of variation. The results are exported to an Excel file into `output folder for easy review.

2. **SQL Projects**: Involves creating and managing SQL databases and tables. This part of the project includes SQL scripts to set up databases and sample data, allowing for complex queries and data analysis.

## Features

### Iris Statistics Project

- **OOP Design**: Encapsulates functionality within a `StatisticsCalculator` class, promoting code reusability and organization.
- **Comprehensive Statistics**: Computes both basic (mean, median, mode) and custom statistical measures (coefficient of variation, interquartile range).
- **Testing**: Includes unit tests to ensure the reliability and correctness of the computations.
- **Excel Export**: Results are exported to an Excel file for easy review and sharing.

### SQL Projects

- **Database Management**: Create and manage SQL databases and tables using Python and MySQL.
- **Data Insertion**: Insert sample data into created tables for analysis.
- **Query Execution**: Execute complex SQL queries to extract meaningful insights from the data.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ArinaKostanyan/TestWork.git
   cd WaveaccessTask
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Add your credentials for initializing a database**

   1. Be sure to have installed MySQL.

   2. Create .env file for your DB personal data. `touch .env`
      Example:
      DB_HOST='localhost'
      DB_USER='user_name'
      DB_PASSWORD='user_password'

## Usage

    Execute the main script to compute statistics and generate the Excel report:
    `python main.py`
    To set up the database and tables, execute the SQL script for task1:
    `python task1.py`
    To execute the SQL script for task2:
    `python task2.py`

## Testing

    python -m unittest discover -s test
