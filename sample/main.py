from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/")
def ginza(item: Item):
    import spacy
    nlp = spacy.load('ja_ginza')
    doc = nlp(item.text)
    tokens = []
    for sent in doc.sents:
        for token in sent:
            # print(
            #     token.i,
            #     token.orth_,
            #     token.lemma_,
            #     token.norm_,
            #     # token.morph.get(“Reading”),
            #     token.pos_,
            #     # token.morph.get(“Inflection”),
            #     token.tag_,
            #     token.dep_,
            #     token.head.i,
            # )
            tokens.append({'text': token.text, 'tag': token.tag_, 'entity_type': token.ent_type_})
    return tokens