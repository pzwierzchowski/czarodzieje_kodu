from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("examples/sounds/laser1.wav", format="wav")
play(sound)