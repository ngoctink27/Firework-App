import pygame
import time
import math
import random
import os

pygame.init()


WEIGHT = 1000
HEIGHT = 600
global allscreen
allscreen = False


screen = pygame.display.set_mode((WEIGHT,HEIGHT))
w, h = pygame.display.get_surface().get_size()
def CreatScreen():
	global screen, w, h
	if allscreen == False:
		screen = pygame.display.set_mode((WEIGHT,HEIGHT))
		pygame.display.toggle_fullscreen()
	else:
		screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
	w, h = pygame.display.get_surface().get_size()

# CreatScreen()	

pygame.display.set_caption("Yolo_pp!")

icon = pygame.image.load("icon2.jpg")
pygame.display.set_icon(icon)

# Add images
def AddImg():
	global img, background
	img = []
	path = "./img"
	FJoin = os.path.join
	files = [FJoin(path, f) for f in os.listdir(os.path.expanduser(path))]
	for i in range(len(files)):
		img.append(pygame.image.load(files[i]))
	background = []
	for i in range(len(img)):
		u = img[i].get_width()
		v = img[i].get_height()
		if u <= v:
			scale_y = h/v
			u = int(scale_y*u)
			v = h
			background.append(pygame.transform.scale(img[i],(u,v)))
		else:
			background.append(pygame.transform.scale(img[i],(w,h)))

# Add music
def AddMusic():
	global music
	music = []
	path = "./music"
	FJoin = os.path.join
	files = [FJoin(path, f) for f in os.listdir(os.path.expanduser(path))]
	for i in range(len(files)):
		music.append(files[i])

AddImg()
AddMusic()

# COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)

YELLOW_1 = (255,250,179)
YELLOW_2 = (254,248,134)
YELLOW_3 = (252,245,76)
YELLOW_4 = (249,244,0)
YELLOW_5 = (220,216,0)

ORANGE = (236,135,14)

RED_1 = (255,0,0)
RED_2 = (223,0,41)
RED_3 = (238,124,107)

GREEN_1 = (131,199,93)
GREEN_2 = (200,226,177)
GREEN_3 = (152,208,185)

PINK = (229,70,70)
BLUEWHITE = (0,166,173)
BLUE = (66,110,180)
BLUE_2 = (148,170,214)
BLUE_3 = (93,12,123)

PURPLE_1 = (162,0,124)
PURPLE_2 = (210,166,199)
PURPLE_3 = (143,0,109)
PURPLE_4 = (120,0,98)

GREY_1 = (183,183,183)
GREY_2 = (112,112,112)

star_colors = ((255,255,255))

colors = (WHITE, YELLOW_1, YELLOW_2, YELLOW_3, YELLOW_4, YELLOW_5,
			RED_1, RED_2, RED_3, GREEN_1, GREEN_2, GREEN_3,
			PINK, BLUEWHITE, BLUE, GREY_1, GREY_2,
			PURPLE_1, PURPLE_2, PURPLE_3, PURPLE_4,
			ORANGE,BLUE_3,BLUE_2)

#........
rad = math.pi/180
maxout = 70 # So luong dan toi da no ra
maxSize = 7 # Kich thuoc toi da
minSize = 3
maxSpeed = 5 # Toc do toi da
minSpeed = 3
maxSpeedup = 9 # Toc do toi da trc khi no
minSpeedup = 7
A = 1.5 # Gia toc roi

# Nhung cham theo sau vien dan
class Dot():
	def __init__(self, x, y, color, size, speed,balloon):
		self.x = x
		self.y = y
		self.color = color
		self.size = size
		self.speed = speed
		self.balloon = balloon

	def draw(self):
		if self.balloon == 0:
			pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))
		else:
			if self.balloon == 1:
				pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size),1)
			else:
				pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size),2)

	def update(self):
		if self.size > 0:
			self.size -=0.2
		else:
			self.size = 0

class Effects_1():
	def __init__(self):
		self.x = random.randint(0,100)
		self.y = random.randint(int(h/5*1.2),int(h/5*2.3))
		self.speed = random.randint(4, 6)
		self.dot = [] # Nhung cham theo sau balloon
		self.itcolor = random.randint(0,len(colors)-1)
		self.color = colors[self.itcolor]
		self.size = (h/600)*random.randint(minSize, maxSize-1)
		self.angle = random.randint(0,10)		

	def update(self):
		self.dot.append(Dot(self.x,self.y,self.color,self.size,self.speed,2))
		self.x = self.x + math.cos(self.angle * rad)*self.speed
		self.y = self.y - math.sin(self.angle * rad)*self.speed
		self.speed -=A*0.001

		for i in range(len(self.dot)):
			self.dot[i].update()

		i=0
		while i<len(self.dot):
			if self.dot[i].size<=0:
				self.dot.pop(i)
			else:
				i+=1

	def draw(self):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

		i=0
		while(i<len(self.dot)):
			self.dot[i].draw()
			i+=1


class Meteors():
	def __init__(self,balloon):
		self.balloon = balloon
		self.x = random.randint(50,w-50)
		self.y = random.randint(0,100)
		self.speed = random.randint(minSpeedup, maxSpeedup+1)
		self.dot = [] # Nhung cham theo sau vien dan
		self.itcolor = random.randint(0,len(star_colors)-1)
		self.color = WHITE
		self.size = random.randint(minSize, maxSize-3)
		self.angle = random.randint(350,358) 

	def update(self):
		self.dot.append(Dot(self.x,self.y,self.color,self.size,self.speed,self.balloon))
		self.x = self.x + math.cos(self.angle * rad)*self.speed
		self.y = self.y - math.sin(self.angle * rad)*self.speed
		self.speed -=A*0.005

		for i in range(len(self.dot)):
			self.dot[i].update()
		i=0
		while i<len(self.dot):
			if(self.dot[i].x>=w):
				self.dot.pop(i)
			else:
				i+=1

	def draw(self):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

		#Ve nhung vien duoi cua balloon
		i=0
		while(i<len(self.dot)):
			self.dot[i].draw()
			i+=1

# Phao hoa bay Xien
class Fly_Oblique():
	def __init__(self, balloon):
		self.balloon = balloon
		self.x = random.randint(50,w-50)
		self.y = random.randint(270,400)
		self.speed = random.randint(minSpeedup, maxSpeedup+1)
		self.dot = [] # Nhung cham theo sau vien dan
		self.itcolor = random.randint(0,len(colors)-1)
		self.color = colors[self.itcolor]
		self.size = random.randint(minSize, maxSize)
		self.angle = random.randint(50,131)		

	def update(self):
		self.dot.append(Dot(self.x,self.y,self.color,self.size,self.speed,self.balloon))
		self.x = self.x - math.cos(self.angle * rad)*self.speed
		self.y = self.y - math.sin(self.angle * rad)*self.speed
		self.speed -=A*0.15

		for i in range(len(self.dot)):
			self.dot[i].update()

		i=0
		while i<len(self.dot):
			if self.dot[i].size<=0:
				self.dot.pop(i)
			else:
				i+=1

	def draw(self):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

		i=0
		while(i<len(self.dot)):
			self.dot[i].draw()
			i+=1

# Bay len truoc khi no
class FlyUp():
	def __init__(self,balloon):
		self.balloon = balloon
		self.x = random.randint(50,w-50)
		self.y = random.randint(370,600)
		self.speed = random.randint(minSpeedup, maxSpeedup+1)
		self.dot = [] # Nhung cham theo sau vien dan
		self.itcolor = random.randint(0,len(colors)-1)
		self.color = colors[self.itcolor]
		self.size = random.randint(minSize, maxSize)
		self.ybroke = random.randint(100,350) 

	def update(self):
		self.dot.append(Dot(self.x,self.y,self.color,self.size,self.speed,self.balloon))
		self.y-=self.speed
		self.speed -= A*0.1

		for i in range(len(self.dot)):
			self.dot[i].update()
			# time.sleep(0.0002)
		i=0
		while i<len(self.dot):
			if(self.dot[i].size<=0):
				self.dot.pop(i)
			else:
				i+=1

	def draw(self):
		# if self.y>self.ybroke:
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))
		# time.sleep(0.005)

		#Ve nhung vien duoi cua dan
		i=0
		while(i<len(self.dot)):
			self.dot[i].draw()
			i+=1

# Vien dan sau no
class Bullets():
	def __init__(self,x,y,speed,angle,color,color_broke,balloon):
		tmp = random.randint(0,len(colors)-1)
		self.balloon = balloon
		self.x = x
		self.y = y
		self.color_broke = color_broke

		if color_broke == 1:
			self.color = color
		else:
			self.color = colors[tmp]
		self.speed = speed
		self.angle = angle
		sz = 1
		if self.balloon == 1:
			sz = h/600
		self.size = 4*sz

	def update(self):
		# Thay doi vi tri
		self.x += self.speed*math.cos(self.angle*rad)
		self.y += self.speed*-math.sin(self.angle*rad)+A

		# Giam size
		if self.size>0:
			self.size -= 0.05
		else:
			self.size=0

		# Giam toc do
		if self.speed>0:
			self.speed -= 0.07
		else:
			self.speed=0

	def draw(self):
		if(self.size>0):
			pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size)

# Phao hoa no
class Broke():
	def __init__(self,x, y, color_broke,balloon):
		self.balloon = balloon
		self.out = random.randint(20, maxout)
		self.x = x
		self.y = y
		self.dot = [] # cac vien dan theo sau
		self.color_broke = color_broke


		def creatbullet(): # tao list cac vien dan
			bullet = []
			color = colors[random.randint(0,len(colors)-1)]
			for i in range(self.out):
				angle = (360/self.out) * i
				speed = random.randint(minSpeed,maxSpeed+1)
				bullet.append(Bullets(self.x,self.y,speed,angle,color, self.color_broke,self.balloon))
			return bullet
		self.bullet = creatbullet();

	def update(self):
		for i in range(len(self.bullet)): # update cac vien dan
			self.bullet[i].update()
			self.dot.append(Dot(self.bullet[i].x,self.bullet[i].y,
				self.bullet[i].color,self.bullet[i].size,self.bullet[i].speed, self.balloon))

		for i in range(len(self.dot)):
			self.dot[i].update()

		i=0
		while i<len(self.dot): # Xoa nhung cham kich thuoc <=0
			if self.dot[i].size<=0:
				self.dot.pop(i)
			else: 
				i+=1

	def draw(self):
		for i in range(len(self.bullet)):
			self.bullet[i].draw()

		for i in range(len(self.dot)):
			self.dot[i].draw()



bullet = []
firework = []
effect_1 = []

global fpsclock
fpsclock = pygame.time.Clock()
time=50
jpg=0

star_music = False
pause_music = 0
id_music = len(music)
next_music = 0
pre_music = 0
pause_firework = False
color_broke = 0
level = 0
effect = False
next_pic = 0
balloon = 0


running = True

while running:
	screen.fill(BLACK)
	
	u = background[jpg].get_width()
	v = background[jpg].get_height()
	if u<=v:
		screen.blit(background[jpg], (int(w-u)/2,0))
	else:
		screen.blit(background[jpg], (0,0))

	mouse_x, mouse_y = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# Setup Mouse
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				jpg = (jpg+1)%len(img)
				next_pic = 1
			else:
				if event.button == 3:
					star_music = True
					next_music = 1
					pre_music = 0
				if event.button == 2:
					pause_music = (pause_music+1)%4

		# Setup Key for Musics and Jmages
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_F11:
				allscreen ^=1
				CreatScreen()
				AddImg()
			if event.key == pygame.K_LEFT:
				jpg = (jpg-1)%len(img)
			if event.key == pygame.K_RIGHT:
				jpg = (jpg+1)%len(img)
				next_pic = 1
			if event.key == pygame.K_UP:
				star_music = True
				next_music = 1
				pre_music = 0
			if event.key == pygame.K_DOWN:
				star_music = True
				next_music = 0
				pre_music = -1
			if event.key == pygame.K_SPACE:
				# pause_firework ^=1
				color_broke = (color_broke+1)%3
			if event.key == pygame.K_e:
				effect ^=1
			if event.key == pygame.K_b:
				balloon = (balloon+1)%2

	# Start Music
	if star_music == True or (pygame.mixer.music.get_busy()==False and (pause_music==0)):
		id_music = (id_music + next_music + pre_music)%len(music)
		pygame.mixer.music.load(music[id_music])
		pygame.mixer.music.play()
		star_music = False

	# Pause Music = on or off
	if pause_music == 1:
		pygame.mixer.music.pause()
		pause_music = (pause_music+1)%4

	if pause_music == 3:
		pygame.mixer.music.unpause()
		pause_music = (pause_music+1)%4

	#....................
	# Fight
	if time==50:

		ran_1 = random.randint(0,2)
		ran_2 = random.randint(0,2)
		ran_3 = random.randint(0,1)

		if color_broke !=0:
			for i in range(ran_1):
				bullet.append(FlyUp(balloon))

			for i in range(ran_2):
				bullet.append(Fly_Oblique(balloon))

		for i in range(ran_3):
			bullet.append(Meteors(balloon))

	for i in range(len(bullet)):
		bullet[i].draw()
		bullet[i].update()

	for i in range(len(firework)):
		firework[i].draw()
		firework[i].update()
	i=0
	while i<len(bullet):
		if bullet[i].speed<=0:
			# Tao no o do cao toi da
			firework.append(Broke(bullet[i].x, bullet[i].y, color_broke, balloon))
			bullet.pop(i)
		else: 
			i+=1

	i=0
	while i<len(firework):
		if firework[i].bullet[0].size<=0:
			firework.pop(i)
		else:
			i+=1

	# Hieu ung
	if effect:
		for i in range(1):
			if len(effect_1) <7:
				effect_1.append(Effects_1())
		for i in range(len(effect_1)):
			effect_1[i].draw()
			effect_1[i].update()

		'''if effect_1[0].speed<=0 or effect_1[0].x>=w:
			effect = False
			while len(effect_1)>0:
				effect_1.pop(0)
		else:'''
		i=0
		while i<len(effect_1):
			if effect_1[i].speed<=0 or effect_1[i].x>=w:
				effect_1.pop(i)
			else:
				i+=1


	# Timelate
	if time<=50:
		time+=1
	else:
		time=0

	pygame.display.update()
	fpsclock.tick(60)

pygame.quit()
