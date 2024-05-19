import face_eye
request  = input("Qaysi funksiyani tanlaysiz?>>>>")
if request == "1":
    face_eye.yuzni_tanish()
elif request == "2":
    image_path = 'people.jpg' 
    face_eye.rasmdan_yuzni_tanish(image_path)
elif request == "3":
    face_eye.object_name()