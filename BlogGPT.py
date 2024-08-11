# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import TextStreamer
import torch

class BlogMessages:
    def __init__ (self, device='cpu', tokenizer = None, tokenize = True):
        self.device = device
        self.tokenize = tokenize
        self.tokenizer = tokenizer
        self.tokenizer.pad_token_id= 128010

    def generate_headings_message(self, title, number=1):
        m = self._generate_headings_message(title)
        tensor = self.formatting_prompts_func(m)
        tensor = torch.tile(tensor, (number, 1)).to(self.device)
        return tensor


    def generate_blog_message(self, title, headings, number=1):
        m = self._generate_blog_message(title, headings)
        tensor = self.formatting_prompts_func(m)
        tensor = torch.tile(tensor, (number, 1)).to(self.device)
        return tensor

    @staticmethod
    def _generate_headings_message(title):
        m = [
            {"role": "system", "content": "You are a helpful AI assistant for writing blog headings"},
            {"role": "user", "content": f'''Generate headings for a blog titled "{title}"'''}]

        return {'messages':m}

    @staticmethod
    def _generate_blog_message(title, headings):
        m = [
            {"role": "system", "content": "You are a helpful AI assistant for writing entire blogs"},
            {"role": "user", "content": f'''Given a blog with title: "{title}", and headings: "{headings}", generate and write all content for the full blog."'''},
        ]

        return {'messages':m}

    # formatting function
    def formatting_prompts_func(self, examples):
        messages = examples['messages']
        texts = self.tokenizer.apply_chat_template(messages, tokenize = self.tokenize, add_generation_prompt = True, return_tensors='pt')
        return texts

# -

class BlogGPT:
    def __init__(self, content='Food&Travel'):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        if content == 'Food&Travel':
          pretrained_model_name_or_path = 'codyfalkosky/blogGPT_foodandtravel'


        self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path, device_map=device)
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, device_map=device)
        self.tokenizer.pad_token_id= 128010
        self.blog_messages = BlogMessages(device, self.tokenizer)
        self.text_streamer = TextStreamer(self.tokenizer, skip_prompt=False)

    def headings(self, title, number=1, max_new_tokens=2048):
        # text streamer only supports batch_size=1
        inputs = self.blog_messages.generate_headings_message(title, number)
        _ = self.model.generate(input_ids = inputs, streamer = self.text_streamer, max_new_tokens = max_new_tokens, use_cache = True)

    def blog(self, title, headings, number=1, max_new_tokens=2048, do_sample=False):
        # text streamer only supports batch_size=1
        if number==1:
            inputs = self.blog_messages.generate_blog_message(title, headings, number)
            _ = self.model.generate(input_ids = inputs, streamer = self.text_streamer, max_new_tokens = max_new_tokens, use_cache = True, do_sample = do_sample)
        else:
            inputs = self.blog_messages.generate_blog_message(title, headings, number)
            outputs = self.model.generate(input_ids = inputs, max_new_tokens = max_new_tokens, use_cache = True, do_sample = do_sample)
            return self.tokenizer.batch_decode(outputs)
