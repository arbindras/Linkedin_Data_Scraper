# Linkedin_Data_Scraper
#1. Overview

The LinkedIn Data Scraper project is designed to extract specific information from a LinkedIn profile using the LinkedIn Bulk Data Scraper API. The extracted data, specifically the companies associated with the profile, is then stored in a MySQL database for further use or analysis.
#2. Workflow
Step 1: API Request
•	A POST request is made to the LinkedIn Bulk Data Scraper API with the LinkedIn profile link provided as input.
•	The API returns a JSON response containing various details about the profile, including work experiences, education, skills, and more.
Step 2: Data Extraction
•	The JSON response is parsed to extract specific information, such as the companyId and companyLink1 from the experiences section of the profile.
Step 3: Database Connection
•	A connection is established to a MySQL database using the mysql.connector library.
•	If the specified table (linkedin_data) does not already exist in the database, it is created.
Step 4: Data Insertion
•	The extracted data (companyId and companyLink1) is inserted into the linkedin_data table.
•	The database connection is then closed after the operation is complete.
Step 5: Output
•	The script prints a success message once the data has been successfully inserted into the database.

#3. Database Schema
Table: linkedin_data
Column Name	Data Type	Description
id	INT (Primary Key, Auto Increment)	Unique identifier for each record
company_id	INT	The ID of the company associated with the profile
company_linkedin_url	TEXT	The LinkedIn URL of the company
Table Creation Query
sql
Copy code
CREATE TABLE IF NOT EXISTS linkedin_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    company_linkedin_url TEXT
);
#4. Assumptions and Considerations

•	API Key and Host: The script assumes that a valid API key and host for the LinkedIn Bulk Data Scraper API are provided.
•	Database Connection: The script assumes that the MySQL database is hosted locally (127.0.0.1) and that the credentials (root, Arb1ndr@) are valid for the test database.
•	Data Integrity: Only records with both companyId and companyLink1 are inserted into the database. This ensures that incomplete data does not populate the database.
•	Error Handling: Basic error handling is implemented to ensure that API request failures are reported.
5. How to Run the Script
Prerequisites
•	Python 3.x installed on your system.
•	MySQL server running with access credentials as defined in the script.
•	Required Python libraries:
o	requests
o	mysql.connector
# Running the Script
1.	Install the required Python libraries:
pip install requests mysql-connector-python
2.	Run the Python script:
python linkedin_data_scraper.py
3.	Check the MySQL database to verify that the data has been inserted correctly.
