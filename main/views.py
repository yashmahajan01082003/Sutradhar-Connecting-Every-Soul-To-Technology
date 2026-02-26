from django.shortcuts import render
import os
import subprocess
import threading
import time
import webbrowser
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from PIL import ImageGrab
from django.conf import settings
from django.http import HttpResponse, request
from django.shortcuts import render
from pathlib import Path
import psutil
import cv2
import mediapipe as mp
import pythoncom
import wmi
import comtypes
import cv2
from bs4 import BeautifulSoup
from django.shortcuts import render
import datetime
import smtplib
import subprocess
import os
import json
from django.http import HttpResponse
import random
import time
import webbrowser
from random import choice
import psutil
import pyautogui
import pyjokes
import requests
import pyttsx3
import speech_recognition as sr
import wikipedia
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.utils import AudioUtilities
from requests import get
import sys
from translate import Translator
from django.http import JsonResponse
from ctypes import cast , POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities , IAudioSessionControl

def home(request):
    return render(request, "home.html")

def filesystem(request):
    return render(request, "filesystem.html")


def openParti(request):
    partitions = psutil.disk_partitions(all=True)
    folders=[]
    for partition in partitions:
        drive_letter = partition.device
        folders.append(drive_letter)
        print(drive_letter)

    context={
        'folders': folders,
    }
    return render(request,'partition.html',context)


def get_directories_in_drive(fName):
    c_drive_path = fName
    directories = [name for name in os.listdir(c_drive_path) if os.path.isdir(os.path.join(c_drive_path, name))]
    return directories


def openPartiSpec(request,fName):
    partitions = psutil.disk_partitions(all=True)
    folders=[]
    directory_list=[]
    for partition in partitions:
        drive_letter = partition.device
        folders.append(drive_letter)

    if fName == folders[0]:
        directory_list = get_directories_in_drive(fName)


    if fName == folders[1]:
        directory_list = get_directories_in_drive(fName)


    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context={
        'folders': directory_list,
        'root' : fName,
        'perc': percent,
        'status': status,
    }
    return render(request,'insidepart.html',context)


def openPartiSpec2(request, fName0, fName1):
    partitions = psutil.disk_partitions(all=True)
    folders = [partition.device for partition in partitions]
    fName0 = fName0.replace('/', '\\')  # Replace forward slash with backslash
    fName1 = fName1.replace('/', '\\') if fName1 else ''  # Replace forward slash with backslash if fName1 is not empty

    path = os.path.join(fName0, fName1)
    is_file = os.path.isfile(path)

    if is_file:
        # Handle file case
        webbrowser.open(path)
        path1 = os.path.join(fName0)
        directory_list = []
        file_list = []
        if os.path.exists(path1):
            for item in os.listdir(path1):
                item_path = os.path.join(path1, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)

        root = os.path.join(fName0)

        context = {
            'folders': directory_list,
            'files': file_list,
            'root': root,
            'parent1': fName1,
        }
        return render(request, 'insidepart.html', context)

    directory_list = []
    file_list = []
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                directory_list.append(item)
            else:
                file_list.append(item)

    root = os.path.join(fName0, fName1)

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context = {
        'folders': directory_list,
        'files': file_list,
        'root': root,
        'parent1': fName1,
        'perc' : percent,
        'status' : status,
    }
    return render(request, 'insidepart.html', context)

def newD(request):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    fName = request.GET.get('name')
    flag = request.GET.get('flag')
    new_directory = os.path.join(desktop_path, fName)
    print(flag)
    # Create the directory if it doesn't exist
    if flag == '2':
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
            print("Directory created successfully.")
        else:
            print("Directory already exists.")

    if flag=='3':
        if not os.path.exists(new_directory):
            with open(new_directory, 'w') as file:
                file.write('')  # You can write content to the file if needed
            print("File created successfully.")
        else:
            print("File already exists.")

    if flag=='4':
        subprocess.call(["powershell.exe"])

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context={
        'folders' : folders,
        'perc' : percent,
        'status' : status,
        'deskp': desktop_path,
    }
    return render(request,'index.html',context)


def newD2(request, fName0):
    fName = request.GET.get('name')
    flag = request.GET.get('flag')
    print(flag)
    partitions = psutil.disk_partitions(all=True)
    folders = [partition.device for partition in partitions]
    fName0 = fName0.replace('/', '\\')  # Replace forward slash with backslash

    specified_path = fName0  # Specify the desired path here

    path = os.path.join(specified_path, fName)
    is_file = os.path.isfile(path)

    directory_list = []
    file_list = []

    if is_file:
        # Handle file case
        webbrowser.open(path)
        if os.path.exists(specified_path):
            for item in os.listdir(specified_path):
                item_path = os.path.join(specified_path, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)
    else:
        # Handle directory case
        if os.path.exists(fName0):
            for item in os.listdir(fName0):
                item_path = os.path.join(fName0, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)

    root = specified_path

    # Create the directory if it doesn't exist
    if flag=='2':
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory created successfully.")
        else:
            print("Directory already exists.")

    if flag=='3':
        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write('')  # You can write content to the file if needed
            print("File created successfully.")
        else:
            print("File already exists.")


    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context = {
        'folders': directory_list,
        'files': file_list,
        'root': root,
        'perc': percent,
        'status': status,
    }
    return render(request, 'insidepart.html', context)

def gesturePage(request):
    return render(request, 'gestures.html')


def pres(request):
    # Replace 'Presentation' with the actual path to your Presentation folder
    presentation_folder = 'Presentation'

    # Initialize an empty list to store folder names
    folder_list = []

    # Get a list of directories within the Presentation folder
    try:
        folders = os.listdir(presentation_folder)

        # Filter out only directories (excluding files)
        for folder in folders:
            folder_path = os.path.join(presentation_folder, folder)
            if os.path.isdir(folder_path):
                folder_list.append(folder)

    except FileNotFoundError:
        # Handle the case when the Presentation folder does not exist
        return "Presentation folder not found."

    # Now folder_list contains the names of folders within the Presentation folder
    # You can do whatever you want with the folder_list, for example, return it as part of the response
    context = {
        'FolderDets': folder_list,
    }
    return render(request, 'present.html', context)

def execPresentation(request,Fname):
    # Variables
    width, height = 1280, 720
    folderPath = 'Presentation/'+Fname

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Get list of images
    pathImages = sorted(os.listdir(folderPath), key=len)
    print(pathImages)

    # Variables
    imgNumber = 0
    hs, ws = int(120 * 1), 213
    gestureThreshold = 300
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 30
    annotations = [[]]
    annotationNumber = -1
    annotationStart = False

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)
        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage)

        # Resize the image to fit the screen
        imgCurrent = cv2.resize(imgCurrent, (width+250, height+70))

        hands, img = detector.findHands(img)

        if hands and buttonPressed is False:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
            lmList = hand['lmList']

            # Constrain value for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

            indexFinger = xVal, yVal
            # Gesture 1
            # Thumb = Backward
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                if imgNumber > 0:
                    imgNumber -= 1
                    buttonPressed = True

            # Gesture 2
            # Pinki Finger = Forward
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                    buttonPressed = True

            # Gesture 3
            # Show Pointer = Second and Index Finger
            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

            # Gesture 4
            # DrawPointer
            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotations[annotationNumber].append(indexFinger)
            else:
                annotationStart = False

            # Gesture 5
            # Erase
            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True

        # Button Pressed Iterations
        if buttonPressed:
            buttonCounter += 1
            if buttonCounter > buttonDelay:
                buttonCounter = 0
                buttonPressed = False

        for i in range(len(annotations)):
            for j in range(len(annotations[i])):
                if j != 0:
                    cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 200), 12)

            # Adding webcam image in slide
            imgSmall = cv2.resize(img, (ws, hs))
            h, w, _ = imgCurrent.shape
            imgCurrent[0:hs, w - ws:w] = imgSmall

        cv2.imshow("Image", img)
        cv2.imshow("Slides", imgCurrent)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


    # Replace 'Presentation' with the actual path to your Presentation folder
    presentation_folder = 'Presentation'

    # Initialize an empty list to store folder names
    folder_list = []

    # Get a list of directories within the Presentation folder
    try:
        folders = os.listdir(presentation_folder)

        # Filter out only directories (excluding files)
        for folder in folders:
            folder_path = os.path.join(presentation_folder, folder)
            if os.path.isdir(folder_path):
                folder_list.append(folder)

    except FileNotFoundError:
        # Handle the case when the Presentation folder does not exist
        return "Presentation folder not found."

    # Now folder_list contains the names of folders within the Presentation folder
    # You can do whatever you want with the folder_list, for example, return it as part of the response
    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'folders': folders,
        'folder_list': folder_list,
    }
    return render(request, 'home.html', context)



hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
virtual_mouse_thread = None
stop_virtual_mouse = threading.Event()
virtual_rmouse_thread = None


def run_virtual_mouse():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

                index_x, index_y = 0, 0
                thumb_x, thumb_y = 0, 0
                middle_x, middle_y = 0, 0

                for id, landmark in enumerate(hand.landmark):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    if id == 8:  # Index finger
                        index_x = x
                        index_y = y

                    if id == 4:  # Thumb finger
                        thumb_x = x
                        thumb_y = y

                    if id == 12:  # Middle finger
                        middle_x = x
                        middle_y = y

                # Draw circles around the fingers
                cv2.circle(frame, (int(index_x), int(index_y)), 10, (0, 255, 255), -1)
                cv2.circle(frame, (int(thumb_x), int(thumb_y)), 10, (0, 255, 255), -1)
                cv2.circle(frame, (int(middle_x), int(middle_y)), 10, (0, 255, 255), -1)

                # Calculate distances between fingers
                distance_index_middle = ((middle_x - index_x) ** 2 + (middle_y - index_y) ** 2) ** 0.5
                distance_index_thumb = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

                if distance_index_middle < 50:
                    pyautogui.click()
                    pyautogui.sleep(1)
                elif distance_index_thumb < 80:
                    pyautogui.moveTo(index_x * (screen_width / frame_width), index_y * (screen_height / frame_height))

        cv2.imshow('Virtual Mouse', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            # Killing thread
            if virtual_mouse_thread and virtual_mouse_thread.is_alive():
                stop_virtual_mouse.set()
                virtual_mouse_thread.join()
            break

    cap.release()
    cv2.destroyAllWindows()

def activateVM(request):
    global virtual_mouse_thread
    if not virtual_mouse_thread or not virtual_mouse_thread.is_alive():
        virtual_mouse_thread = threading.Thread(target=run_virtual_mouse)
        virtual_mouse_thread.start()

    return render(request,'home.html')

def speciallyabled(request):
    # Variables
    width, height = 500, 500

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)


    while True:
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img)

        if hands and len(hands) == 1:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
            lmList = hand['lmList']

            # Thumb tip and index tip coordinates
            thumbTip = lmList[4][0], lmList[4][1]
            indexTip = lmList[8][0], lmList[8][1]

            # Calculate distance between thumb tip and index tip
            distance = np.linalg.norm(np.array(thumbTip) - np.array(indexTip))

            # Constrain value for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

            indexFinger = xVal, yVal

            # Gesture1
            # Display "Nice" if the distance is very less
            if distance < 30:  # Adjust the threshold value as needed
                text = 'Fine'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


            if fingers == [1, 1, 1, 1, 1]:
                text = 'Wait'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Thumb = Drink Water
            elif fingers == [1, 0, 0, 0, 0]:
                text = 'Drink Water'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture2
            # Thumb + Index = Smile
            elif fingers == [1, 1, 0, 0, 0]:
                text = 'Smile'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 3
            # Thumb + Index + Middle Finger = Understood
            elif fingers == [1, 1, 1, 0, 0]:
                text = 'Understood'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 4
            # Thumb + Index + Middle + Ring = Rock On
            elif fingers == [0, 1, 0, 0, 1]:
                text = 'Rock On'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 5
            # Index = No
            elif fingers == [0, 1, 0, 0, 0]:
                text = 'No'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 6
            # Pinky and Thumb = Call
            elif fingers == [1, 0, 0, 0, 1]:
                text = 'Call'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 7
            # Thumb + Index + Pinky = I Love U
            elif fingers == [1, 1, 0, 0, 1]:
                text = 'I Love U'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 8
            # Index + Middle + Ring = Slow
            elif fingers == [0, 1, 1, 1, 0]:
                text = 'Slow'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 9
            # Index + Middle = Louder
            elif fingers == [0, 1, 1, 0, 0]:
                text = 'Louder'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 10
            # Pinky = Repeat
            elif fingers == [0, 0, 0, 0, 1]:
                text = 'Repeat'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            elif fingers == [0, 0, 1, 0, 0]:
                text = 'Go To Hell'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()  # Close OpenCV windows

    return render(request, 'home.html')

def execBrightnessControl(request):
    # Define the maximum and minimum brightness values
    MAX_BRIGHTNESS = 100
    MIN_BRIGHTNESS = 0
    pythoncom.CoInitialize()
    # Connect to WMI
    wmi_obj = wmi.WMI(namespace="wmi")

    # Function to set the screen brightness
    def set_brightness(value):
        # Clamp the value within the brightness range
        brightness = max(min(value, MAX_BRIGHTNESS), MIN_BRIGHTNESS)

        # Scale the brightness value to the range [0, 100]
        brightness = int(brightness * 100 / MAX_BRIGHTNESS)

        # Set the screen brightness
        wmi_obj.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

    cap = cv2.VideoCapture(0)
    hd = HandDetector()
    val = 0
    while True:
        ret, img = cap.read()
        if not ret:
            break

        hands, img = hd.findHands(img)

        if hands:
            lm = hands[0]['lmList']

            length, info, img = hd.findDistance(lm[8][0:2], lm[4][0:2], img)
            blevel = np.interp(length, [25, 145], [0, 100])
            val = np.interp(length, [0, 100], [400, 150])
            blevel = int(blevel)

            set_brightness(blevel)

            cv2.rectangle(img, (20, 150), (85, 400), (0, 255, 255), 4)
            cv2.rectangle(img, (20, int(val)), (85, 400), (0, 0, 255), -1)
            cv2.putText(img, str(blevel) + '%', (20, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'home.html')

def execHandTab(request):
    # Url
    fbUrl = 'https://www.facebook.com/'
    instaUrl = 'https://www.instagram.com/'
    meetUrl = 'https://meet.google.com/'

    # Variables
    width, height = 500, 500

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Variables
    imgNumber = 0
    hs, ws = int(120 * 1), 213
    gestureThreshold = 300
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 30
    annotations = [[]]
    annotationNumber = -1
    annotationStart = False

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    while True:
        try:
            # Import images
            success, img = cap.read()
            img = cv2.flip(img, 1)

            hands, img = detector.findHands(img)

            if hands and len(hands) == 1:
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                print(fingers)
                lmList = hand['lmList']

                # Constrain value for easier drawing
                indexFinger = lmList[8][0], lmList[8][1]
                xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
                yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

                indexFinger = xVal, yVal

                # Gesture1
                # Thumb = Open FaceBook
                if fingers == [1, 0, 0, 0, 0]:
                    webbrowser.open(fbUrl)
                    time.sleep(2)


                # Gesture 3
                # Thumb + Index + Middle Finger = Calculator
                if fingers == [1, 1, 1, 0, 0]:
                    calculator_process = subprocess.Popen('calc.exe')
                    # Close the calculator process
                    time.sleep(2)

                # Gesture 4
                # Thumb + Index + Middle + After Index = File
                if fingers == [1, 1, 1, 1, 0]:
                    subprocess.Popen('explorer')
                    time.sleep(2)

                # Gesture 5
                # ALl up = Whatsapp
                if fingers == [0, 1, 0, 0, 0]:
                    # Open whatsapp
                    webbrowser.open('https://web.whatsapp.com/')
                    time.sleep(2)

                # #Gesture 6
                # Pinki and Thumb = Settings
                if fingers == [1, 0, 0, 0, 1]:
                    subprocess.Popen('explorer.exe ms-settings:')
                    time.sleep(2)

                # #Gesture 7
                # Thumb + Index + Pinki = Mail
                if fingers == [1, 1, 0, 0, 1]:
                    webbrowser.open('mailto:')
                    time.sleep(2)



        except BrokenPipeError as e:
            pass

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    return render(request, 'home.html')



def execFaceDistance(request):
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=1)

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            # cv2.line(img,pointLeft,pointRight,(0,200,0),3)
            # cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
            # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3

            # Finding the focal length
            # d = 50
            # f = (w*d)/W
            # print(f)

            # Finding the distance or depth
            f = 500
            d = (W * f) / w
            print(d)

            cvzone.putTextRect(img, f'Depth : {int(d)} cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    return render(request, 'home.html')

def eyeBasedFeat(request):
    return render(request, "eyeBasedFeat.html")


def run_virtual_rmouse():
    cam = cv2.VideoCapture(0)
    print(cv2.__version__)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.0085:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        key = cv2.waitKey(1)
        if key is ord('q'):
            global virtual_rmouse_thread
            if not virtual_rmouse_thread or not virtual_rmouse_thread.is_alive():
                virtual_rmouse_thread = threading.Thread(target=run_virtual_rmouse)
                virtual_rmouse_thread.start()
            break
    cv2.destroyAllWindows()  # Close OpenCV windows

def activateRM(request):
    global virtual_rmouse_thread
    if not virtual_rmouse_thread or not virtual_rmouse_thread.is_alive():
        virtual_rmouse_thread = threading.Thread(target=run_virtual_rmouse)
        virtual_rmouse_thread.start()

    return render(request, 'home.html' )


def frontEndForJarvis(request):
    #runJarvis(request)
    features = []
    features.append('open youtube')
    features.append('open notepad')
    features.append('tell me a joke')
    features.append('turn bluetooth on')
    features.append('get date or time')
    features.append('open command prompt')
    features.append('open camera')
    features.append('play music')
    features.append('ip address')
    features.append('wikipedia')
    features.append('stack overflow')
    features.append('linkedin')
    features.append('play song on youtube')
    features.append('close notepad')
    features.append('shut down')
    features.append('restart computer')
    features.append('say you can sleep to turn it off')
    features.append('say no thank to turn it off')
    features.append('where are we')
    features.append('read pdf')
    features.append('send message')
    features.append('translate')
    context = {'feats': features}
    return render(request, 'jarvis1.html',context)

import subprocess

def runJarvis(request):
    subprocess.Popen(["python", "main/jarvis.py"])
    return render(request, "home.html")

def voiceFeat(request):
    return render(request, "voiceBasedFeat.html")

def chatbot(request):
     return render(request, "chatbot.html")

import os
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
import json
import os
import google.generativeai as genai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.conf import settings

genai.configure(api_key="AIzaSyCurpPbqf-yXxsnqyC_8HlzLm-S02X2O44")
model = genai.GenerativeModel("gemini-3-flash-preview")


@require_POST
def chat_with_gemini(request):
    try:
        data = json.loads(request.body)
        user_message = data.get("message")

        if not user_message:
            return JsonResponse({"error": "Empty message"}, status=400)

        response = model.generate_content(user_message)

        return JsonResponse({
            "response": response.text
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def faceFeat(request):
     return render(request, "faceBasedFeatures.html")
