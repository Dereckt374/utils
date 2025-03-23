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

    text = """"
    The two six-unit XL cubesats, known as Kepler-4 and Kepler-5 but nicknamed Antilles and Amidala, were among the 15 smallsat secondary payloads brokered by Exolaunch that launched on a Soyuz-2.1b from the Plesetsk Cosmodrome in northern Russia at 7:20 a.m. Eastern. The primary payload for the launch was a trio of Gonets satellites for the Russian government.

    The two Kepler satellites are the first “GEN1” satellites for the company after the launch of three prototypes, two in 2018 and the third Sept. 2 on a Vega dedicated rideshare mission. The three prototypes were built in cooperation with AAC Clyde Space.

    The new GEN1 satellites, however, were built by Kepler at a satellite manufacturing facility it established at its Toronto headquarters late last year. The company said that challenges in “maturing the supply chain” in the satellite manufacturing industry led it to establish an in-house production capability rather than work with an existing manufacturer.

    “We’re able now to own the production of this very capable platform,” Jared Bottoms, director of space systems at Kepler, said during a company webcast about the launch. “We really wanted to centralize our production in downtown Toronto to take advantage of the fast-paced atmosphere, the wide breadth of talent that we can tap into, and take that spirit and apply it to the space industry.”

    That internal production capability will allow the company to adopt what it calls a “lean and agile” approach to producing its satellites. “Building a production line associated with that allows us to be cost efficient while also allowing us to be innovative and collaborative,” said Shehroz Hussain, production control lead at Kepler.

    The GEN1 satellites incorporate improvements over the three prototypes, including increased power and improved thermal control, as well as updates to the communications payload. Those satellites will provide store-and-forward communications for large data files as well as narrowband Internet of Things services for asset tracking and monitoring.

    """

    
    num_sentences_to_generate = 1
    summary = generate_summary(num_sentences_to_generate, text)
    summary_listed = ','.join([ str(i) for i in summary])

    print(f'number of characters of summary : {len(summary_listed)} over {len(text)}')
    print(f'compression of : {len(summary_listed)/len(text)*100:.2f} %')
    print(summary)

if __name__ == "__main__":
    main()
