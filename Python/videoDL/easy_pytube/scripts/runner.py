# -*- coding: utf-8 -*-


import configparser
import random
import string
from multiprocessing import Process

import ffmpeg
from moviepy.editor import *
from pytube import YouTube


def dodownload(url, start, end):
    # move to current dir to access ffmpeg executable and config file
    os.chdir(os.path.dirname(__file__))

    # get default path from conf file
    config = configparser.ConfigParser()
    filename = os.path.join('..', 'config', 'conf.ini')
    config.read(filename)

    # pick highest stream quality available
    yt = YouTube(url)
    video_in_file = ffmpeg.input(yt.streams.filter(file_extension="mp4").order_by('resolution').last().url)


    # define path and ensure name doesn't already exist
    path = config['config']['default_dir'] + "\\" + '' \
        .join(random.choices(string.ascii_uppercase + string.digits, k=10))
    while os.path.exists(path):
        path = config['config']['default_dir'] + "\\" + '' \
            .join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # download all audio at path\name_audio.mp4
    yt.streams.filter(only_audio=True).first().download(output_path=path.rsplit("\\", 1)[0], filename=path.rsplit("\\", 1)[1] + "_audio")

    # get portion of video and cut duplicated frames out
    video_in_file.trim(start=int(start), end=int(end)).output(path + "_cut.mp4").run()
    # clip = VideoFileClip(path + ".mp4").subclip(int(start), int(end))
    # clip.write_videofile(path + "_cut.mp4")
    # clip.close()

    # trim audio
    audioclip = AudioFileClip(path + "_audio.mp4").subclip(int(start), int(end))
    audioclip.write_audiofile(path + "_audiocut.mp3")
    audioclip.close()

    # concat audio and video
    ffmpeg.concat(ffmpeg.input(path + "_cut.mp4"), ffmpeg.input(path + "_audiocut.mp3"), v=1, a=1).output(path + "_processed.mp4").run()

    # remove the useless video and audio
    os.remove(path + "_cut.mp4")
    os.remove(path + "_audiocut.mp3")
    os.remove(path + "_audio.mp4")


def run():
    # (really) quick explanation.
    print("____________________________START____________________________")
    print("how to use :")
    print("first arg : video url at time t.")
    print("second arg : record duration.")

    # get url, start and end. Correct arg usage is expected.
    inputed = input("url : ")
    url = inputed.split("?")[0]
    start = inputed.split("t=")[-1]
    end = int(start) + int(input("len : "))

    Process(target=dodownload, args=(url, start, end,)).start()

    print("\n\n\n")


if __name__ == "__main__":
    run()
