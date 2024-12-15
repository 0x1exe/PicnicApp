# PicnicApp
Small website with AI search capabilities 

The project was meant to experiment with item search using LLMs. 
The idea is to use the prompt: 
```
f"""<s>[INST] <<SYS>>
        You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
        If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
        <</SYS>>

        Given a user query: {user_query} return a list of items relevant to the query from item list: {item_list }[/INST]
        """
```
To make LLM return a list of items relevant to the query, which can then shown to the user. 

Project is not finished as idea has proven to be invalid (such search takes a lot of time and is basically as efficient as other options) 
