#Python 2.x program for Speech Recognition

import speech_recognition as sr
import threading
from threading import Thread, current_thread
import time
from multiprocessing import Process, Queue, Manager 


def Record(person):
    #enter the name of usb microphone that you found
    #using lsusb
    #mic_name = "USB PnP Sound Device"
    if (person == "doctor"):
    	mic_name = "Built-in Microphone"
    else:
    	mic_name = "Built-in Microphone"
    	#mic_name = "USB PnP Sound Device"
    #Sample rate is how often values are recorded
    sample_rate = 48000
    #Chunk is like a buffer, stores 2048 samples (bytes of data)
    #Advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048

    #generate a list of all audio cards/microphones
    mic_list = sr.Microphone.list_microphone_names()

    #the following loop aims to set the device ID of the mic that
    #we specifically want to use to avoid ambiguity.
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i
            #print(device_id)

    #use the microphone as source for input. Here, we also specify
    #which device ID to specifically look for incase the microphone
    #is not working, an error will pop up saying "device_id undefined"
	with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
		recog.adjust_for_ambient_noise(source)
		recog.pause_threshold = 0.5
		while 1:
            #energy threshold based on the surrounding noise level
			print person + " Please Say Something"
            #listens for the user's input
			audio = recog.listen(source)
            #print "Record finish, processing"
			t_recog = threading.Thread(target = Recogize, name = person, args = (audio,))
			t_recog.start()

def Recogize(audio):
	person = current_thread().getName()
	try:
		index = queue_index.get()
		queue_index.put(index+1)
		text = recog.recognize_google(audio)
		# to prevent strange "u'somestring'" in print
		text = text.encode("utf8")
		queue_sentence.put({index: person + ": " + text})
	#error occurs when google could not understand what was said     
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")    
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

def Classify(text):
	#classify interface
	return 1

def OutputSingle():
	pick = queue_sentence.get()
	# add to whole dictionary
	whole_para.update(pick)
	# send to text classification
	Classify(pick)
	print pick
	if "quit" in pick.values()[0]:
		p_doctor.terminate()
		p_patient.terminate()
		return 1
	return 0

def OutputWhole(whole_para):
	return sorted(whole_para.values())

if __name__ == '__main__':
	whole_para = {}
	recog = sr.Recognizer()
	queue_sentence = Manager().Queue()
	queue_index = Queue()
	queue_index.put(1)
	p_doctor = Process(target = Record, args=("doctor",))
	p_patient = Process(target = Record, args=("patient",))
	p_patient.start()
	p_doctor.start()
	quit_flag = 0
	while(not quit_flag):
		quit_flag = OutputSingle()

    # p_patient.join()
    # p_doctor.join()
	print OutputWhole(whole_para)

    #print(threading.enumerate())