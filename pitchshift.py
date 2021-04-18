import numpy as np
import sox
import pyaudio, struct, wave
import tkinter
import pygame

# sample rate in Hz
RATE = 44100
RECORD_SECONDS = 5
BLOCKLEN=800

MAXVALUE = 2**15-1

k=0

# Number of blocks to run for
num_blocks = int(RATE / BLOCKLEN * RECORD_SECONDS)

p = pyaudio.PyAudio()
# wf = wave.open("sample.wav", 'rb')
PA_FORMAT = pyaudio.paInt16
#
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=2,
#                 rate=44100,
#                 output=True,
#                 frames_per_buffer = 800)

stream = p.open(
        format      = PA_FORMAT,
        channels    = 1,
        rate        = RATE,
        input       = True,
        output      = True,
        frames_per_buffer = 800)

CONTINUE = True
KEYPRESS = False


def up():
    global CONTINUE
    global KEYPRESS
    global k

    k += 1

def down():
    global CONTINUE
    global KEYPRESS
    global k

    k -= 1

def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('aroha.wav')
    pygame.mixer.music.play()


root = tkinter.Tk()
# root.bind("<Key>", my_function)

button1 = tkinter.Button(text='pitch up')
button1.config(command = up)

button2 = tkinter.Button(text='pitch down')
button2.config(command = down)

button1.pack()
button2.pack()


# Start loopfgh
while CONTINUE:
    root.update()

    # Get frames from audio input stream
    # input_bytes = stream.read(BLOCKLEN)       # BLOCKLEN = number of frames read
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)   # BLOCKLEN = number of frames read
    # print(input_bytes)
    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)

    scaled = np.frombuffer(input_bytes, np.int16)

    # create a transformer
    tfm = sox.Transformer()


    # shift the pitch up by 1 semitones
    tfm.pitch(k)

    y_out=2*tfm.build_array(input_array=scaled, sample_rate_in=RATE)

    y = np.clip(y_out.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    output_bytes = struct.pack('h' * BLOCKLEN, *y)

    # Write binary data to audio output stream
    stream.write(output_bytes, BLOCKLEN)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()



