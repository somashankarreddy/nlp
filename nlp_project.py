
import spacy

def extract_named_entities(text):
    # Load the spaCy English model
    try:
        nlp = spacy.load("en_core_web_sm")
    except Exception as e:
        print(f"Error loading spaCy model: {e}")
        return {}

    # Process the text
    doc = nlp(text)

    # Extract entities
    entities = {"PERSON": [], "GPE": [], "DATE": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities

# Example usage
text = input("Enter a text: ")
entities = extract_named_entities(text)

# Check if any entities were found
if any(entities.values()):
    print("Named Entities Found:")
    for label, entity_list in entities.items():
        if entity_list:
            print(f"{label}: {', '.join(entity_list)}")
else:
    print("No relevant named entities found.")