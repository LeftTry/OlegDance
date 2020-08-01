import speech_recognition as sr
import os
import sys
import webbrowser
import random

def command():
	zadanie = ""
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		try: 
			zadanie = r.recognize_google(audio, language="ru-RU").lower()
			print("Вы сказали: " + zadanie)
		except sr.UnknownValueError:
			print("Я вас не поняло")
			zadanie = command()

	return zadanie

def makeSomething(zadanie):
	if 'олег' in zadanie:

		if "прощай" in zadanie or "стоп" or "Пока" in zadanie or "Остановись" in zadanie:
			print("Да, конечно, без проблем")        
			sys.exit()
			return 1

		if 'имя' in zadanie or 'как тебя зовут' in zadanie or'зовут тебя как'in zadanie or' как звать тебя'in zadanie or' назови свое имя' in zadanie or'назовись'  in zadanie:
			print("Меня зовут Олег")
			return 1

		if 'открой' in zadanie:
			if 'вк' in zadanie or "vk"  in zadanie:
				urlVK = "https://vk.com/feed"
				webbrowser.open(urlVK)
			elif "youtube" in zadanie or "ютуб" in zadanie:
				Rolic = ["Tenserflow for 12 hours", "C++ course", "Java part 1", "javascript курс"]
				print("Я надеюсь ты сейчас будешь смотреть ролик" + Rolic[random])
				urlYou = "https://www.youtube.com"
				webbrowser.open(urlYou)
			elif "хабар" in zadanie or "хабр"in zadanie or "habr" in zadanie or "лабр"  in zadanie:
				urlHabr = "https://habr.com/ru/"
				webbrowser.open(urlHabr)
			else:
				print("чего тебе открыть надо? Лучше рот открой свой и внятно скажи.")

		
		


		else:
			print("чё?")
			return 1
while True:
	makeSomething(command())