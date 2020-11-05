
try:
    import sys
    import os
    print("Python version")
    print(sys.version)
    if 'LOCAL_PIP_PATH_SL' in os.environ:
        sys.path.append(os.environ['LOCAL_PIP_PATH_SL'])  # nopep8 # noqa
    elif 'EFS_PIP_PATH' in os.environ:
        sys.path.append(os.environ['EFS_PIP_PATH'])  # nopep8 # noqa
    else:
        raise Exception("If you are locak set LOCAL_PIP_PATH_SL and if you are in lambda set EFS_PIP_PATH")
except ImportError:
    pass

import json
from model.model import get_model,get_tokenizer,serverless_pipeline

model = get_model('distilbert-base-cased-distilled-squad')
tokenizer = get_tokenizer('distilbert-base-cased-distilled-squad')
question_answering_pipeline = serverless_pipeline(model,tokenizer)


def handler(event, context):
    try:
        print(event['body'])
        # extract body
        body = json.loads(event['body'])
        # init pipeline
        # predict the answer
        answer = question_answering_pipeline(question=body['question'], context=body['context'])
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
