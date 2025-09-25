import cv2 as cv
vid= cv.VideoCapture(0)
# vid = cv.cvtColor(vi, cv.COLOR_BGR2GRAY)
while True:
    isTrue, frame = vid.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
      break
vid.release()
cv.destroyAllWindows()

