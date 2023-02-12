import phonetic
import graphic

word_phonetic = phonetic.generatePhoneticDict("lyric.txt")
graphic.generatePDF(word_phonetic)
