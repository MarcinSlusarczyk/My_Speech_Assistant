import speech_recognition as sr
import pyttsx3 as tts
import os, sys, time

# objects
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)

# loading chrome
chrome = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
ilosc = 0
def speak(text):
	engine.say(text)
	engine.runAndWait()

def getText():
	try:
		with sr.Microphone() as source:
			
			audio = r.listen(source)
			text = r.recognize_google(audio, language="pl-PL")
			if text == "":
				return None
			else:
				return text
	except:
		return None

def czy_zawiera(string, slowa):
	return [element for element in slowa if element in string.lower()]


WYKRYJ = ['bot', 'robot', 'robocie']
DOWIDZENIA = ['dowidzenia', 'do widzenia', 'papa', 'żegnaj']
SZUKAJ = ['wyszukaj', 'szukaj', 'znajdź', 'google', 'googluj', 'pokaż']
PRZEKLENSTWA = ['kurwa', 'japierdole', 'pojebany', 'spierdalaj', 'skurwiel']


print("Aby wyjść powiedz 'Dowidzenia'")
while True:
	time.sleep(0.5)
	cur = getText()
	print(cur)
	print(" "*50, end="\r")
	if cur != None:
    	# detect words and search in google
		if len(czy_zawiera(cur, WYKRYJ)):
    		
			if len(czy_zawiera(cur, DOWIDZENIA)):
				speak("Żegnaj.")
				break
			elif len(czy_zawiera(cur, SZUKAJ)):
				linczek = cur.lower().split(' ' + czy_zawiera(cur, SZUKAJ)[0] + ' ')[1]
				speak("Oto co udało mi się znaleźć.")
				url = "https://www.google.com/search?q=" + linczek.replace(" ", "+").replace("?", "%3F")
				os.system(chrome + " " + url)
		# detect curses and warning before closing system for punishment
		if len(czy_zawiera(cur, PRZEKLENSTWA)):
				ilosc += 1 					
				if ilosc == 1:								
					speak("Jak jeszcze raz przeklniesz to wyjebie Ci z buta i wyłączę kompa")
				if ilosc == 2:
					speak("Miarka się przebrała jełopie, wyłączam kompa, papatki!")
					os.system("shutdown /s /t 1")
			
			
			
    			

