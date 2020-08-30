import sys
from moviepy.editor import *

video = VideoFileClip('input.mp4')
audio = video.audio
audio.write_audiofile('output.wav') 