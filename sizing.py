import cv2 as cv

def rescaleFrame(frame,scale = 0.2):
   #images, video, live video
   width = int(frame.shape[1] * scale) 
   height = int(frame.shape[0] * scale)

   dimensions = (width, height)

   return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('SAM_7586.JPG')
resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

vi = cv.VideoCapture('SAM_7069.MP4')
def Changeres(width,height):
   #only live video
   vid.set(3,width)
   vid.set(4,height)


vid= cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
      break
vid.release()
cv.destroyAllWindows()

