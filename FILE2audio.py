from gtts import gTTS
import os

file = open("Tutorials\speech_to_audio/text.txt",'r').read()
language = 'hi'
output = gTTS(text=file,lang=language,slow=False)
output.save('Tutorials\speech_to_audio/audio.mp3')

os.system("start audio.mp3")