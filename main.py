import phonetic
import graphic

print(phonetic.wordToPhoneticSymbol("yesterday"))
word_phonetic = phonetic.generatePhoneticDict("test.txt")
print(word_phonetic)

graphic.generateImage(word_phonetic)
