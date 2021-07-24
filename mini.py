# Importing required modules
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from pdf2image import convert_from_path
from googletrans import Translator
from gtts import gTTS
import os
import pytesseract

global filepath
root = Tk()

def openin():
	roots=Tk()
	filepath = filedialog.askopenfilename()
# Creating the frame for PDF Viewer
	pdf_frame = Frame(roots).pack(fill=BOTH,expand=1)

# Adding Scrollbar to the PDF frame
	scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)

# Adding text widget for inserting images
	pdf = Text(pdf_frame,yscrollcommand=scrol_y.set,bg="grey")

# Setting the scrollbar to the right side
	scrol_y.pack(side=RIGHT,fill=Y)
	scrol_y.config(command=pdf.yview)

# Finally packing the text widget
	pdf.pack(fill=BOTH,expand=1)

# Here the PDF is converted to list of images
	pages = convert_from_path(filepath,size=(800,900))

# Empty list for storing images
	photos = []
	transbtn = Button(root, text='Translate', command=newWindow)
	transbtn.pack(padx=5, pady=20, side=LEFT)
	ttsbtn = Button(root, text='Text To Speech', command=tts)
	ttsbtn.pack(padx=5, pady=20, side=RIGHT)

# Storing the converted images into list
	for i in range(len(pages)):
		photos.append(ImageTk.PhotoImage(pages[i]))
		global textfrompdf
		textfrompdf = str(pytesseract.image_to_string(pages[i]))
		textfrompdf = textfrompdf.replace('-\n', '')

# Adding all the images to the text widget
	for photo in photos:
		pdf.image_create(END,image=photo)
  	# For Seperating the pages
		pdf.insert(END,'\n\n')
	roots.mainloop()
# Ending of mainloop
def translation(code):
	translator = Translator()
	outfile = "out_text.txt"
	f = open(outfile, "a")
	translatedtext=translator.translate(textfrompdf,dest=code)
	with open(outfile, "w", encoding="utf-8") as f:
		f.write(str(translatedtext))
	f.close()

def tts():
	language = 'en'
	myobj = gTTS(text=textfrompdf, lang=language, slow=False)
	myobj.save("outputofpdf.mp3")
	os.system("outputofpdf.mp3")


def newWindow():  # new window definition
	LANGUAGES = {
		'af': 'afrikaans',
		'sq': 'albanian',
		'am': 'amharic',
		'ar': 'arabic',
		'hy': 'armenian',
		'az': 'azerbaijani',
		'eu': 'basque',
		'be': 'belarusian',
		'bn': 'bengali',
		'bs': 'bosnian',
		'bg': 'bulgarian',
		'ca': 'catalan',
		'ceb': 'cebuano',
		'ny': 'chichewa',
		'zh-cn': 'chinese (simplified)',
		'zh-tw': 'chinese (traditional)',
		'co': 'corsican',
		'hr': 'croatian',
		'cs': 'czech',
		'da': 'danish',
		'nl': 'dutch',
		'en': 'english',
		'eo': 'esperanto',
		'et': 'estonian',
		'tl': 'filipino',
		'fi': 'finnish',
		'fr': 'french',
		'fy': 'frisian',
		'gl': 'galician',
		'ka': 'georgian',
		'de': 'german',
		'el': 'greek',
		'gu': 'gujarati',
		'ht': 'haitian creole',
		'ha': 'hausa',
		'haw': 'hawaiian',
		'iw': 'hebrew',
		'hi': 'hindi',
		'hmn': 'hmong',
		'hu': 'hungarian',
		'is': 'icelandic',
		'ig': 'igbo',
		'id': 'indonesian',
		'ga': 'irish',
		'it': 'italian',
		'ja': 'japanese',
		'jw': 'javanese',
		'kn': 'kannada',
		'kk': 'kazakh',
		'km': 'khmer',
		'ko': 'korean',
		'ku': 'kurdish (kurmanji)',
		'ky': 'kyrgyz',
		'lo': 'lao',
		'la': 'latin',
		'lv': 'latvian',
		'lt': 'lithuanian',
		'lb': 'luxembourgish',
		'mk': 'macedonian',
		'mg': 'malagasy',
		'ms': 'malay',
		'ml': 'malayalam',
		'mt': 'maltese',
		'mi': 'maori',
		'mr': 'marathi',
		'mn': 'mongolian',
		'my': 'myanmar (burmese)',
		'ne': 'nepali',
		'no': 'norwegian',
		'ps': 'pashto',
		'fa': 'persian',
		'pl': 'polish',
		'pt': 'portuguese',
		'pa': 'punjabi',
		'ro': 'romanian',
		'ru': 'russian',
		'sm': 'samoan',
		'gd': 'scots gaelic',
		'sr': 'serbian',
		'st': 'sesotho',
		'sn': 'shona',
		'sd': 'sindhi',
		'si': 'sinhala',
		'sk': 'slovak',
		'sl': 'slovenian',
		'so': 'somali',
		'es': 'spanish',
		'su': 'sundanese',
		'sw': 'swahili',
		'sv': 'swedish',
		'tg': 'tajik',
		'ta': 'tamil',
		'te': 'telugu',
		'th': 'thai',
		'tr': 'turkish',
		'uk': 'ukrainian',
		'ur': 'urdu',
		'uz': 'uzbek',
		'vi': 'vietnamese',
		'cy': 'welsh',
		'xh': 'xhosa',
		'yi': 'yiddish',
		'yo': 'yoruba',
		'zu': 'zulu',
		'fil': 'Filipino',
		'he': 'Hebrew'
	}

	LANGCODES = dict(map(reversed, LANGUAGES.items()))

	newwin = Toplevel(root)
	newwin.title('Translation')
	droplang = StringVar()
	droplang.set("select language")
	drop = OptionMenu(newwin, droplang,*LANGCODES)
	def result():
		translation(LANGCODES[droplang.get()])
	btn = Button(newwin, text='OK',command=result)
	drop.pack()
	btn.pack()


openbtn=Button(root,text='Open',command=openin)
openbtn.pack(padx=5, pady=20, side=LEFT)

root.mainloop()

