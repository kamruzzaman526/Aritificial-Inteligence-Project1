import cv2
from simple_facerec import SimpleFacerec
import datetime
from datetime import datetime

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

def attend(name,day,today):
    with open('attend.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        # print("Day",day)
        # print("today",today)
        # daylist = []
    #     daylist.insert(0,day)
        # print(daylist[0])
        if(day != today):
            nameList.clear()
            # myDataList.clear()
            # for line in myDataList:
            #     myDataList.clear()
            #     entry = line.split(",")
            #     # nameList.remove(entry[0])

               
            # print(nameList)

        
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])
            # print(nameList)

        if name not in nameList:
               
            # count = 1
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            date = now.strftime('%d-%m-%y')
            f.writelines(f'\n{name},{time},{date}')
            # yt = day
        # else:
            
        #     print(k)
        #     k = k+1
            # now = datetime.now()
            # time = now.strftime('%H:%M:%S')
            # date = now.strftime('%d-%m-%y')
            # f.writelines(f'\n{name},{time},{date},{k}')
            # print
            # ct =1
            # ct = ct +1
            # now = datetime.now()
            # time = now.strftime('%H:%M:%S')
            # date = now.strftime('%d-%m-%y')
            # f.writelines(f'\n{name},{time},{date},{count}')



# attend("chopol")

before = ""
today = ""
while True:
    ret, frame = cap.read()
   
    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 0, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (200, 0, 0), 2)

        # before = name
        # show name

        now = datetime.now()
        da = now.strftime("%d")

        if(name != before):
            print(name, " ", now.strftime("%H:%M:%S %d-%m-%y"))
            day = now.strftime("%d")
            # print (day)
            attend(name,day,today)
            before=name
            today = da
            



    cv2.imshow("Frame1", frame)
    

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()