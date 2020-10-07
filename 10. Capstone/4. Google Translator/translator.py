from googletrans import Translator
# from googletrans import Languages


translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])


# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
text = input("Enter text: ")
_src = input("Enter source language (Default: auto detect): ")
_dst = input("Enter destination language (Default: en): ")


if len(text)<1:
	handle = open('text.txt', 'r')
	text = handle.read()

if len(_dst)<1:
	_dst = 'en'

if len(_src)<1:
	_src = 'auto'

# print(googletrans.Languages)

dt = translator.detect(text)
print(dt)
print(type(dt))

translation = translator.translate(text, src = _src, dest = _dst)
# print(translation, type(translation), dir(type(translation)))
print(translation["extra_data"])
text = str(translation)

handle = open('output.txt', 'w')
handle.write(text)