import os
from pytube import YouTube
from moviepy.editor import *


class YoutubeToMp3:
	def __init__(self, url):
		self.url = url

	@staticmethod
	def create_folder_mp3(folder_name):
		os.system('mkdir %s' % folder_name)
		os.chdir(folder_name)

	def get_mp4_file(self):
		yt = YouTube(self.url)
		mp4_file = yt.streams.get_by_itag(18).download()
		return mp4_file

	def get_mp3_file(self):
		mp4_file = self.get_mp4_file()
		mp3_file = mp4_file.replace('.mp4', '.mp3')
		return mp3_file

	@staticmethod
	def convert_mp4_to_mp3(mp4_file, mp3_file):
		video_file = VideoFileClip(mp4_file)
		audio_file = video_file.audio
		audio_file.write_audiofile(mp3_file)
		audio_file.close()
		video_file.close()
		os.remove(mp4_file)

	def run(self):
		mp4_file = self.get_mp4_file()
		mp3_file = self.get_mp3_file()
		self.convert_mp4_to_mp3(mp4_file, mp3_file)


if __name__ == "__main__":
	input_url = input("Youtube Link: ")
	input_folder_name = "Music"  # change folder here
	ytb = YoutubeToMp3(input_url)
	ytb.create_folder_mp3(input_folder_name)
	ytb.run()
