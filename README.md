# Assignment 3: Python Classes and DBT Integration for Data Management

## Overview

This project involves designing Python classes for managing data schemas and implementing DBT for data transformation workflows. It is divided into two parts:

- **Part 1:** Design of Python classes (`URLClass`, `MetaDataPDFClass`, and `ContentPDFClass`) for data schema representation and validation.
- **Part 2:** Utilization of DBT with Snowflake for running transformation workflows on cleaned data.

## Related Links

- [![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1_ZuYHgvTGdHBf7qtLQNaO-pem1ZU3vnN2BTnCqzulAE/)

## Goals

- **Part 1:**
  - Design and validate data schemas for webpages and PDF content using Pydantic.
  - Create clean CSV files from validated data.
  - Develop 5 positive and 5 negative test cases for each class using Pytest.
- **Part 2:**
  - Integrate DBT with Snowflake to transform and summarize data.
  - Create a summary table with specified schema.
  - Document and deploy the DBT model.

## Technologies Used

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)

- Pydantic
- Pytest

[![Snowflake](https://img.shields.io/badge/snowflake-0000FF?style=for-the-badge&logo=snowflake&logoColor=white)](https://docs.snowflake.com/ )

- DBT & Snowflake

## Project Structure
```
.
├── Diagram
│   ├── Architecture.py
│   ├── project_workflow.png
│   └── pydantic-logo.png
├── README.md
├── data
│   ├── Validation_data.csv
│   ├── content.csv
│   ├── items.csv
│   ├── log.txt
│   ├── log_for_web.txt
│   ├── metadata.csv
│   └── metadata_new.csv
├── notebooks
│   ├── DBT
│   │   ├── core
│   │   │   ├── pdfscraping_model.sql
│   │   │   └── webscraping_model.sql
│   │   ├── dbt_project.yml
│   │   └── staging
│   │       ├── src_pdfdata.yml
│   │       ├── src_webscrape.yml
│   │       ├── stg_pdfcontents.sql
│   │       ├── stg_pdfdata.yml
│   │       ├── stg_pdfmetadata.sql
│   │       ├── stg_webscrape.sql
│   │       └── stg_webscrape.yml
│   ├── PDFParsing
│   │   └── PDFParsing.ipynb
│   └── requirements.txt
├── pytest
│   ├── ContentPDF_pytest.py
│   ├── MetaDataPDF_pytest.py
│   └── test_URLclass.py
├── utils
│   ├── Model_PDFClass.py
│   ├── URLclass.py
│   ├── __init__.py
│   └── __pycache__
│       ├── URLclass.cpython-311.pyc
│       └── __init__.cpython-311.pyc
└── xml
    ├── 2024-l1-topics-combined-2.pdf.tei.xml
    ├── 2024-l2-topics-combined-2.pdf.tei.xml
    ├── 2024-l3-topics-combined-2.pdf.tei.xml
    ├── Grobid_RR_2024_l1_combined_metadata.xml
    ├── Grobid_RR_2024_l2_combined_metadata.xml
    └── Grobid_RR_2024_l3_combined_metadata.xml
```
## Prerequisites

- General recommendation Python 3.8+ and required package
- DBT
- Snowflake

## Setup and Execution

### Part 1: Python and Jupyter Setup

1. **Create a Virtual Environment and Jupyter Kernel:**

   - Create a virtual environment:

      `python -m venv venv`

   - Activate the environment:

     - Windows: `.\venv\Scripts\activate`
     - Mac/Linux: `source venv/bin/activate`

   - Create a Jupyter kernel linked to this virtual environment: 

     `ipython kernel install --user --name=<your_env_name>`

2. **Install Dependencies:**

   - Install required packages:

      `pip install -r requirements.txt`

3. **Launch Jupyter:**

   - Start Jupyter Notebook: 

     `jupyter notebook`

4. **Environment Variables:**

   - Create a '.env' file in your project directory and add your account information in the format:

     ```
     A=<value>
     B=<value>
     C=<value>
     ```

5. **Execution Order:**

   - Run `a.ipynb` first to initialize the setup.
   - Follow with `b.ipynb`, `c.ipynb`, and `d.ipynb` in sequence for the complete execution flow.

Ensure to replace `<your_env_name>` with the name you prefer for your Jupyter kernel and `<value>` with your actual account details.

### Part 2: DBT and Snowflake Setup Using an Online IDE

1. **Access the Online IDE:**
   - Navigate to the DBT Cloud or a similar online IDE that supports DBT and Snowflake integration.
2. **Connect to Your Snowflake Warehouse:**
   - Within the IDE, locate the settings or configuration section to connect your DBT project to your Snowflake warehouse. You will need your Snowflake account details, including account identifier, username, and password.
3. **Configure Your DBT Project:**
   - Use the IDE's interface to create or import your DBT project. Follow the guided setup to configure your project, specifying the Snowflake connection details as required.
4. **Develop and Test Your Models:**
   - Directly within the IDE, begin developing your DBT models. Take advantage of the IDE's features for writing SQL, testing, and version control.
   - Utilize the `dbt run` and `dbt test` commands within the IDE's terminal or command interface to execute and test your models.
5. **Deploy Your DBT Models:**
   - Once satisfied with your DBT models, use the deployment features of the online IDE to deploy your models to your Snowflake warehouse.

For detailed instructions on using DBT, refer to the [DBT Tutorial](https://docs.getdbt.com/docs/introduction).



## Learning Outcomes

- **Python Class Design and Data Validation:** Deepened understanding of object-oriented programming in Python through designing classes that represent data schemas. Enhanced skills in data validation using Pydantic to ensure data integrity and reliability.
- **Automated Testing with Pytest:** Gained proficiency in writing and executing automated tests using Pytest, reinforcing the importance of test-driven development (TDD) for reliable software.
- **DBT and Snowflake Integration:** Acquired practical experience in setting up and using DBT with Snowflake for data transformation and workflow management, emphasizing the importance of data engineering best practices.

## References

- Pydantic Documentation
- DBT Documentation
- Snowflake Documentation

## Team

| Name         | NUID          |
| ------------ | ------------- |
| Dongyu Liu   |  002837324    |
| Ekta Bhatia  |  002767736    |
| Parth Kalani |  002766306    |
| Sumit Sharma |  002778911    |
