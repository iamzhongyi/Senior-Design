#Python 2.x program for Speech Recognition

import speech_recognition as sr
import threading
import time
from multiprocessing import Process, Queue 


def RecordDoctor(person):
    #enter the name of usb microphone that you found
    #using lsusb
    #mic_name = "USB PnP Sound Device"
    if (person == "doctor"):
    	mic_name = "Built-in Microphone"
    else:
    	mic_name = "USB PnP Sound Device"
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

	k = 0
	wholetext = ""
	with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
		r2.adjust_for_ambient_noise(source)
		r2.pause_threshold = 0.5
		while k<20:
			k = k + 1
            #wait for a second to let the recognizer adjust the
            #energy threshold based on the surrounding noise level
            #print(source_D)
			print person + " Please Say Something"
            #listens for the user's input
			audio = r2.listen(source)
            #print "Record finish, processing"
			t_recog = threading.Thread(target = RecogizeDoctor, name = "doctor", args = (audio,))
			t_recog.start()
            # print(threading.enumerate())

def RecordPatient(queue_patient):
    #enter the name of usb microphone that you found
    #using lsusb
    #the following name is only used as an example
    mic_name_P = "USB PnP Sound Device"
    #mic_name_2 = "Built-in Microphone"
    #Sample rate is how often values are recorded
    sample_rate = 48000
    #Chunk is like a buffer. It stores 2048 samples (bytes of data)
    #here.
    #it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    #Initialize the recognizer

    #generate a list of all audio cards/microphones
    mic_list = sr.Microphone.list_microphone_names()

    #the following loop aims to set the device ID of the mic that
    #we specifically want to use to avoid ambiguity.
    
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name_P:
            device_id_P = i
            print(device_id_P)

    audio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #use the microphone as source for input. Here, we also specify
    #which device ID to specifically look for incase the microphone
    #is not working, an error will pop up saying "device_id undefined"

    k = 0
    wholetext = ""
    while k<20:
        k = k + 1

        with sr.Microphone(device_index = device_id_P, sample_rate = sample_rate, chunk_size = chunk_size) as source_P:
                #wait for a second to let the recognizer adjust the
                #energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source_P)
            r.pause_threshold = 2.0
            #print(source_P)
                    
            print "Patient, Please Say Something(with USB microphone)"
            #listens for the user's input
            audio[2*k-1] = r.listen(source_P)
            print "Record finish, processing"
            Process_Read_1 = threading.Thread(target = RecogizePatient, name = "test_patient", args = (audio[2*k-1],))
            Process_Read_1.start()
            print(threading.enumerate())

def RecogizeDoctor(audio):
    try:
        text = r2.recognize_google(audio)
        #print "doctor said: " + text
        queue_sentence.put(text)
        
        #error occurs when google could not understand what was said
        
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        
    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def RecogizePatient(audio):
    try:
        text[2*k-1] = r.recognize_google(audio)
        print "patient said: " + text[2*k-1]
        queue_patient.put(text[2*k-1])
    except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            
    except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def OutputSingle():
	print queue_sentence.get()

def OutputWhole():
	print "output whole conversation"

if __name__ == '__main__':
    rd = sr.Recognizer()
    r2 = sr.Recognizer()
    audio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    k = 0
    queue_sentence = Queue()
    queue_patient = Queue()
    something = 0
    process_doctor = Process(target = RecordDoctor, args=("doctor",))
    #process_patient = Process(target = RecordPatient, args=(queue_patient,))
    #process_patient.start()
    process_doctor.start()
    
    while(1):
    	OutputSingle()

    #print(threading.enumerate())