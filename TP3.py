import cv2
import numpy as np

image_path = "image072.png"
image2_path = "image092.png"
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
img2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

point1 = (0,0)
point2 = (0,0)
target = (0,0)
k = 50

def draw_rect(event, x, y, flags, param):
    global points
    global point1 , point2, target
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv2.rectangle(
            img,
            point1, point2,
            (0, 0, 255),
            2,
        )
        cv2.rectangle(
            img,
            (point1[0]-k, point1[1]-k),
            (point2[0]+k, point2[1]+k),
            (0, 255, 0),
            2,
        )
        
        rouge = [
            point1[0],
            point1[1],
            point2[0],
            point2[1],
        ]

        vert = [
            point1[0]-k,
            point1[1]-k,
            point2[0]+k,
            point2[1]+k,
        ]

        w_r = rouge[2] - rouge[0]
        h_r = rouge[3] - rouge[1]

        r_area = img[rouge[1]:rouge[3], rouge[0]:rouge[2]]# image slicing
        v_area = img2[vert[1]:vert[3], vert[0]:vert[2]]

        min_mse = float('inf')

        for y in range(v_area.shape[0] - h_r):
            for x in range(v_area.shape[1] - w_r):
                block = v_area[y:y + h_r, x:x + w_r]  
                mse = np.sum((r_area.astype("float") - block.astype("float")) ** 2)
                mse /= float(w_r * h_r)
                if mse < min_mse:
                    min_mse = mse
                    target = (x+vert[0],y+vert[1])
        print(target)
        cv2.rectangle(
            img2,
            target,
            (target[0]+w_r, target[1]+h_r),
            (255, 0, 255),
            2,
        )
        cv2.imshow("image2", img2)

        

    
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_rect)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
