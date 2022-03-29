from unittest import result
import cv2
import mediapipe as mp
mpDrawing = mp.solutions.drawing_utils
mppDrawingStyle = mp.solutions.drawing_styles
mpHands = mp.solutions.hands

# camera access
cap = cv2.VideoCapture(0)
hands = mpHands.Hands()
while 1:
    data, image = cap.read()
    # flipping image
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # storing results
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mpDrawing.draw_landmarks(
                image, hand_landmark, mpHands.HAND_CONNECTIONS)
    cv2.imshow('Hand Tracker', image)
    cv2.waitKey(1)
