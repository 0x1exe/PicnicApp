from transformers import AutoTokenizer, AutoModelForCausalLM,Qwen2ForCausalLM, BitsAndBytesConfig
import re
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_compute_dtype=torch.bfloat16,
)

query='Something to eat with'
item_list='pork belly, beef , banana, berries , cake topping, salt,pen,pencil,spoon,fork,knife'

model_name='Qwen/Qwen2.5-7B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = Qwen2ForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    trust_remote_code=True,
)

model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

prompt = f"""Given a list of items, return those that may be relevant to the user input query.
Place items in order of relevance to the query. Return items in a list.
EXAMPLE:
input: query="cake",item_list = "cake topping, dough, cream,banana,berries" 
output: [dough,cake topping,cream]
CURRENT INPUT:
input: query = {query}, item_list={item_list}
output: 
"""
inputs = tokenizer(prompt, return_tensors="pt").to(device)

generate_ids = model.generate(inputs.input_ids, max_length=(len(item_list)+len(prompt)))
generated_output = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

def extract_output_tags(text):
    pattern = r'<output>(.*?)<\/output>'
    matches = re.findall(pattern, text)
    return matches

extracted_text = extract_output_tags(generated_output)
print(extracted_text, generated_output) 
