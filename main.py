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

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def moveCursor(x, y):
	a = 20
	b = 20
	currentMouseX, currentMouseY = gui.position()
	while currentMouseX != x and currentMouseY != y:
		currentMouseX, currentMouseY = gui.position()
		gui.moveTo(currentMouseX + a, currentMouseY + b, 2)  
		if(currentMouseX == x)
			a = 0
		if(currentMouseY == y)
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
				webbrowser.open(urlVK)
			
			if "youtube" in zadanie or "ютуб" in zadanie:
				
				searches = 1
				Rolic = ["Tenserflow for 12 hours", "C++ course", "Java part 1", "javascript курс", "Как выжить, если ты холостяк", "Как воровать хлеб из ларька, туториал"]
				print("Я надеюсь ты сейчас будешь смотреть " +'"'+ Rolic[random.randint(0, len(Rolic))]+'"')
				url = "https://www.youtube.com"
				webbrowser.open(url)
			
			if "хабар" in zadanie or "хабр"in zadanie or "habr" in zadanie or "лабр"  in zadanie:
				
				searches = 1
				url = "https://habr.com/ru/"
				webbrowser.open(urlHabr)
			
			if searches == 0:

				return 1

			else:
				
				print("чего тебе открыть надо? Лучше рот открой свой и внятно скажи.")
		
		elif "прощай" in zadanie or "стоп" or "Пока" in zadanie or "Остановись" in zadanie:
			
			print("Да, конечно, без проблем")        
			sys.exit()
			
		elif 'имя' in zadanie or 'как тебя зовут' in zadanie or'зовут тебя как'in zadanie or' как звать тебя'in zadanie or 'назовись'  in zadanie:
			
			print("Меня зовут Олег, за 5 лет можно было и запомнить...")

		else:
			print("чё?")
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

def hungersys(vegeterian_food, non_vegeterian_food):
	
	hunger = vegeterian_food * 0,05 + non_vegeterian_food * 0,1
	mood = vegeterian_food * 0,2 - non_vegeterian_food * 0,25
	
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
 root.image = tk.PhotoImage(file='123')

label = tk.Label(root, image=root.image, bg='white')
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()

while True:
	
	makeSomething(command())


	

thread1 = Thread(target = wander, args=(20, 40,))
thread2 = Thread(target = recive, args=())

thread1.start()
thread2.start()
thread1.join()
thread2.join()
