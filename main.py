import phonetic
import graphic

lyricfile = "data/lyric.txt"

word_phonetic = phonetic.generatePhoneticDict(lyricfile)
graphic.generatePDF(word_phonetic)
