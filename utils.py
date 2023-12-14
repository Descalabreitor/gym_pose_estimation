import numpy as np
import cv2

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

def create_button(x, y, width, height, text, function, frame):

    rect = cv2.Rect(x, y, width, height)

    # Crear la imagen del botón
    img_boton = cv2.rectangle(frame, rect, (255, 255, 255), -1)

    # Escribir el texto del botón
    cv2.putText(img_boton, text, (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # Crear el evento de clic para el botón
    cv2.setMouseCallback(img_boton, function)

def calculate_speed(counter, prev_timestamp):
    if counter > 0:
        timestamp_diff = time.time() - prev_timestamp
        prev_timestamp = time.time()

        speed = counter / timestamp_diff

        return speed, prev_timestamp
