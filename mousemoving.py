import time 
import pyautogui as gui

def moveCursor(x, y):
	int a = 20, b = 20
	currentMouseX, currentMouseY = gui.position()
	while currentMouseX != x and currentMouseY != y:
		print("yes")
		currentMouseX, currentMouseY = gui.position()
		gui.moveTo(currentMouseX + a, currentMouseY + b, 2)  
		if(currentMouseX == x)
			a = 0
		if(currentMouseY == y)
			b = 0
