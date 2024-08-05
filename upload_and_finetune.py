from openai import OpenAI
import time

# Initialize the OpenAI client to interact with api
client = OpenAI(api_key='INSERT API KEY HERE')

# Upload the fine-tuning file
try:
    response = client.files.create(
        file=open("finetuning_data.jsonl", "rb"),
        purpose='fine-tune'
    )
    file_id = response.id # retrieves id of uploaded file from response
    print(f"File uploaded successfully. File ID: {file_id}")
except Exception as e:
    print(f"Error uploading file: {e}")
    exit(1) # status code 1 indicates error

# Create a fine-tune job
try:
    fine_tune_response = client.fine_tuning.jobs.create( 
        training_file=file_id,
        model="gpt-3.5-turbo-0613"  # Use the GPT-3.5 model
    )
    fine_tune_id = fine_tune_response.id # retrieves id of fine-tuning job from response
    print(f"Fine-tune job created successfully. Fine-tune ID: {fine_tune_id}")
except Exception as e:
    print(f"Error creating fine-tune job: {e}")
    exit(1)

# Check the fine-tune job status
while True:
    try:
        status_response = client.fine_tuning.jobs.retrieve(fine_tune_id) # retrieve status of fine-tuning job using job id
        status = status_response.status # status of fine-tuning job from response
        print(f"Fine-tuning status: {status}")
        
        if status in ["succeeded", "failed"]:
            print(f"Fine-tune job completed. Status: {status}")
            print(f"Fine-tuned model: {status_response.fine_tuned_model}") # prints id of fine-tuned model
            
            # Print fine-tuning job events
            events_response = client.fine_tuning.jobs.list_events(fine_tune_id) # list events associated with fine-tuning job
            for event in events_response.data:
                print(event)
            break
        time.sleep(30)
    except Exception as e:
        print(f"Error checking fine-tune status: {e}")
        break
