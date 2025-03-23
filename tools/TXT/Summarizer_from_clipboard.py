import win32clipboard
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from heapq import nlargest
punctuations = string.punctuation
from spacy.language import Language
nlp = English()
nlp.add_pipe('sentencizer') # updated
parser = English()



def pre_process(document):
    clean_tokens = [ token.lemma_.lower().strip() for token in document ]
    clean_tokens = [ token for token in clean_tokens if token not in STOP_WORDS and token not in punctuations ]
    tokens = [token.text for token in document]
    lower_case_tokens = list(map(str.lower, tokens))
    
    return lower_case_tokens

def generate_numbers_vector(tokens):
    frequency = [tokens.count(token) for token in tokens]
    token_dict = dict(list(zip(tokens,frequency)))
    maximum_frequency=sorted(token_dict.values())[-1]
    normalised_dict = {token_key:token_dict[token_key]/maximum_frequency for token_key in token_dict.keys()}
    return normalised_dict


def sentences_importance(text, normalised_dict):
    importance ={}
    for sentence in nlp(text).sents:
        for token in sentence:
            target_token = token.text.lower()
            if target_token in normalised_dict.keys():
                if sentence in importance.keys():
                    importance[sentence]+=normalised_dict[target_token]
                else:
                    importance[sentence]=normalised_dict[target_token]
    return importance



def generate_summary(rank, text):
    target_document = parser(text)
    importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
    summary = nlargest(rank, importance, key=importance.get)
    return summary



def main():

    # get clipboard data
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(f'number of characters of inital text : {len(text)}, for  {len(text.split("."))} sentences')
    num_sentences_to_generate = int(input('Nombre de phrase pour le résumé...'))
    summary = generate_summary(num_sentences_to_generate, text)
    summary_listed = ','.join([ str(i) for i in summary])

    print(f'number of characters of summary : {len(summary_listed)} over {len(text)}')
    print(f'compression of : {100-(len(summary_listed)/len(text)*100):.2f} %')
    print(summary)
    
    input('Close.')
    

if __name__ == "__main__":
    main()

