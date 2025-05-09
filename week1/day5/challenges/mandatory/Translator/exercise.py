# Daily challenge: Translator

import asyncio
from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt" ,"Merci"]

translator = Translator()

async def translate_words():
    translations = {}
    for word in french_words:
        result = await translator.translate(word, src='fr', dest='en')
        translations[word] = result.text
    print(translations)

# Lancement de la boucle async
asyncio.run(translate_words())

