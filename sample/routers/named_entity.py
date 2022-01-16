from typing import List
from fastapi import APIRouter
import sample.schemas.named_entity as named_entity

router = APIRouter()

@router.post("/named_entity", response_model=List[named_entity.Response])
async def named_entity(request: named_entity.Request):
    import spacy
    nlp = spacy.load('ja_ginza')
    doc = nlp(request.text)
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
