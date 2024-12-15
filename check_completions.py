from huggingface_hub import InferenceClient

client = InferenceClient(
    base_url="http://127.0.0.0:8080",
)

prompt = f"""<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

Given a user query: {'cake'} return a list of items relevant to the query from item list: {'cake topping, cream , dough, meat ,banana' }[/INST]
"""

output = client.text_generation(prompt)
print(output)