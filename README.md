# Finetuning Models For Stock Market Data

Pip installations: <br />
• pandas <br />
• sqlalchemy <br />
• psycopg2-binary <br />
<br />

Set up local postgres database <br />

## About

This project aims to finetune an openai gpt3.5 model using a specific CSV file column as input and two other columns as output. For my own CSV file, I used a column containing complete article text as input, and columns for the company's ticker symbol and name as output. The finetuned model will create a generate_response function for: 'explain nvidia's events in july 2024'. To test this project, I used a CSV file that contained news articles data on some of the most popular companies that are traded on the stock market. <br />

There are separate Python scripts for: <br />
• Loading the news articles CSV dataset into postgresql local database <br />
• Loading the OpenAI finetuning API using a key <br />
• Creating a finetuning dataset and job with the news data <br />
• Loading the finetuned model and generating a response

### load_data.py

Reads a CSV file named news_articles.csv into a pandas DataFrame, df, using 'latin1' encoding, and then writes this DataFrame to a new CSV file named (your csv filename).csv using UTF-8 encoding. The script reads the new UTF-8 encoded CSV file into another DataFrame, df_utf8. It then creates a connection engine to a PostgreSQL database using SQLAlchemy, with specified credentials and database details. The DataFrame df_utf8 is written to a table named articles in the PostgreSQL database, replacing any existing table with the same name. The script establishes a connection to the database, executes a SQL query to count the number of rows in the articles table, retrieves the count, and prints both the number of rows in the database table and in the DataFrame.

## prepare_finetuning_data.py

Fetches data from a PostgreSQL database and prepares it for fine-tuning a model, ultimately creating a JSON file. It imports necessary libraries, including json and pandas, and establishes a connection to a PostgreSQL database using SQLAlchemy. The script executes a SQL query to retrieve specific columns from the articles table and loads the data into a pandas DataFrame. It then processes each row, checking for non-null article text and formatting the data into a list of dictionaries representing a conversation between a user and an assistant. The formatted data is appended to a list, which is then written to a file named finetuning_data.jsonl in JSON Lines format. This file will be used for fine-tuning a language model.

## upload_and_finetune

Uploads a dataset to OpenAI and creates a fine-tuning job. It imports the OpenAI class from the openai library and the time library. An instance of the OpenAI client is created using an API key to interact with OpenAI’s API. The script attempts to upload the finetuning_data.jsonl file for fine-tuning, handling any exceptions that may occur during the upload process. If successful, it retrieves and prints the file ID. Next, it attempts to create a fine-tuning job using the uploaded file and the gpt-3.5-turbo-0613 model, handling any exceptions during job creation. If successful, it retrieves and prints the fine-tuning job ID. The script then enters an infinite loop to continuously check the status of the fine-tuning job, printing the current status and any events until the job completes or an error occurs, with a 30-second pause between status checks.

## generate.py

Loads a fine-tuned model and generates a response using the OpenAI API. It imports the OpenAI class and creates a client instance with an API key to interact with the API. The script defines a function, get_fine_tuned_model_id, to retrieve the ID of the most recently fine-tuned model by checking for successful fine-tuning jobs. Another function, generate_response, generates a response using this fine-tuned model. It sets up a conversation context and sends a request to the OpenAI API to generate a response, handling any exceptions that may occur. The generated response is returned and printed. The script defines a prompt about Nvidia's events in August 2024, calls the generate_response function with this prompt, and prints the response.



