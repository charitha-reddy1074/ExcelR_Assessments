import spacy

def pos_tagging(sentence):
    """Perform part-of-speech tagging on a sentence using SpaCy."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    print("Part-of-Speech Tags:")
    for token in doc:
        print(f"{token.text}: {token.pos_}")

if __name__ == "__main__":
    sentence = "NLP is amazing and fun to learn."
    pos_tagging(sentence)
