import face_recognition
import time

start = time.time()
known_image = face_recognition.load_image_file("C:/Users/fang/Desktop/1.jpg")
unknown_image = face_recognition.load_image_file("C:/Users/fang/Desktop/2.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
start_compare = time.time()
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
print('人脸比对耗时' + str(time.time() - start_compare))

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print('人脸比对总耗时' + str(time.time() - start))
print(results)
