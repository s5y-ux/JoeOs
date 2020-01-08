import time
import os
import matplotlib.pyplot as plt 
import numpy as np
import random
spa = ("  ") 																						#Define Empty Lines

def los(): 																							#Double Space Effecincy in Code.
	print spa
	print spa
def bs():  																							#Tripple Space Effecincy in Code.
  print (spa)
  print (spa)
  print (spa)
time.sleep(1)
os.system('clear')
print("\033[1;31;40m Loading...")																	
print("\033[0;33;40m")
time.sleep(3) 																						#Just Checks if Script Imports work
os.system('clear')
print "Welcome To..."
time.sleep(2)
print "     _                  _       ___  ___ "
print "  _ | |___ ___ ___ _ __| |_    / _ \/ __|"
print " | || / _ (_-</ -_) '_ \ ' \  | (_) \__ \ "
print "  \__/\___/__/\___| .__/_||_|  \___/|___/"
print "                  |_|                    "
los()
print("\033[0;37;40m (Type help for a list of commands.)")

def command():																						#Command Execution function
	command_window = raw_input("\033[0;32;40m >: ")
	if command_window == 'Decimal_To_Binary':														#Base Two Conversion
		print spa
		x = int(input("Please input Decimal INT [Max - 1024]: "))
		one = (x % 2)
		two = ((x / 2) % 2)
		three = ((x / 4) % 2)
		four = ((x / 8) % 2)
		five = ((x / 16) % 2)
		six = ((x / 32) % 2)
		seven = ((x / 64) % 2)
		eight = ((x / 128) % 2)
		nine = ((x / 256) % 2)
		ten = ((x / 512) % 2)
		eleven = ((x / 1024) % 2)
		los()
		print eleven,ten,nine,eight,seven,six,five,four,three,two,one
		print spa
		simulate()
	elif command_window == 'Help':																	#Creates Help List
		los()
		los()
		print spa,   "(([  Base Operations  ]))"
		print spa
		print spa,      "* Help - prints a list of commands inside the command line"
		print spa,      "* Clear - clears the OS"
		print spa,		"* Restart - Restarts the OS"
		print spa
		print spa,   "(([   Conversions and Math   ]))"
		print spa
		print spa,      "* Decimal_To_Binary - Converts Intigers to Binary"
		print spa,		"* Binary_To_Decimal - Converts Binary to Intigers (Start the number with 0b(#))"
		print spa,      "* BMI - Calculates where you lay on the Body Mass Index"
		print spa,		"* Mob Calculator - Calculates mobs"
		print spa,		"* Test - Add two numbers for the command line maths test"
		print spa,		"* Quadratic_Equation - Solves the Quadratic Equation"
		print spa
		print spa,   "(([   OSX Base Operations   ]))"
		print spa
		print spa,		"* OSX_Say_Hi - Test command that says Hi"
		print spa,		"* OSX_Terminal - Execute OSX command line functions"
		print spa,		"* OSX_Network_Ping - Pings local area network"
		print spa,		"* OSX_Network_Status - Relays network status to the user"
		print spa,		"* OSX_Get_Subnet_Mask - Relays Subnet Mask to the user"
		print spa,		"* OSX_Get_Host_IP - Relays the Host's public IP address"
		print spa,		"* OSX_Get_Personal_IP - Relays the Host's private IP address"
		print spa,		"* OSX_Get_Basic_Network_Info - Relays network information to the user"
		print spa,		"* OSX_Launch_Minecraft - Play Minecraft!"
		print spa,		"* OSX_Launch_Discord - Chat on Discord!"
		print spa,		"* OSX_Launch_Chess - Play Chess!"
		print spa,		"* OSX_Launch_Audacity - Record some Music!"
		print spa,		"* OSX_Launch_SeaMonkey - Surf the web!"
		print spa,		"* OSX_Launch_HTML_Editor - Make some cool websites for the web!"
		print spa,		"* OSX_Launch_Arduino_Compiler - Tool Around with some robots!"
		print spa,		"* OSX_Help - Shows you a list of commands you may Execute inside the OSX Command prompt"
		print spa,		"* OSX_Launch_1.13.2_Server - Launches a 1.13.2 Minecraft server inside the OSX Command line."
		print spa
		print spa,   "(([   Linux Base Maths and Conversions   ]))"
		print spa
		print spa,		"* Music Generator - Creates a chord and note progression for a set scale"
		los()
		los()
		simulate()
	elif command_window == 'Clear':																	#Clears the Command Line
		os.system('clear')
		simulate()
	elif command_window == 'BMI':																	#BMI Calculator
		c = 1
		d = 2

		ques = int(input("Please type 1 to use the Imperial system. Or type 2 to use the Metric system: "))
		def uk():
			print(spa)
			kg = float(input("Please Enter how much you weigh (Kg's): "))
			print(spa)
			m = float(input("Please Enter how many Meters tall you are: "))
			print(spa)
			bmib = (kg / (m ** 2))
			print("Your BMI is,")
			print (bmib)
			print("And...")
			if bmib >= 30:
				print("\033[1;31;40m You are Obese!!!")
				print(spa)
				print("\033[0;32;40m")
			if bmib <= 18.5:
				print("\033[1;31;40m You are Underweight!!!")
				print(spa)
				print("\033[0;32;40m")
			if 18.5 < bmib < 24.9:
				print("\033[0;33;40m You have a healthy weight.")
				print(spa)
				print("\033[0;32;40m")
			if 25 < bmib < 30:
				print("\033[0;33;40m You are a bit Overweight...")
				print(spa)
				print("\033[0;32;40m")
				t.sleep(2)
			mapu = raw_input("Would you like to see a graph of where you stand in the chart?  [y / n]: ")
			if mapu == ('y'):
				objects = ('Your BMI', 'Underweight', 'Normal', 'Overweight', 'Obese', 'UK Avarage')
				y_pos = np.arange(len(objects))
				performance = [bmib,18.5,24.9,30,37,26.5]
				plt.bar(y_pos, performance, align='center', alpha=0.5)
				plt.xticks(y_pos, objects)
				plt.ylabel('BMI')
				plt.title('Body Mass Index')
				plt.show()
				simulate()
			if mapu == ('n'):
				los()
				simulate()

		def us():
			print (spa)
			lbs = float(input("Please Enter how much you weigh: "))
			print (spa)
			feet = int(input("Please Enter how many feet tall you are: "))
			print (spa)
			inc = int(input("Please Enter how many inches tall you are: "))
			print (spa)
			truehight = ((feet * 12) + inc)
			heightmeathod = (truehight ** 2)
			bmia = ((lbs / heightmeathod) * 703)
			bs()
			print("Your BMI is,")
			print (bmia)
			print("And...")
			print (spa)
			time.sleep(1)
			if bmia >= 30:
				print("\033[1;31;40m You are Obese!!!")
				print(spa)
				print("\033[0;32;40m")
			elif bmia <= 18.5:
				print("\033[1;31;40m You are Underweight!!!")
				print(spa)
				print("\033[0;32;40m")
			elif 18.5 < bmia < 24.9:
				print("\033[0;33;40m You have a healthy weight.")
				print(spa)
				print("\033[0;32;40m")
			elif 25 < bmia < 30:
				print("\033[0;33;40m You are a bit Overweight...")
				print(spa)
				print("\033[0;32;40m")
			time.sleep(2)
			mapu = raw_input("Would you like to see a graph of where you stand in the chart?  [y / n]: ")
			if mapu == ('y'):
				objects = ('Your BMI', 'Underweight', 'Normal', 'Overweight', 'Obese', 'US Avarage')
				y_pos = np.arange(len(objects))
				performance = [bmia,18.5,24.9,30,37,28]
				plt.bar(y_pos, performance, align='center', alpha=0.5)
				plt.xticks(y_pos, objects)
				plt.ylabel('BMI')
				plt.title('Body Mass Index')
				plt.show()
				simulate()
			if mapu == ('n'):
				simulate()
		if ques == c:
			us()
		elif ques == d:
			uk()
	elif command_window == 'Test':																		#Mathmatical Test Operation
		x = float(input("Enter the first number: "))
		y = float(input("Enter the second number: "))
		print(x + y)
		simulate()
	elif command_window == 'Restart':																	#Restarts OS
		os.system('clear')
		print("\033[0;33;40m")
		print "Welcome To..."
		time.sleep(2)
		print "     _                  _       ___  ___ "
		print "  _ | |___ ___ ___ _ __| |_    / _ \/ __|"
		print " | || / _ (_-</ -_) '_ \ ' \  | (_) \__ \ "
		print "  \__/\___/__/\___| .__/_||_|  \___/|___/"
		print "                  |_|                    "
		los()
		print("\033[0;37;40m (Type help for a list of commands.)")
		simulate()	
	elif command_window == 'Quadratic_Equation':														#Quadratic Equation ;)
		a = float(input("Please Input (a) Value: "))
		b = float(input("Please Input (b) Value: "))
		c = float(input("Please Input (c) Value: "))
		mod = ((b * b) - (4 * a * c))
		bot = (2 * a)
		fir = (-b)
		avalue = ((fir + mod) / bot)
		bvalue = ((fir - mod) / bot)
		print("X ="), avalue, ("and"), bvalue
		simulate()
	elif command_window == 'OSX_Say_Hi':																#Says Hi														 
		print (spa)
		os.system('say Hi')
		print spa
		simulate()
	elif command_window == 'OSX_Network_Ping':															#Pings Localhost
		os.system('ping localhost')
	elif command_window == 'OSX_Get_Subnet_Mask':
		print spa
		os.system('ipconfig getoption en0 subnet_mask')
		print spa
		simulate()
	elif command_window == 'OSX_Get_Host_IP':															#Returns your IP address
		print spa
		os.system('ipconfig getoption en0 domain_name_server')
		print (spa)
		simulate()
	elif command_window == 'OSX_Get_Personal_IP':														#ipv6
		print spa
		os.system('ipconfig getifaddr en0')
		print spa
		simulate()
	elif command_window == 'OSX_Get_Basic_Network_Info':												#Returns ipconfig en0
		print (spa)
		os.system('ifconfig en0')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_Minecraft':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Minecraft.app')
		print(spa)
		simulate()
	elif command_window == 'OSX_Launch_SeaMonkey':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/SeaMonkey')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_Discord':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Discord')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_Chess':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Chess')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_HTML_Editor':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Brackets.app')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_Audacity':
		print spa
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Audacity')
		print spa
		simulate()
	elif command_window == 'OSX_Launch_Arduino_Compiler':
		print(spa)
		os.system('open /Users/dirkshumaker/Desktop/Joseph\ OS/Arduino.app')
		print spa
		simulate()
	elif command_window == 'OSX_Network_Status':													#Shows you open and closed ports
		print(spa)
		os.system('netstat')
		print spa
		simulate()
	elif command_window == 'OSX_Terminal':															#Access the OSX terminal as sudo
		os.system('clear')
		print "   ___  _____  __"
		print "  / _ \/ __\ \/ /"
		print " | (_) \__ \>  < "
		print "  \___/|___/_/\_\ "
		print spa
		print("\033[0;37;40m You have now entered the OSX command line!")
		print spa
		os.system('sudo -s')
		simulate()
	elif command_window == 'OSX_Help':																#All of the terminal commands
		f=open("OSX.txt", "r")
		if f.mode == 'r':
			contents = f.read()
			print(contents)
		simulate()
	elif command_window == 'Binary_To_Decimal':														#0b number
		print spa
		x = int(input("Enter Binary Number: "))
		print x
		los()
		simulate()
	elif command_window == 'OSX_Launch_1.13.2_Server':
		print spa
		os.system('cd /Users/dirkshumaker/Desktop/Joseph\ OS')
		os.system('perl launch.pl')
		simulate()
	elif command_window == 'Mob Calculator':														#Calculate Mobs
		walk = float(3)
		Bike = float(11.5)
		Car = float(30)
		Unicycle = float(5)
		Hoverboard = float(13)
		Running = float(8.3)
		Bullet_train = float(200)
		F_Bullet_train = float(375)
		Plane = float(550)
		Skateboard = float(10)
		Rocket = float(294)
		Land_Speed_Record = float(763.035)
		Swim = float(3.7)
		x = raw_input("Enter the mode of transportation: ")
		if x == ("Walking"):
			inn = walk
		elif x == ("Biking"):
			inn = Bike
		elif x == ("Driving"):
			inn = Car
		elif x == ("Unicycle"):
			inn = Unicycle
		elif x == ("Hoverboard"):
			inn = Hoverboard
		elif x == ("Running"):
			inn = Running
		elif x == ("Bullet Train"):
			inn = Bullet_train
		elif x == ("Worlds Fastest Bullet Train"):
			inn = F_Bullet_train
		elif x == ("Flying"):
			inn = Plane
		elif x == ("Skating"):
			inn = Skateboard
		elif x == ("Rocket"):
			inn = Rocket
		elif x == ("Land Speed Record"):
			inn = Land_Speed_Record
		elif x == ("Swimming"):
			inn = Swim
		mob = float((inn / 60) * 20)
		mobdistance = (mob * 5)
		if inn == walk:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person walks at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Bike:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person bikes at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Car:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person drives at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Unicycle:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person unicycles at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Hoverboard:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person hovers at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Running:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person runs at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Bullet_train:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person rides at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == F_Bullet_train:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The fastest person rides at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Plane:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person flys at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Skateboard:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person skates at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Rocket:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage astronaut flys at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Land_Speed_Record:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The fastest land mobber travels at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
		elif inn == Swim:
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			print("\033[0;33;40m")
			print "The avarage person swims at", mob, "miles per mob."
			print(spa)
			print "If you were to travel 5 mobs... you would travel", mobdistance, "Miles"
			print(spa)
			print("\033[0;32;40m")
			print("(*)")
			print(spa)
			simulate()
	elif command_window == 'Music Generator':
		x = raw_input("Enter Scale: ")

		if x == 'cmaj':																					#C Major Chords
			melodycmaj = ['C', 'D', 'E', 'F', 'A', 'B']
			cmaj = ['C', 'D', 'E', 'F', 'A', 'B']
			cmajrand_item = cmaj[random.randrange(len(cmaj))]
			cmajrand_item1 = cmaj[random.randrange(len(cmaj))]
			cmajrand_item2 = cmaj[random.randrange(len(cmaj))]
			cmajrand_item3 = cmaj[random.randrange(len(cmaj))]
			cmajnote = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote1 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote2 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote3 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote4 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote5 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote6 = melodycmaj[random.randrange(len(melodycmaj))]
			cmajnote7 = melodycmaj[random.randrange(len(melodycmaj))]
			print("\033[0;37;40m ==========")
			print "  "
			print("\033[0;33;40m Chord Progression (*)")
			print cmajrand_item, "Major Chord"
			print cmajrand_item1, "Major Chord"
			print cmajrand_item2, "Major Chord"
			print cmajrand_item3, "Major Chord"
			print "  "
			print("\033[0;37;40m ==========")
			print "  "
			print("\033[0;32;40m Melody (*)")
			print cmajnote
			print cmajnote1
			print cmajnote2
			print cmajnote3
			print cmajnote4
			print cmajnote5
			print cmajnote6
			print cmajnote7
			print "  "
			print("\033[0;37;40m ==========")
			simulate()
		elif x == 'cminor':																				#C Minor Chords
			cminorchord = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb',]
			cminornote = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb',]
			cminorchord1 = cminorchord[random.randrange(len(cminorchord))]
			cminorchord2 = cminorchord[random.randrange(len(cminorchord))]
			cminorchord3 = cminorchord[random.randrange(len(cminorchord))]
			cminorchord4 = cminorchord[random.randrange(len(cminorchord))]
			cminornote1 = cminornote[random.randrange(len(cminornote))]
			cminornote2 = cminornote[random.randrange(len(cminornote))]
			cminornote3 = cminornote[random.randrange(len(cminornote))]
			cminornote4 = cminornote[random.randrange(len(cminornote))]
			cminornote5 = cminornote[random.randrange(len(cminornote))]
			cminornote6 = cminornote[random.randrange(len(cminornote))]
			cminornote7 = cminornote[random.randrange(len(cminornote))]
			cminornote8 = cminornote[random.randrange(len(cminornote))]
			print("\033[0;37;40m ==========")
			print "  "
			print("\033[0;33;40m Chord Progression (*)")
			print cminorchord1, "Minor Chord"
			print cminorchord2, "Minor Chord"
			print cminorchord3, "Minor Chord"
			print cminorchord4, "Minor Chord"
			print "  "
			print("\033[0;37;40m ==========")
			print "  "
			print("\033[0;32;40m Melody (*)")
			print cminornote1
			print cminornote2
			print cminornote3
			print cminornote4
			print cminornote5
			print cminornote6
			print cminornote7
			print cminornote8
			print "  "
			print("\033[0;37;40m ==========")
			simulate()
		
def simulate():
	command()

command()
