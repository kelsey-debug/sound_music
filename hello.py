
import simpleaudio as sa 
import numpy as num
import matplotlib.pyplot as pyplot

duration = 3 
sample_rate = 48000 #samples per second 
freq = 440 * 2 * num.pi #in radians

#generate array holding timesteps.start at 0 and end at 3 seconds, containing samplerate * duration num of samples.to have enough components sampled for hifidelity? 
timestep = num.linspace (0,duration,sample_rate * duration, False)

sin_wave = num.sin(freq * timestep ) #no phase specified in hw

#2^15 - 1 = 32767 is the full amp range. I want my amplitude to be limited to a quarter this size (32767 *.25 = 8191). 
audio = sin_wave * 8191/ num.max(num.abs(sin_wave))
#audio = sin_wave * 32767/ num.max(num.abs(sin_wave))  this is the normal. high quality amp range we want to be inside

#convert wave to 16 bit integers
sound = audio.astype(num.int16)

wav_obj = sa.WaveObject(sound,1,2,sample_rate)
playback_obj = wav_obj.play() 

if playback_obj.is_playing():
    print('still playing')

playback_obj.wait_done() 
