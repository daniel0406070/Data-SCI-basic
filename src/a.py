import cv2
import tensorflow as tf

# 이미지 불러오기
img = cv2.imread('image.jpg')

# 이미지 전처리
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
_, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

# 숫자 인식 모델 불러오기
model = tf.keras.models.load_model('model.h5')

# 이미지에서 숫자 추출
contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w < 10 or h < 10:
        continue
    number_img = img_thresh[y:y+h, x:x+w]
    number_img = cv2.resize(number_img, (28, 28))
    number_img = number_img.reshape((1, 28, 28, 1))
    number_img = number_img.astype('float32') / 255
    prediction = model.predict(number_img)
    number = tf.argmax(prediction, axis=1)
    print(number.numpy()[0])
