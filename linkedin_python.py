import sys
import requests
import json
import mysql.connector

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/person_data_with_educations"
payload = { "link": "https://www.linkedin.com/in/ingmar-klein" }
headers = {
	"x-rapidapi-key": "cf894f83dcmsh358be998effcec6p1692eajsn9aab1a4665c7",
	"x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Establish MySQL connection
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Arb1ndr@",
        database="test"
    )

    cursor = conn.cursor()

    # Create table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS linkedin_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        company_id INT,
        company_linkedin_url TEXT
    )
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert company data
    for experience in data['data']['experiences']:
        company_id = experience["companyId"]
        print(company_id)
        company_linkedin_url = experience.get("companyLink1")
        print(company_linkedin_url)

        if company_id and company_linkedin_url:
            insert_query = """
            INSERT INTO linkedin_data (company_id, company_linkedin_url)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (company_id, company_linkedin_url))
    
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    print("\nData inserted successfully into the database.")

else:
    print(f"Error: {response.status_code} - {response.json()}")