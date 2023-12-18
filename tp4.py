import cv2
import numpy as np

im1 = cv2.imread('image072.png')
im2 = cv2.imread('image092.png')

block_size = 16
result_image = im2.copy()

mse_values = []
for y in range(0, im2.shape[0] - block_size, block_size):
    for x in range(0, im2.shape[1] - block_size, block_size):
        
        block2 = im2[y:y+block_size, x:x+block_size]
        block1 = im1[y:y+block_size, x:x+block_size]
        mse = np.sum((block1 - block2) ** 2) / float(block1.size)
        
        mse_values.append(mse)

mse_mean = np.mean(mse_values)
mse_std = np.std(mse_values)
threshold_multiplier = 2 
mse_threshold = mse_mean + threshold_multiplier * mse_std
print(mse_threshold)

for y in range(0, im2.shape[0] - block_size, block_size):
    for x in range(0, im2.shape[1] - block_size, block_size):
        
        block2 = im2[y:y+block_size, x:x+block_size]
        block1 = im1[y:y+block_size, x:x+block_size]
        mse = np.sum((block1 - block2) ** 2) / float(block1.size)

        if mse > mse_threshold:
            cv2.rectangle(result_image,
                          (x, y), 
                          (x+block_size, y+block_size), 
                          (0, 0, 255), 
                          2)

cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()






   