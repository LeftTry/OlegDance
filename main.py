import tkinter
import random
import time
from threading import Thread
import ctypes
import speech_recognition as sr
import os
import time 
import pyautogui as gui
import sys
import webbrowser
import random
from send2trash import send2trash

def hardbass():
	os.system("start HardBass.mp3")

def search(s):
	for i in range(0, len(s)):
			if s[i] == "+":
				s = s[:len(s) - i] + "%2B" + s[i:]
	url = "https://www.google.com/search?q=" + s
	webbrowser.open(url)

def find_files(filename, search_path):
	result = []
	_result = ""

	for root, dir, files in os.walk(search_path):
		if filename in files:
			result.append(os.path.join(root, filename))
	for i in result:
		_result += i
	return _result

def moveCursor(x, y):
	a = 20
	b = 20
	currentMouseX, currentMouseY = gui.position()
	while currentMouseX != x and currentMouseY != y:
		currentMouseX, currentMouseY = gui.position()
		gui.moveTo(currentMouseX + a, currentMouseY + b, 2)  
		if(currentMouseX == x):
			a = 0
		if(currentMouseY == y):
			b = 0

def walp(imagepath):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, imagepath , 0)

def spamterm():
	for i in range(0, 10):
		subprocess.call([r".\externalmoduls\spamterminals.bat"])

def wander(minT, maxT):
	time = random.randint(minT,maxT)

def command():
	zadanie = ""
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Шпрехай!")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		try: 
			zadanie = r.recognize_google(audio, language="ru-RU").lower()
			print("Ты вякнул: " + zadanie)
		except sr.UnknownValueError:
			print("Говори чётко, а не как будто у тебя во рту валенок.")
			zadanie = command()

	return zadanie

def makeSomething(zadanie):
	
	if 'олег' in zadanie:

		if 'открой' in zadanie:
			
			searches = 0

			if 'вк' in zadanie or "vk"  in zadanie:
				
				searches = 1
				url = "https://vk.com/feed"
				webbrowser.open(url)
			
			if "youtube" in zadanie or "ютуб" in zadanie:
				
				searches = 1
				Rolic = ["Tenserflow for 12 hours", "C++ course", "Java part 1", "javascript курс", "Как выжить, если ты холостяк", "Как воровать хлеб из ларька, туториал"]
				print("Я надеюсь ты сейчас будешь смотреть " +'"'+ Rolic[random.randint(0, len(Rolic))]+'"')
				url = "https://www.youtube.com"
				webbrowser.open(url)
			
			if "хабар" in zadanie or "хабр"in zadanie or "habr" in zadanie or "лабр"  in zadanie:
				
				searches = 1
				url = "https://habr.com/ru/"
				webbrowser.open(url)

			if "reddit" in zadanie or "redit"in zadanie or "редит" in zadanie or "реддит"  in zadanie:

				searches = 1
				url = "https://www.reddit.com/"
				webbrowser.open(url)

			if "github" in zadanie or "git"in zadanie or "гит" in zadanie or "гитхаб"  in zadanie:

				searches = 1
				url = "https://www.github.com/"
				webbrowser.open(url)

			if "gitlab" in zadanie or "гитлаб"  in zadanie:

				searches = 1
				url = "https://www.gitlab.com/"
				webbrowser.open(url)

			if searches == 0:

				return 1

			else:
				os.system("start Recording (2).m4a")

		elif "как" in zadanie or "зачем" in zadanie or "почему" in zadanie or "кто" in zadanie or "что" in zadanie:
			search(zadanie)
			os.system("start Recording (3).m4a")
		
		elif "поищи" in zadanie or "поиск" in zadanie or "найди" in zadanie:
			send2trash(find_files(zadanie[5:], "C:"))
			os.system("start Recording (4).m4a")

		elif "привет" in zadanie or "здраствуй" in zadanie or "здраствуйте" in zadanie or "доброе утро" in zadanie or "добрый день" in zadanie or "добрый вечер" in zadanie:
			os.system("start Recording (5).m4a")

		elif "сколько тебе лет" in zadanie or "твой возраст" in zadanie or "твой год рождения" in zadanie:
			listoffrases0 = ["start Recording (6).m4a", "start Recording (7).m4a", "start Recording (8).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases0))])

		elif "как дела" in zadanie or "как жизнь" in zadanie or "как поживаешь" in zadanie or  "как живется" in zadanie:
			listoffrases = ["start Recording (9).m4a", "start Recording (10).m4a", "start Recording (8).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases))])

		elif "где ты живешь" in zadanie or "твое место жительства" in zadanie or "твое место проживания" in zadanie:
			listoffrases1 = ["start Recording (11).m4a", "start Recording (12).m4a", "start Recording (8).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases1))])

		elif "что ты сегодня ел" in zadanie:
			listoffrases2 = ["start Recording (13).m4a", "start Recording (14).m4a", "start Recording (8).m4a", "start Recording (16).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases2))])

		elif "какая сегодня погода" in zadanie or "прогноз погоды на сегодня" in zadanie or "погода на сегодня" in zadanie:
			listoffrases3 = ["start Recording (17).m4a", "start Recording (18).m4a", "start Recording (8).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases3))])

		elif "сколько времени" in zadanie or "котрый час" in zadanie:
			listoffrases4 = ["start Recording (17).m4a", "start Recording (19).m4a", "start Recording (20).m4a"]
			os.system(listoffrases[random.randint(0, len(listoffrases4))])

		elif "прощай" in zadanie or "стоп" or "пока" in zadanie or "остановись" in zadanie or "останови приложение" in zadanie:
			
			os.system("start Recording (21).m4a")     
			sys.exit()
			
		elif 'имя' in zadanie or 'как тебя зовут' in zadanie or'зовут тебя как'in zadanie or' как звать тебя'in zadanie or 'назовись'  in zadanie:
			
			os.system("start Recording (22).m4a")

		else:
			os.system("start Recording (23).m4a")
			return 1

def moodbehavior(mood):
	
	if(mood <= -2):
		#отказ что-либо делать, рандомные звуки криков
		os.system("start scream2.mp3")
		os.system("start scream1.mp3")
		os.system("start scream3.mp3")
		os.system("start Violence_scream.mp3")
	if(mood >= 2):
		#отказ что-либо делать, не говорит, спит
		pass

def hungersys(vegeterian_food, non_vegeterian_food):
	
	hunger = vegeterian_food * 0.05 + non_vegeterian_food * 0.1
	mood = vegeterian_food * 0.2 - non_vegeterian_food * 0.25
	
	if(hunger <= -2):
		spamterm()



mood = 0
hunger = 1

root = tkinter.Tk()
root.title("_$$Oleg_Dancer$$_")

#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#= tk.PhotoImage(file='')
#root.image = tkinter.PhotoImage(file = 'Слой 1_1.gif')

#label = tkinter.Label(root, image=root.image, bg='white')
#root.overrideredirect(True)
#root.geometry("+250+250")
#root.lift()
#root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
#root.wm_attributes("-transparentcolor", "white")
#label.pack()

#label.mainloop()

while True:
	
	makeSomething(command())


	

thread1 = Thread(target = wander, args=(20, 40,))
thread2 = Thread(target = recive, args=())

thread1.start()
thread2.start()
thread1.join()
thread2.join()
