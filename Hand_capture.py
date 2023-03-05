# Code inspiré de https://google.github.io/mediapipe/solutions/hands.html

import cv2
import mediapipe as mp


class Coord:

    def __init__(self, x=1 / 2, y=1 / 2, z=0, fist=False, bottom_hand=False, gun=False, thumb=False):
        self.x = x
        self.y = y
        self.depth = z
        self.fist = fist
        self.bottom_hand = bottom_hand
        self.gun = gun
        self.thumb = thumb


def run(coords):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    # For webcam input:
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
                coords.x = 1 - hand_landmarks.landmark[mp_hands.HandLandmark(9).value].x
                coords.y = 1 - hand_landmarks.landmark[mp_hands.HandLandmark(9).value].y
                coords.depth = hand_landmarks.landmark[mp_hands.HandLandmark(9).value].z
                index = hand_landmarks.landmark[mp_hands.HandLandmark(7).value]
                indexMid = hand_landmarks.landmark[mp_hands.HandLandmark(5).value]
                ringFinger = hand_landmarks.landmark[mp_hands.HandLandmark(15).value]
                ringFingerMid = hand_landmarks.landmark[mp_hands.HandLandmark(13).value]
                handBottom = hand_landmarks.landmark[mp_hands.HandLandmark(0).value]
                thumbMid = hand_landmarks.landmark[mp_hands.HandLandmark(1).value]
                thumbTop = hand_landmarks.landmark[mp_hands.HandLandmark(4).value]
                for i in range(5):
                    if (index.y > indexMid.y) and (index.y < handBottom.y) and (ringFinger.y > ringFingerMid.y) and (ringFinger.y < handBottom.y) :
                        if i == 4:
                            coords.fist = True
                    else :
                        coords.fist = False
                        break
                for i in range(5):
                    if (ringFingerMid.y > handBottom.y) and (indexMid.y > handBottom.y):
                        if i == 4:
                            coords.bottom_hand = True
                    else :
                        coords.bottom_hand = False
                        break
                for i in range(5):
                    if (thumbMid.y < handBottom.y) and (thumbMid.y < index.y) and (thumbMid.y < ringFinger.y):
                        if i == 4:
                            coords.gun = True
                    else :
                        coords.gun = False
                        break
                if thumbTop.y < handBottom.y:
                    coords.thumb = True
                else:
                    coords.thumb = False
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
