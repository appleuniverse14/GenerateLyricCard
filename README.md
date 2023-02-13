# GenerateLyricCard
### Purpose
- for English Learners
- This program is inspired by "Parrot's Law" from the book called "Eigomimi"(in Japanese: 「英語耳」, in English: "English Ear").
- This program generate lyric card with phonetic symbols from text file of lyric to PDF file.
### Specification
- what you need
    - Python3
    - Necassary PyPI libraries
        - requests
        - BeautifulSoup
        - PIL
        - img2pdf
### Usage
- Write lyric of your favorite song to 'data/lyric.txt'
- Save background image(A4 size) to 'data/background.png'
    - In this repository, 'data/background.png' is an A4(2100px x 2970px) white image as a example
- Execute the following command: `python3 main.py`
### Structure
- main.py
    - Main process
- phonetic.py
    - Text and phonetic process
        - Get phonetic symbols from the Internet(https://dictionary.cambridge.org/us/dictionary/english/)
- graphic.py
    - Make image of lyric and phonetic symbol
    - Combine images into a PDF file