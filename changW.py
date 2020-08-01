import ctypes
def walp(imagepath):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, imagepath , 0)