import pandas as pd
from sqlalchemy import create_engine, text

# Reads CSV file into pandas dataframe using 'latin1' encoding
# Adjust the encoding if necessary
df = pd.read_csv('news_articles.csv', encoding='latin1')  # Replace 'latin1' with the correct encoding if needed

# Save the DataFrame to a new CSV file with UTF-8 encoding
df.to_csv('news_articles_utf8.csv', index=False, encoding='utf-8') #index=False ensures Dataframe's index not written to csv file

# Re-load the CSV file with UTF-8 encoding into another dataframe
df_utf8 = pd.read_csv('news_articles_utf8.csv', encoding='utf-8')

# Create a connection to PostgreSQL
engine = create_engine('postgresql://postgres:Personic1!@localhost:5432/postgres')

# Write DataFrame to PostgreSQL in table called 'articles', this will create the table if it doesn't exist
df_utf8.to_sql('articles', engine, index=False, if_exists='replace')

# Verify import
with engine.connect() as connection: # establish connection to postgresql db
    # Use SQLAlchemy text construct for raw SQL
    result = connection.execute(text("SELECT COUNT(*) FROM articles;")) #count no. of rows in articles table
    count = result.scalar() #count from query execution

print(f"Number of rows in the database table: {count}") 
print(f"Number of rows in the CSV file: {len(df_utf8)}") 
