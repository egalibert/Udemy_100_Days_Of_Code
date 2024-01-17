import pyautogui
from PIL import Image, ImageGrab
import time


def space_bar_press():
	pyautogui.press("space")
	# return


def stay():
	f = False
	if not f:
		up_press()
	return f


def up_press():
	# time.sleep(1)
	pyautogui.press("up")
	return


def down_press():
	pyautogui.press("down")
	return


pyautogui.moveTo(1080, 1080, 2)
pyautogui.click()
space_bar_press()


while True:
	image = ImageGrab.grab().convert('L')
	data = image.load()

	# Draw the rectangle for cactus
	for i in range(329, 428):
		for j in range(637, 660):
			if data[i, j] < 255:
				up_press()
				time.sleep(0.001)
				break
