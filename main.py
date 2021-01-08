import pyautogui
from PIL import Image
import time
import random

#Varibles
PixelSize = 50
firsttime = "1"
px = 0
py = 0

#Open the Picture
#picture = input("Path to Picture")
#image = Image.open(picture)
image = Image.open("C:/Users/9000050/OneDrive - School Town of Munster/Desktop/jo/DrawingPictures/Test.jpg")

#Get size
size = image.size
LenPic = len(size)
Lenght = size[0]
Width = size[-1]
PixelCount = Lenght * Width

#Get starting X, Y
pyautogui.alert("Move Mouse to the bottom left part of Drawing area")
startp = pyautogui.position()

#Deffing the mouse movements
def DrawingBottom(hops):
	point = 0
	pyautogui.click()
	while not point == hops:
		pyautogui.move(PixelSize, 0)
		pyautogui.click()
		point += 1
		time.sleep(.1)

def DrawingRight(hops):
	point = 0
	while not point == hops:
		pyautogui.move(0, -PixelSize)
		pyautogui.click()
		point += 1
		time.sleep(.1)

def DrawingTop(hops):
	point = 0
	while not point == hops:
		pyautogui.move(-PixelSize, 0)
		pyautogui.click()
		point += 1
		time.sleep(.1)

def DrawingLeft(hops):
	point = 0
	while not point == hops:
		pyautogui.move(0, PixelSize)
		pyautogui.click()
		point += 1
		time.sleep(.1)

def FillInVertical(Vsize):
	line = 0
	up = 1
	pyautogui.press('l')
	while line != Lenght - 1:
		pyautogui.move(PixelSize, 0)
		pyautogui.click()
		if up == 1:
			pyautogui.move(0, -PixelSize*Vsize)
			up = 0
		else:
			pyautogui.move(0, PixelSize*Vsize)
			up = 1
		pyautogui.click()
		line += 1
		time.sleep(.1)

def FillInHozantial(Lsize):
	line = 0
	up = 1
	pyautogui.press('l')
	while line != Width - 1:
		pyautogui.move(0, PixelSize)
		pyautogui.click()
		if up == 1:
			pyautogui.move(-PixelSize*Lsize, 0)
			up = 0
		else:
			pyautogui.move(PixelSize*Lsize, 0)
			up = 1
		pyautogui.click()
		line += 1
		time.sleep(.1)

def Check():
	pyautogui.click(pyautogui.locateCenterOnScreen('Check.png', confidence=0.8))

def ExtrudeShortCut():
	pyautogui.hotkey('shift','e')

def ChangeHeight():
	pyautogui.click(pyautogui.locateCenterOnScreen('Height.png', confidence=0.8))
	time.sleep(1)
	number = random.randint(0, 8)
	print(number)
	if number == 0:
		pyautogui.typewrite(".001")
	elif number == 1:
		pyautogui.typewrite(".002")
	elif number == 2:
		pyautogui.typewrite(".003")
	elif number == 3:
		pyautogui.typewrite(".004")
	elif number == 4:
		pyautogui.typewrite(".005")
	elif number == 5:
		pyautogui.typewrite(".006")
	elif number == 6:
		pyautogui.typewrite(".007")
	elif number == 7:
		pyautogui.typewrite(".008")
	elif number == 8:
		pyautogui.typewrite(".009")
	time.sleep(2)
	Check()
	time.sleep(2)

def GetPixleColor(X, Y):
	cordinate = x, y = X, Y
	color = image.getpixel(cordinate)
	color = str(color)
	red, green, blue = color.split(', ')
	red = red[1:]
	blue = blue[:-1]
	print(red)
	print(blue)
	return [red, green, blue]

def ChangeColorRed(Red):
	pyautogui.click(pyautogui.locateCenterOnScreen('Red.png', confidence=0.8))
	time.sleep(1)
	pyautogui.typewrite(Red)
	time.sleep(.2) 

def ChangeColorGreen(Green):
	pyautogui.click(pyautogui.locateCenterOnScreen('Green.png', confidence=0.9))
	time.sleep(1)
	pyautogui.typewrite(Green)
	time.sleep(.2) 

def ChangeColorBlue(Blue):
	pyautogui.click(pyautogui.locateCenterOnScreen('Blue.png', confidence=0.9))
	time.sleep(1)
	pyautogui.typewrite(Blue)
	time.sleep(.2) 

def Color(middle, CX, CY):
	pyautogui.click(pyautogui.locateCenterOnScreen('ColorAdd.png', confidence=0.8))
	time.sleep(1)
	pyautogui.click(middle)
	#CX -= 1
	#CY -= 1
	red, green, blue = GetPixleColor(CX, CY)
	ChangeColorRed(red)
	time.sleep(3)
	ChangeColorGreen(green)
	time.sleep(3)
	ChangeColorBlue(blue)
	Check()

def Extrude():
	ExtrudeShortCut()
	time.sleep(1)
	pyautogui.click()
	time.sleep(2)
	ChangeHeight()
	Check()

DrawingBottom(Lenght)
DrawingRight(Width)
DrawingTop(Lenght)
DrawingLeft(Width)
pyautogui.press('esc')
time.sleep(1)
FillInVertical(Width)
time.sleep(1)
pyautogui.press('esc')
pyautogui.move(PixelSize, 0)
FillInHozantial(Lenght)
Check()
time.sleep(2)
pyautogui.moveTo(startp) # move to bottom right
pyautogui.move(0, -PixelSize*Width) # Move to top right
pyautogui.move(PixelSize/2, PixelSize/2) # Move to the top right middle
TopRightMiddle = pyautogui.position() # Save Pos
f, Ylevel = pyautogui.position() # Save Y pos
TopRightMiddleX, TopRightMiddleY = pyautogui.position() #Save X, Y pos sep

for i in range(Width):
	for i in range(Lenght):
		currentx, currenty = pyautogui.position()
		pyautogui.moveTo(currentx, Ylevel)
		if px > 0:
			pyautogui.move(PixelSize*px, 0)
		loc = pyautogui.position()
		Extrude()
		if firsttime == "1":
			pyautogui.alert("Show Sketch")
			firsttime = "0"
		Color(loc, px, py)
		px += 1
	pyautogui.moveTo(TopRightMiddle)
	pyautogui.move(0, PixelSize)
	sfkdl, Ylevel = pyautogui.position()
	py += 1
	px = 0