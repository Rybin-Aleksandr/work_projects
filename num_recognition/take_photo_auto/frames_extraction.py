import numpy as np
import cv2
import os
import keyboard
import time
from datetime import datetime
from pathlib import Path


def write_frames(path: dir):
    if not os.path.exists(path):
        os.mkdir(path)
        
    print('--Меню:')
    print('-----------------------------------------')
    print('--Сделать снимки: зажатие клавиши "Space"')
    print('--Выход: нажать "q"')

    frames_counter = 1
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow("", frame)
        if keyboard.is_pressed(' '):
            cv2.imwrite(path + "/frame%d.jpg" % frames_counter, frame)
            print("--Сохранено в:")
            print(path + "/frame%d.jpg" % frames_counter)
            print('-----------------------------------------')
            frames_counter += 1
            time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    today = str(datetime.now())[:19].replace('-', '_').replace(':', '_')
    directory = '{}image_data_{}'.format(Path(__file__).resolve().parents[1], today)
    write_frames(directory)



