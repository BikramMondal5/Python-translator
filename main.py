from googletrans import Translator

text = input("Enter your text:")
translator = Translator()
translator.detect(text)
translated = translator.translate(text)
print("Your translated text:",translated.text) 
