import cv2
import mediapipe as mp
from pynput.mouse import Controller

mouse = Controller()

# Choose you camera
camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cursor_history = []
cursor_history_max_len = 5  # Smoothness

while True:
    success, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = cv2.flip(imgRGB, flipCode=1)
    img = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB)
    results = hands.process(image=imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            # Check with extended index finger
            index_finger_extended = False
            if handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP].y:
                index_finger_extended = True

            for id, point in enumerate(handLms.landmark):
                width, height, _ = img.shape
                x, y = int(point.x * width), int(point.y * height)

                if id == 8 and index_finger_extended:

                    # Calculate coordinates as a percentage
                    x_percent = int(point.x * 100)
                    y_percent = int(point.y * 100)

                    # Calculate mouse position based on camera view and monitor size
                    monitor_width, monitor_height = 1920, 1080
                    mouse_x = int(x_percent * monitor_width / 100)
                    mouse_y = int(y_percent * monitor_height / 100)

                    # Apply moving average to smooth cursor movement
                    cursor_history.append((mouse_x, mouse_y))
                    if len(cursor_history) > cursor_history_max_len:
                        cursor_history.pop(0)
                    smoothed_cursor = tuple(map(lambda i: sum(i) / len(i), zip(*cursor_history)))

                    # Move the mouse cursor
                    mouse.position = smoothed_cursor

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
