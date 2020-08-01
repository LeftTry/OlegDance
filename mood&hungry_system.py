import os

mood = 0
hungriness = 1
def moodbehavior(mood):
	if(mood <= -2):
		#отказ что-либо делать, рандомные звуки криков
		os.system("start scream2.mp3")
		os.system("start scream1.mp3")
		os.system("start scream3.mp3")
		os.system("start Violence_scream.mp3")
	if(mood >= 2)
		#отказ что-либо делать, не говорит, спит
def hungrysys(vegeterian_food, non_vegeterian_food):
	hungriness = vegeterian_food * 0,05 + non_vegeterian_food * 0,1
	mood = vegeterian_food * 0,2 - non_vegeterian_food * 0,25
	if(hungriness == 0)
		#spamterminals

