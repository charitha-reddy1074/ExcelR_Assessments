import spacy

def perform_ner(text):
    """Perform Named Entity Recognition (NER) on the given text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    print("Named Entities and Their Types:")
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")

if __name__ == "__main__":
    text = input("Enter text to perform NER: ")
    perform_ner(text)
