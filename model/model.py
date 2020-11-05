

from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer


def get_model(model):
  """Loads model from Hugginface model hub"""
  try:
    model = AutoModelForQuestionAnswering.from_pretrained(model,cache_dir="/tmp",use_cdn=True)
  except Exception as e:
    raise(e)
  
def get_tokenizer(tokenizer):
  """Loads model from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer,cache_dir="/tmp")
  except Exception as e:
    raise(e)
  
  
def serverless_pipeline(model='',tokenizer=''):
  """creates an question answering pipeline"""
  try:
    my_pipeline = pipeline(task="question-answering",framework='pt',model=model,tokenizer=tokenizer)
    return my_pipeline
  except Exception as e:
    raise(e)