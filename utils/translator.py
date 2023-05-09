import googletrans


trans = googletrans.Translator()

def t(word, lang):
    if lang == 'ko':
        return word
    
    return (trans.translate(word, dest=lang)).text
