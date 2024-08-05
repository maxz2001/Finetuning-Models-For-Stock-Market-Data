from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key='sk-proj-4ahxeEw12MgwlzMkwJkMT3BlbkFJpohecZTmZSX3FTF3bI3M')

def get_fine_tuned_model_id(): # retrieve id of most recent fine-tuned model
    # Retrieve the list of fine-tuning jobs from OpenAI API
    fine_tune_jobs = client.fine_tuning.jobs.list()

    # Find the most recent fine-tune job that succeeded
    for job in fine_tune_jobs.data: # iterates over list of fine-tuning jobs
        if job.status == 'succeeded':
            return job.fine_tuned_model # return id of fine-tuned model if successful job found
    raise Exception("No successful fine-tuning job found.")

def generate_response(prompt):
    fine_tuned_model_id = get_fine_tuned_model_id() # get id of most recent fine-tuned model

    try:
        response = client.chat.completions.create(  # send request to generate response from fine-tuned model
            model=fine_tuned_model_id,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}, # set role of assistant
                {"role": "user", "content": prompt} # sets user message as prompt
            ],
            max_tokens=150, # each token is a word
            temperature=0.7, # level of randomness, 0.7 = moderate level of creativity
        )
        return response.choices[0].message.content.strip() # return content of generated response, whitespace eliminated
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# Example usage
prompt = "Explain Nvidia's events in July 2024."
response = generate_response(prompt)
print(f"Response: {response}")
