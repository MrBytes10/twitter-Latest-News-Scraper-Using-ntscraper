"""# First , open the terminal and run this: pip install ntscraper
from ntscraper import Nitter
import json
import pandas as pd

# Get the latest 100 tweets from a single user (@elonmusk in this example)
tweets= Nitter().get_tweets("python jobs", mode="term", number=100)

# Export the data in json format
with open("elon.json", "w") as file:
    json.dump(tweets, file, indent=4)

# Read the JSON file
with open("pyJobs.json", "r") as file:
    data = json.load(file)

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file = "pyJobs_tweets.xlsx"
df.to_excel(excel_file, index=False)

print(f"Tweets saved to {excel_file}")"""


# First, open the terminal and run this: pip install ntscraper pandas openpyxl
from ntscraper import Nitter
import pandas as pd

# Define search parameters for fetching tweets related to Python jobs
search_query = "python jobs filter:links"  # Adjust the query if needed
number_of_tweets = 100

# Get the latest tweets based on the search query
tweets = Nitter().get_tweets(search_query, mode="term", number=number_of_tweets)



# Convert the tweet data to a pandas DataFrame
df = pd.DataFrame(tweets)

# Save the DataFrame to an Excel file
excel_file = "python_jobs_tweets.xlsx"
df.to_excel(excel_file, index=False)

print(f"Tweets saved to {excel_file}")



# run python xLatestNewsScraper.py