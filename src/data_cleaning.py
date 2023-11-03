import pandas as pd

def text_cleaning(text):
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("'", "")
    text = text.split(" ")
    return text

def build_sentence_answer(conversation, dict_sentence):
    for i in range(len(conversation)-1):
        sentence = dict_sentence[conversation[i]]
        answer = dict_sentence[conversation[i+1]]
        yield sentence, answer

dict_sentence = {}
with open("data/movie_lines.tsv", "r") as f_lines:
    for line in f_lines:
        line = line[:-1].split("\t")
        key = line[0].replace("\"","")
        dict_sentence[key] = line[4]

with open("data/movie_conversations.tsv", "r") as f_conversation:
    with open("sentence.csv", "w") as f_output:
        for conversation in f_conversation:
            conversation = text_cleaning(conversation[:-1].split("\t")[3])
            for sentence, answer in build_sentence_answer(conversation, dict_sentence):
                f_output.write(f"{sentence},{answer}\n")