import cv2
import numpy as np
import hand_detection as hd
import notes as nk
import pygame
from pygame import mixer

# Set up video capture from the camera
cap = cv2.VideoCapture(0)
cap.set(3,20* 75)
cap.set(4,400)

detector = hd.handDetector() 
pygame.init()
pygame.mixer.set_num_channels(60)
timer = pygame.time.Clock()

# Define the dimensions of the piano keys
white_key_width = 75
white_key_height = 350
black_key_width = white_key_width // 2
black_key_height = white_key_height // 2

left_oct = 4
right_oct = 5

active_whites = []
active_blacks = []
white_sounds = []
black_sounds = []

left_hand = nk.left_hand
right_hand = nk.right_hand
piano_notes = nk.piano_notes
white_notes = nk.white_notes
black_notes = nk.black_notes


for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))


# Define the ranges for each key's x-coordinate to identify key presses
key_ranges = [(i * white_key_width, (i + 1) * white_key_width) for i in range(21)]
black_key_ranges = [(i * white_key_width - black_key_width // 2, i * white_key_width + black_key_width // 2) for i in range(1, 21) if i % 7 not in [3, 0]]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    overlay = frame.copy()
    frame = detector.findHands(frame)
    lmList, bboxInfo = detector.findPosition(frame)
    if not ret:
        break

    # Draw white keys with border
    for i in range(0, 17):
        x = i * white_key_width
        cv2.rectangle(overlay, (x, 0), (x + white_key_width, white_key_height), (255, 255, 255), -1)
        cv2.rectangle(overlay, (x, 0), (x + white_key_width, white_key_height), (0, 0, 0), 2)
#set
    # Draw black keys with border
    for i in range(1, 17):
        if i % 7 not in [3, 0]:
            x = i * white_key_width - black_key_width // 2
            cv2.rectangle(overlay, (x, 0), (x + black_key_width, black_key_height), (0, 0, 0), -1)
            cv2.rectangle(overlay, (x, 0), (x + black_key_width, black_key_height), (255, 255, 255), 2)

    # name keys
    left_dict = {'W0': f'C{left_oct}',
                 'B21': f'Db{left_oct}',
                 'W1': f'D{left_oct}',
                 'B22': f'Eb{left_oct}',
                 'W2': f'E{left_oct}',
                 'W3': f'F{left_oct}',
                 'B23': f'Gb{left_oct}',
                 'W4': f'G{left_oct}',
                 'B24': f'Ab{left_oct}',
                 'W5': f'A{left_oct}',
                 'B25': f'Bb{left_oct}',
                 'W6': f'B{left_oct}'}

    right_dict = {'W7': f'C{right_oct}',
                 'B26': f'Db{right_oct}',
                 'W8': f'D{right_oct}',
                 'B27': f'Eb{right_oct}',
                 'W9': f'E{right_oct}',
                 'W10': f'F{right_oct}',
                 'B28': f'Gb{right_oct}',
                 'W11': f'G{right_oct}',
                 'B29': f'Ab{right_oct}',
                 'W12': f'A{right_oct}',
                 'B210': f'Bb{right_oct}',
                 'W13': f'B{right_oct}'}

    # Detecting key presses
    if lmList:
        x, y = lmList[8][1], lmList[7][2]
        for idx, (key_start, key_end) in enumerate(key_ranges+black_key_ranges):
            if key_start <= x <= key_end and black_key_height < y <= white_key_height:
                kn= f"W{idx}"
                if kn in left_dict:
                    index = white_notes.index(left_dict[kn])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
                elif kn in right_dict:
                    index = white_notes.index(right_dict[kn])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if key_start <= x <= key_end and black_key_height > y:
                kn= f"B{idx}"
                if kn in left_dict:
                    index = black_notes.index(left_dict[kn])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                elif kn in right_dict:
                    index = black_notes.index(right_dict[kn])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])

    alpha = 0.4
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    cv2.imshow('Piano', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
