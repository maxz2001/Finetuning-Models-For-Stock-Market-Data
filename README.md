# Finetuning Models For Stock Market Data

Pip installations: <br />
• pandas <br />
• sqlalchemy <br />
• psycopg2-binary <br />
<br />

Set up local postgres database <br />

## About

The purpose of this project is to finetune an openai gpt3.5 model using a specific CSV file column as input and using two other columns as output. For my own CSV file, I used a column containing complete article text as input, and columns for the company's ticker symbol and name as output. The finetuned model will create a generate_response function for: 'explain nvidia's events in july 2024'. To test this project, I used a CSV file that contained news articles data on some of the most popular companies that are traded on the stock market. <br />

There are separate Python scripts for: <br />
• Loading the news articles CSV dataset into postgresql local database <br />
• Loading the OpenAI finetuning API using a key <br />
• Creating a finetuning dataset and job with the news data <br />
• Loading the finetuned model and generating a response

### load_data.py
