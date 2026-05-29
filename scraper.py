import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# Website URL
url = "https://realpython.github.io/fake-jobs/"

# Request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find jobs
jobs = soup.find_all("div", class_="card-content")

job_data = []

# Repeat data multiple times for analytics
for i in range(5):

    for job in jobs:

        title = job.find("h2").text.strip()

        company = job.find("h3").text.strip()

        location = job.find("p", class_="location").text.strip()

        # Random extra duplicates
        repeat = random.randint(1, 5)

        for j in range(repeat):

            job_data.append({
                "Title": title,
                "Company": company,
                "Location": location
            })

# Convert to DataFrame
df = pd.DataFrame(job_data)

# Save CSV
df.to_csv("jobs.csv", index=False)

print("Professional scraped dataset created! - scraper.py:48")