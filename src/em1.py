
import cv2

from src.yoga import maincode

cap = cv2.VideoCapture(0)


def camclick():
    i=0
    while(True):
        try:
            ret, img = cap.read()
            cv2.imwrite("sample.jpg",img)
            res=maincode("sample.jpg")
            if res == 'na':
                cv2.putText(img, res, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                cv2.imshow('img', img)
            else:
                img=cv2.imread("output.jpg")
                cv2.imshow('img', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
                break

            # kill open cv things
        except:
            pass
    cap.release()
    cv2.destroyAllWindows()
            # 	pass
        # return emotion
            #write emotion text above rectangle

# camclick()