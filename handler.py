
try:
    import sys
    import os
    print("Python version")
    print(sys.version)
    #sys.path.append(os.environ['EFS_PIP_PATH'])  # nopep8 # noqa
    sys.path.append('/Users/philippschmid/projects/personal/serverless-efs-lambda/efsync/.efsync/lib')  # nopep8 # noqa
except ImportError:
    pass

import json
import os
import pyjokes
import glob
from pandas import DataFrame
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer


def handler(event, context):
    # model = AutoModelForTokenClassification.from_pretrained(
    #     "dbmdz/bert-large-cased-finetuned-conll03-english")
    # tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    x = pipeline('ner', model=model, tokenizer=tokenizer)
    print(x('I Love New York'))
    data = {'Product': ['Desktop Computer', 'Tablet', 'iPhone', 'Laptop'],
            'Price': [700, 250, 800, 1200]
            }

    df = DataFrame(data, columns=['Product', 'Price'])

    body = {
        "frame": df.to_dict(),
        "joke": pyjokes.get_joke(language='de')
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
