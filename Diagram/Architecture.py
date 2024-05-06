# run uder the Diagram folder

from diagrams import Diagram, Cluster
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.analytics import Dbt
from diagrams.programming.language import Python
from diagrams.custom import Custom
# import os
# print(os.getcwd())
with Diagram("Project Workflow", show=True, direction="LR"):
    pydantic = Custom("Pydantic", "pydantic-logo.png")  # Update the path to the Pydantic logo image

    with Cluster("Data Validation & Processing",direction="LR"):
        with Cluster("Web Data"):
            url_class = Python("URLClass")
        with Cluster("PDF Data"):
            meta_data_pdf_class = Python("MetaDataPDFClass")
            content_pdf_class = Python("ContentPDFClass")

    with Cluster("Data Storing and Processing"):
        dbt = Dbt("DBT")
        postgresql = PostgreSQL("Snowflake")
    
    url_class >> pydantic 
    meta_data_pdf_class >> pydantic 
    content_pdf_class >> pydantic >> dbt >> postgresql
    postgresql >> dbt
