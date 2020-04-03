# -*- coding: utf-8 -*-


import configparser
import os
import random
import string
from multiprocessing import Process
import ffmpeg
from pytube import YouTube
import ctypes


def dodownload(url, start, end):
    # get default path from conf file
    config = configparser.ConfigParser()
    config.read(os.path.join("..", "config", "conf.ini"))

    # pick highest stream quality available
    yt = YouTube(url)
    in_file = ffmpeg.input(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].url)

    path = config['config']['default_dir'] + "\\" + '' \
        .join(random.choices(string.ascii_uppercase + string.digits, k=10))
    # ensure name doesn't already exist
    while os.path.exists(path):
        path = config['config']['default_dir'] + "\\" + '' \
            .join(random.choices(string.ascii_uppercase + string.digits, k=10))

    in_file.trim(start=int(start), end=int(end)).output(path + ".mp4").run()

def run():
    # (really) quick explanation.

    print("____________________________START____________________________")
    print("how to use :")
    print("first arg : video url at time t.")
    print("second arg : record duration.")

    # get url, start and end. Correct arg usage is expected.
    url = input("url : ").split("?t=")
    url, start = url[0], int(url[1])
    end = int(start) + int(input("len : "))

    Process(target=dodownload, args=(url, start, end, )).start()

    print("\n\n\n")


if __name__ == "__main__":
    run()
