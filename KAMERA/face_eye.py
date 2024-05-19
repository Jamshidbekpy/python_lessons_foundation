import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
def yuzni_tanish():
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # copyright Tim Ruscia aka techwithtim
    # code from https://github.com/techwithtim/OpenCV-Tutorials
def rasmdan_yuzni_tanish(image_path):
    # Kiritilgan rasmni yuklash
    image = cv2.imread(image_path)
    # Haqiqiy ranglarga o'tkazish
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Yuzni aniqlash uchun kaskadlar
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Yuzlarni chizish va nomlarini joylash
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, 'Inson', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    # Tanilgan yuzlarni ko'rsatish
    cv2.imshow('Yuzlar', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def object_name():
        # YOLOv8 modelini yuklash
    model = YOLO('yolov8n.pt')  # YOLOv8 model faylini to'g'ri yo'l bilan ko'rsating

    # Kamerani ishga tushirish
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Kameradan kadrni olish
        success, frame = cap.read()
        if not success:
            break

        # Obyektlarni aniqlash
        results = model(frame)

        # Aniqlangan obyektlarni ekranga chiqarish
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Obyektning koordinatalari va ishonchliligi
                x1, y1, x2, y2 = box.xyxy[0]
                confidence = box.conf[0]

                # Ishonchlilik darajasi 0.5 dan yuqori bo'lgan obyektlarni chiqarish
                if confidence > 0.5:
                    # To'rtburchak chizish
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

                    # Obyekt nomini va ishonchliligini yozish
                    label = f'{model.names[int(box.cls[0])]} {confidence:.2f}'
                    cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Natijani ko'rsatish
        cv2.imshow('Obyektlarni aniqlash', frame)

        # "q" tugmasini bosilsa chiqish
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamerani va oynani yopish
    cap.release()
    cv2.destroyAllWindows()