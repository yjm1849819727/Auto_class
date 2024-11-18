# encoding=utf-8
from PIL import Image


def show_donate(imgpath="res/QRcode.jpg"):
    try:
        print("如果帮助到了您请记得给个star")
    except FileNotFoundError:
        return
