from tkinter import *
from tkinter import ttk
from selenium import webdriver
import bangla
from datetime import date

# tkinter window
root = Tk()
root.title('What is today')

#create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

#create another frome inside the canvas
second_frame = Frame(my_canvas)

#add that new frame to the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

path = 'chromedriver.exe'

download_fp = './testPrismaDownload/'
prefs = {
    "download.prompt_for_download" : False,
    "download.default_directory": download_fp
}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(options=options, desired_capabilities=options.to_capabilities(), executable_path=path)

month = {
	'January': 'জানুয়ারি',
	'February': 'ফেব্রুয়ারি',
	'March': 'মার্চ',
	'April': 'এপ্রিল',
	'May': 'মে',
	'June': 'জুন',
	'July': 'জুলাই',
	'August': 'আগস্ট',
	'September': 'সেপ্টেম্বর',
	'October': 'অক্টোবর',
	'November': 'নভেম্বর',
	'December': 'ডিসেম্বর',
}

today = date.today()

todayDate = today.strftime('%d')
todayDateBangla = bangla.convert_english_digit_to_bangla_digit(todayDate)
todayMonth = today.strftime('%B')
todayYear = today.strftime('%Y')
todayYearBangla = bangla.convert_english_digit_to_bangla_digit(todayYear)

url = 'https://bn.wikipedia.org/wiki/' + todayDateBangla + '_' + month[todayMonth]

browser.get(url)

#App start
lineNo = 1
#row 0
heading = Label(second_frame, text="আজ " + todayDateBangla + ' ' + month[todayMonth] + ',' + todayYearBangla, font=("Helvetica", 28))
heading.pack(padx=10, pady=10)

#row 2
happedHeading = Label(second_frame, text="ঘটনাবলীঃ")
happedHeading.pack(ipadx=10, ipady=10, padx=10, pady=10)
lineNo += 1

#happend today
happendLi = browser.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li')

for i in range(1, len(happendLi)+1):
	happend = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li[' + str(i) + ']').text
	happendPrint = Label(second_frame, text=happend)
	happendPrint.pack()
	lineNo += 1

#row 2
bornHeading = Label(second_frame, text="জন্মঃ")
bornHeading.pack(ipadx=10, ipady=10, padx=10, pady=10)
lineNo += 1

#born today
bornLi = browser.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[2]/li')

for i in range(1, len(bornLi)+1):
	born = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[2]/li[' + str(i) + ']').text
	bornPrint = Label(second_frame, text=born)
	bornPrint.pack()
	lineNo += 1

#row 3
diedHeading = Label(second_frame, text="মৃত্যুঃ")
diedHeading.pack(ipadx=10, ipady=10, padx=10, pady=10)

#died today
diedLi = browser.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[3]/li')

for i in range(1, len(diedLi)+1):
	died = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[3]/li[' + str(i) + ']').text
	diedPrint = Label(second_frame, text=died)
	diedPrint.pack()
	lineNo += 1

browser.close()
root.mainloop()