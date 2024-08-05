# Inspect the first few lines of the generated finetuning_data.jsonl file
with open('finetuning_data.jsonl', 'r') as file:
    for _ in range(5):  # Adjust this number to inspect more lines
        print(file.readline())
