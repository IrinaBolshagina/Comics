
import torch
from transformers import pipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


# descriptions_list = [
#     "a man in a suit and tie is dancing with his friends",
#     "a woman in a white shirt and black pants with red hearts",
#     "a woman in a pink flamingo swimsuit sitting on an inflatable",
#     "a man standing on a bridge",
#     "a man riding a horse"]

# number_of_characters = [3,1,1,1,1]

# pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# messages = [
#     {
#         "role": "system",
#         "content": "You are a comic book writer who creates funny comic book stories. An artist gives you pictures one by one and you write short dialogs for each picture. The number of lines in each dialog equals number of characters on the picture. Each line should be no longer than 300 characters. The story must be consistent and continue from one picture to another",
#     },
#     {"role": "user", "content": f"Write me only {str(num)} lines of dialogue, one for each of {str(num)} character on this picture:{prompt}"},
# ]
# prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# outputs = pipe(prompt, max_new_tokens=500, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
# return(outputs[0]["generated_text"])

# create_lines(descriptions_list[0], number_of_characters[0])


# pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
# messages = [
#     {
#         "role": "system",
#         "content": "You are a friendly chatbot who always responds in the style of a pirate",
#     },
#     {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
# ]
# prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
# print(outputs[0]["generated_text"])


model_path = 'ahxt/LiteLlama-460M-1T'

model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.eval()

prompt = 'Q: Write me only 3 lines of dialogue, one for each of 3 character on this picture: "a man in a suit and tie is dancing with his friends"\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
tokens = model.generate(input_ids, max_length=100)
print( tokenizer.decode(tokens[0].tolist(), skip_special_tokens=True) )
# Q: What is the largest bird?\nA: The largest bird is a black-headed gull.
