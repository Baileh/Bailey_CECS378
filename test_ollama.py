import ollama

try:
    response = ollama.chat(
        model = 'phi',
        messages = [{'role': 'user', 'content': 'Explain the CIA Tried in cybersecurity.'}]
    )

    print(response['message']['content'])
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure the Ollama application is running.")