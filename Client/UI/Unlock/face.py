import face_recognition
import cv2
import numpy as np

# qt
import threading

from PyQt5.QtCore import QTimer
from threading import Thread
from PyQt5.QtWidgets import *  # UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor
from PyQt5.Qt import QApplication
import os
import time
from threading import Timer
# qt


class face_ui(QMainWindow):
    
    def __init__(self):

        self.close_cam = False
        super(face_ui, self).__init__()
        uic.loadUi("unlock.ui", self)

        self.setStyleSheet("QWidget { background-color: %s}" %
                           QtGui.QColor(247, 247, 247).name())

        self.welcome_l.setHidden(True)
        self.offset = None
        radius = 25.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        # self.lookingfor_l.setHidden(False)
        self.lookingfor_l.setStyleSheet(
            'background-color:rgba(255, 255, 255, 0.5);')

        movie = QtGui.QMovie(os.getcwd() + '/befor.gif')
        self.lookingfor_l.setMovie(movie)
        movie.start()

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.textEdit.setStyleSheet(
            "background-color:  rgb(247, 247, 247);border: 1px solid rgb(0, 0, 0);border-radius:15px;color:black;")

        self.move(qr.topLeft())
        self.welcome_l.setStyleSheet(
            'background-color:transparent;color:rgba(107, 107, 107)')
        self.welcome_l_2.setStyleSheet(
            'background-color:transparent;color:rgba(107, 107, 107)')

        self.textEdit.textChanged.connect(self.textChanged_messege_event)
        self.show()
        self.face_id_unlock()

    def textChanged_messege_event(self):
        if str(self.textEdit.text()) == '1234':
            self.close_cam = True
            self.show_next()
            self.welcome_l_2.setHidden(True)
            self.textEdit.setHidden(True)

    def face_id_unlock(self):
        app_face.processEvents()
        face_count = 0
        video_capture = cv2.VideoCapture(0)
        # Load a sample picture and learn how to recognize it.
        obama_image = face_recognition.load_image_file("face.jpg")
        app_face.processEvents()
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        known_face_encodings = [obama_face_encoding, ]
        known_face_names = ["Mohammad Hossein", ]
        face_locations = []
        face_encodings = []
        app_face.processEvents()
        face_names = []
        process_this_frame = True
        while True:
            app_face.processEvents()
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    app_face.processEvents()
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding)
                    name = "Unknown"
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    face_names.append(name)

            process_this_frame = not process_this_frame

            print('\033c')
            print(face_count)

            if face_names == known_face_names:
                app_face.processEvents()
                face_count += 1
            else:
                face_count = 0
            if face_count == 30 or self.close_cam == True:
                break

        # Release handle to the webcam
        app_face.processEvents()
        video_capture.release()
        cv2.destroyAllWindows()
        self.close_cam = True
        self.show_next()

    def show_next(self):

        if self.close_cam == True:

            self.lookingfor_l.setStyleSheet(
                'background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/after.gif')
            self.lookingfor_l.setMovie(movie)
            movie.start()
            self.welcome_l.setText("Hello "+"mohammad hossein"+" !")
            self.welcome_l_2.setHidden(True)
            self.textEdit.setHidden(True)
            self.welcome_l.setHidden(False)

            self.timer_face = QtCore.QTimer()
            self.timer_face.singleShot(3400, lambda: self.close())


app_face = QApplication(sys.argv)
face = face_ui()
app_face.exit(app_face.exec_())
