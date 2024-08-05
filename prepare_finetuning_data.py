import json
import pandas as pd
from sqlalchemy import create_engine

# Create a connection to PostgreSQL
engine = create_engine('postgresql://postgres:Personic1!@localhost:5432/postgres')

# Load the data into a DataFrame
df = pd.read_sql("SELECT complete_article_text, symbol, title FROM articles", engine)

# Create a list of dictionaries with the required format
data = []
for index, row in df.iterrows(): # iterate over each row in dataframe
    if pd.notna(row['complete_article_text']):  # Ensure user content is not null
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}, # system message defines assistant's role
            {"role": "user", "content": row['complete_article_text']}, # user message containing article text
            {"role": "assistant", "content": f"{row['symbol']} - {row['title']}"} # assistant message containing symbol + title
        ]
        data.append({"messages": messages}) # appends 'messages' list as dictionary to 'data' list

# Save to a JSONL file
with open('finetuning_data.jsonl', 'w') as f: # f = write mode
    for item in data:
        f.write(json.dumps(item) + '\n') # each item in 'data' converted to JSON string and writes to file, newline char after each item
