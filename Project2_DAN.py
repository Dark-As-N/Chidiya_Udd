import time
import cv2


cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.read()
new = time.time() + 3
  
buffer = []
prev_frame_time = 0
new_frame_time = 0
text = ''
sf = 1.5


def capture_motion(list2):
    buffer = []
    prev_frame_time = 0
    new_frame_time = 0
    text = ''
    sf = 1.5
    for i in range(1):
        ret1,frame1= cap.read()
        frame1 = cv2.resize(frame1, (int(frame1.shape[1] * sf), int(frame1.shape[0] * sf)))
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
        buffer.append(gray1)

    a = time.time() + 1.5
    while(time.time() < a):
        global camera_closed
        ret2,frame2=cap.read()
        #print("dsbah")
        frame2 = cv2.resize(frame2, (int(frame2.shape[1] * sf), int(frame2.shape[0] * sf)))
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
        deltaframe = cv2.absdiff(buffer[0], gray2)
        buffer.append(gray2)
        buffer[:] = buffer[1:]
        #cv2.imshow('delta',deltaframe)
        threshold = cv2.threshold(deltaframe, 50, 255, cv2.THRESH_BINARY)[1]
        #cv2.imshow('threshold',threshold)
    
    
        countour,heirarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in countour:
            if cv2.contourArea(i) < 20:
                continue
            (x, y, w, h) = cv2.boundingRect(i)
            mid = (int) (x + h/2)
        
            if (mid < 320):
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
                frame2 = cv2.putText(frame2, "1", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                list2[0] = 1

          
          
            elif (mid < 640):
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame2 = cv2.putText(frame2, "2", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                list2[1] = 1

          
            elif (mid>640):
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                frame2 = cv2.putText(frame2, "3", (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                list2[2] = 1
        frame2 = cv2.putText(frame2, text, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('window',frame2)
        if cv2.waitKey(1) == ord('q'):
            camera_closed = True
            cv2.destroyAllWindows()
            cap.release()
            break
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time 
        text = 'FPS ' + str(round(fps, 1))
    return list2

list3 = [0,0,0]
camera_closed = False
while camera_closed == False :
    x=time.time()
    print('Be Ready')
    time.sleep(0)
    print(capture_motion(list3))
    y=time.time()
    print(y-x)    
    list3 = [0,0,0]
#print(time.time(), new)
#while(time.time() < new):
#    list3 = motion_detector(list3)

cv2.destroyAllWindows()