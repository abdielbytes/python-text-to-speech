from gtts import gTTS

def text_to_speech(text, filename, lang='en', tld='co.uk'):
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.save(filename)
