import sys
import os
sys.path.append(os.environ['EFS_PIP_PATH'])  # nopep8 # noqa
import json
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

question_answering_pipeline = serverless_pipeline()

def handler(event, context):
    try:
        print(event['body'])
        # extract body

        body = json.loads(event['body'])
        # init pipeline
        # predict the answer
        answer = question_answering_pipeline(question=body['question'], context=body['context'])
        print(answer)
        #return
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'answer': answer})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
