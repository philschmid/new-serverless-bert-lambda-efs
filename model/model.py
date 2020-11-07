
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig

def encode(tokenizer, question, context):
    encoded = tokenizer.encode_plus(question, context)
    return encoded["input_ids"], encoded["attention_mask"]

def decode(tokenizer, token):
    answer_tokens = tokenizer.convert_ids_to_tokens(
        token, skip_special_tokens=True)
    return tokenizer.convert_tokens_to_string(answer_tokens)
      
def serverless_pipeline(model_path='./model/files'):
  print('before model init')
  tokenizer = AutoTokenizer.from_pretrained(model_path)
  model = AutoModelForQuestionAnswering.from_pretrained(model_path)
  print('after model init')
  def predict(question, context):
          input_ids, attention_mask = encode(tokenizer,question, context)
          start_scores, end_scores = model(torch.tensor(
              [input_ids]), attention_mask=torch.tensor([attention_mask]))
          ans_tokens = input_ids[torch.argmax(
              start_scores): torch.argmax(end_scores)+1]
          answer = decode(tokenizer,ans_tokens)
          return answer
  return predict
