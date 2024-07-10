import wave
import pyaudio
from pydub import AudioSegment

# Reading from a File

class InputFile:
  def __init__(self,inp):
    self.input_path=inp
  def CreateObj(self):
    try:
      obj=wave.open(self.input_path, 'rb')
    except:
      input_file=AudioSegment.from_mp3(self.input_path)
      l=self.input_path.split('.')
      self.input_path=l[0]+".wav"
      input_file.export(self.input_path, format="wav")
      obj=wave.open(self.input_path, 'rb')
    return obj

# Recording Voice

class RecordLive:
  def __init__(self):
    self.pyaud=pyaudio.PyAudio()
    self.frames=[]
  def StartRecording(self):
    stream=self.pyaud.open(
        format=pyaudio.paInt16,
        channels=2,
        rate=16000,
        frames_per_buffer=3200,
        input=True
    )
    for i in range(0,25):
      data=stream.read(3200)
      self.frames.append(data)

    stream.stop_stream()
    stream.close()
    self.pyaud.terminate()

    obj=wave.open("voice.wav","wb")
    obj.setnchannels(2)
    obj.setsampwidth(self.pyaud.get_sample_size(pyaudio.paInt16))
    obj.setframerate(16000)
    obj.writeframes(b"".join(self.frames)) #this line copies the previous file to the new file
    obj.close()
    return obj

def start():
  i=False
  while i==False:
    answer=input("Do you want to record your voice or choose a music file? \"press r to record and press f for file\"")
    if answer=="r":
      robj=RecordLive()
      obj=robj.StartRecording()
      i=True
      file=AudioSegment.from_wav("voice.wav")  # Part of Enhancement
    elif answer=="f":
      inp=input("enter file name with extension (mp3 or wav)")
      fobj=InputFile(inp)
      obj=fobj.CreateObj()
      i=True
      file=AudioSegment.from_wav(fobj.input_path) # Part of Enhancement
  
  # Enhancing the Audio
  
  file=file+6 # Inclrease volume by 6 db
  file.export("audio.mp3", format='mp3')
  file2=AudioSegment.from_mp3("audio.mp3")
