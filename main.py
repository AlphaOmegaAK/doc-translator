from googletrans import Translator

translator = Translator()

output = translator.translate('wie hiesen sie?', dest='en')
print(output.text)