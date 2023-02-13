from PIL import Image, ImageDraw, ImageFont
import img2pdf

HEIGHT = 2970
WIDTH = 2100
TITLESIZE = 120
WORDSIZE = 60
PHONETICSIZE = 40
NUMBERSIZE = 30
TITLEMARGIN = 250
TOPMARGIN = 200
BOTTOMMARGIN = 200
SIDEMARGIN = 100
COLUMNMARGIN_TOP = 10
COLUMNMARGIN_MIDDLE = 30
COLUMNMARGIN_BOTTOM = 50
WORDMARGIN = 50
PHONETICMARGIN = 50
NEWLINEMARGIN = 100
TITLEFONT = ImageFont.truetype(
    '/mnt/c/Windows/Fonts/HelveticaNeue-Light-08.ttf', TITLESIZE)
WORDFONT = ImageFont.truetype(
    '/mnt/c/Windows/Fonts/HelveticaNeue-Light-08.ttf', WORDSIZE)
PHONETICFONT = ImageFont.truetype(
    '/mnt/c/Windows/Fonts/l_10646.ttf', PHONETICSIZE)
NUMBERFONT = ImageFont.truetype(
    '/mnt/c/Windows/Fonts/HelveticaNeue-Light-08.ttf', NUMBERSIZE)
PAGECOUNT = 1
WORDINDEX = 0
backgroundfile = 'data/background.png'
title = 'Something'


def generateImage(wordList):
    global WORDINDEX
    global PAGECOUNT
    img = Image.open(backgroundfile)
    draw = ImageDraw.Draw(img)

    # draw title
    if PAGECOUNT == 1:
        draw.text((WIDTH/2, TITLEMARGIN/2), title,
                  '#000000', font=TITLEFONT, anchor='mm')

    # draw page number
    draw.text((WIDTH/2, HEIGHT - BOTTOMMARGIN/2), str(PAGECOUNT),
              '#000000', font=NUMBERFONT, anchor='mm')

    # draw word and phonetic symbol
    wordAnchor_X = SIDEMARGIN
    if PAGECOUNT == 1:
        wordAnchor_Y = TITLEMARGIN + COLUMNMARGIN_TOP + WORDMARGIN/2
    else:
        wordAnchor_Y = TOPMARGIN + COLUMNMARGIN_TOP + WORDMARGIN/2
    phoneticAnchor_X = wordAnchor_X
    phoneticAnchor_Y = wordAnchor_Y + COLUMNMARGIN_MIDDLE + PHONETICMARGIN/2
    # for word in wordList:
    while True:
        # draw word
        if WORDINDEX == len(wordList):
            break
        if wordList[WORDINDEX][0] == '\n':
            wordAnchor_X = SIDEMARGIN
            if wordList[WORDINDEX-1][0] == '\n':
                wordAnchor_Y += NEWLINEMARGIN
            else:
                wordAnchor_Y += WORDMARGIN + COLUMNMARGIN_MIDDLE + \
                    PHONETICMARGIN + COLUMNMARGIN_BOTTOM + COLUMNMARGIN_TOP
            phoneticAnchor_X = wordAnchor_X
            phoneticAnchor_Y = wordAnchor_Y + COLUMNMARGIN_MIDDLE + PHONETICMARGIN/2
        else:
            wordBbox = draw.textbbox((wordAnchor_X, wordAnchor_Y), wordList[WORDINDEX][0] + '    ',
                                     font=WORDFONT, anchor='lm')
            if wordBbox[1] > HEIGHT - BOTTOMMARGIN:  # stick out to the bottom
                break
            if wordBbox[2] > WIDTH - SIDEMARGIN:  # stick out to the right
                wordAnchor_X = SIDEMARGIN
                wordAnchor_Y += WORDMARGIN + COLUMNMARGIN_MIDDLE + \
                    PHONETICMARGIN + COLUMNMARGIN_BOTTOM + COLUMNMARGIN_TOP
                wordBbox = draw.textbbox((wordAnchor_X, wordAnchor_Y), wordList[WORDINDEX][0] + '    ',
                                         font=WORDFONT, anchor='lm')
                phoneticAnchor_X = wordAnchor_X
                phoneticAnchor_Y = wordAnchor_Y + COLUMNMARGIN_MIDDLE + PHONETICMARGIN/2
            draw.text((wordAnchor_X, wordAnchor_Y), wordList[WORDINDEX][0] + ' ', '#000000',
                      font=WORDFONT, anchor='lm')
            wordAnchor_X = wordBbox[2]
            # draw phonetic symbol
            phoneticBbox = draw.textbbox((phoneticAnchor_X, phoneticAnchor_Y), wordList[WORDINDEX][1] + '    ',
                                         font=PHONETICFONT, anchor='lm')
            draw.text((phoneticAnchor_X, phoneticAnchor_Y), wordList[WORDINDEX][1], '#888888',
                      font=PHONETICFONT, anchor='lm')
            phoneticAnchor_X = wordAnchor_X
        WORDINDEX += 1
    img.save('data/output' + str(PAGECOUNT) + '.png')
    PAGECOUNT += 1


def generatePDF(wordList):
    while True:
        if len(wordList) == WORDINDEX:
            break
        generateImage(wordList)

    PDFFileName = 'data/output.pdf'
    imageList = []
    for i in range(1, PAGECOUNT, 1):
        imageName = 'data/output' + str(i) + '.png'
        imageList.append(imageName)
    with open(PDFFileName, "wb") as f:
        f.write(img2pdf.convert(imageList))
