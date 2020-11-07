from transformers import AutoModelForQuestionAnswering, AutoTokenizer

def get_model(model):
  """Loads model from Hugginface model hub"""
  try:
    model = AutoModelForQuestionAnswering.from_pretrained(model,use_cdn=True)
    model.save_pretrained('./model/files')
  except Exception as e:
    raise(e)
  
def get_tokenizer(tokenizer):
  """Loads model from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    tokenizer.save_pretrained('./model/files')
  except Exception as e:
    raise(e)
  
  
# get_model('distilbert-base-cased-distilled-squad')
# get_tokenizer('distilbert-base-cased-distilled-squad')
get_model('mrm8488/mobilebert-uncased-finetuned-squadv2')
get_tokenizer('mrm8488/mobilebert-uncased-finetuned-squadv2')