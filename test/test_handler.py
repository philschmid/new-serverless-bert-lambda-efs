import os

os.environ['LOCAL_PIP_PATH_SL'] = "/Users/philippschmid/projects/personal/blog/blog-posts/new-serverless-bert-lambda/lib"

from handler import handler

test_events = {
    "body": '{"question": "Who has the most covid-19 deaths?", "context":"The US has passed the peak on new coronavirus cases,President Donald Trump said and predicted that some states would reopen this month. The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world."}'
}


context = "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement)."

question_one = "What is BERTs best score on Squadv2 ?"
# 83 . 1

question_two = "What does the 'B' in BERT stand for?"
# 'bidirectional encoder representations from transformers'
    
def test_handler():
    test_event1 = {"body": '{"question": "' +question_one +'", "context": "'+context+'"}'}
    res = handler(test_event1, '')



# lambci test_event1

#  docker run --rm -v "$PWD":/var/task:ro,delegated lambci/lambda:python3.8 handler.handler   '{"question": "Who has the most covid-19 deaths?", "context":"The US has passed the peak on new coronavirus cases,President Donald Trump said and predicted that some states would reopen this month. The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world."}'