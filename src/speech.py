#Python 2.x program for Speech Recognition

import speech_recognition as sr
import threading
import time
from multiprocessing import Process, Queue 


def RecordDoctor(something):
    #enter the name of usb microphone that you found
    #using lsusb
    #the following name is only used as an example
    #mic_name = "USB PnP Sound Device"
    mic_name_D = "Built-in Microphone"
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
        if microphone_name == mic_name_D:
            device_id_D = i
            print(device_id_D)

    audio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #use the microphone as source for input. Here, we also specify
    #which device ID to specifically look for incase the microphone
    #is not working, an error will pop up saying "device_id undefined"

    k = 0
    wholetext = ""
    while k<20:
        k = k + 1
        with sr.Microphone(device_index = device_id_D, sample_rate = sample_rate, chunk_size = chunk_size) as source_D:
                #wait for a second to let the recognizer adjust the
                #energy threshold based on the surrounding noise level
            r2.adjust_for_ambient_noise(source_D)
            r2.pause_threshold = 1.0
            #print(source_D)
            
            print "Doctor, Please Say Something"
            #listens for the user's input
            audio[2*k] = r2.listen(source_D)
            #print "Record finish, processing"
            Process_Read_2 = threading.Thread(target = RecogizeDoctor, name = "test_doctor", args = (audio[2*k],))
            Process_Read_2.start()
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
        text[2*k] = r2.recognize_google(audio)
        #print "doctor said: " + text[2*k]
        queue_doctor.put(text[2*k])
        
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
	return 0;

def OutputWhole():
	return 0;

if __name__ == '__main__':
    rd = sr.Recognizer()
    r2 = sr.Recognizer()
    audio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    k = 0
    queue_doctor = Queue()
    queue_patient = Queue()
    something = 0
    process_doctor = Process(target = RecordDoctor, args=(something,))
    #process_patient = Process(target = RecordPatient, args=(queue_patient,))
    #process_patient.start()
    process_doctor.start()
    print queue_doctor.get()
    #while(not end):
    #	Output()

    #print(threading.enumerate())