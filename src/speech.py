import speech_recognition as sr
import threading
from threading import Thread, current_thread
import time
from multiprocessing import Process, Queue, Manager 

def Classify(text,svm):
	#classify interface
	return 1

def Record(person):
	#target the microphone by id or by name
	if (person == "doctor"):
		#mic_name = "USB PnP Sound Device" 
		device_id = 0
	else:
		mic_name = "R555"
		device_id = 0
    	#mic_name = "USB PnP Sound Device"
    #Sample rate is how often values are recorded
	sample_rate = 48000
    #Chunk is like a buffer, stores 2048 samples (bytes of data)
    #Advisable to use powers of 2 such as 1024 or 2048
	chunk_size = 2048

    #generate a list of all audio cards/microphones
	mic_list = sr.Microphone.list_microphone_names()
	print mic_list
	# for i, microphone_name in enumerate(mic_list):
	# 	if microphone_name == mic_name:
	# 		device_id = i

    #use the microphone as source for input. Here, we also specify
    #which device ID to specifically look for incase the microphone
    #is not working, an error will pop up saying "device_id undefined"
	with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
		recog.adjust_for_ambient_noise(source)
		recog.pause_threshold = 0.7
		while 1:
            #listens for the user's input
			audio = recog.listen(source)
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

# OutputSingle(): convert one dialoge sentence dictionary to string, and feed 
# into text classify function.
def OutputSingle():
	pick = queue_sentence.get()
	# add to whole dictionary
	log.update(pick)
	# send a string to text classification
	index = pick.keys()[0]
	output = str(index)+ " " + pick[index]
	Classify(output,svm,)
	print output
	# check for end of visit
	if "quit" in pick.values()[0]:
		p_doctor.terminate()
		p_patient.terminate()
		return 1
	return 0

# OutputWhole(log): sort the orderless dialoge dictionary, produce ordered 
# dialoge list
# @param[in] log: a dictionary containning all the sentences
def OutputWhole(log):
	temp = log
	whole = []
	for i in sorted(log.keys()):
		whole.append(temp[i])
	return whole

if __name__ == '__main__':
	log = {}
	recog = sr.Recognizer()
	queue_sentence = Manager().Queue()
	queue_index = Queue()
	queue_index.put(1)
	# pre-train the bayes network 
	# 
	# 
	# 	
	p_doctor = Process(target = Record, args=("doctor",))
	p_patient = Process(target = Record, args=("patient",))
	p_patient.start()
	p_doctor.start()
	quit_flag = 0
	while(not quit_flag):
		quit_flag = OutputSingle()
	print OutputWhole(log)