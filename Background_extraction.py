
'''
This script exctracts the background from the moving object frames.

The technique used is averaging the frames using the command
        cv2.accumulateWeighted(src, dst, alpha[, mask]) → None
            Parameters:
                src – Input image as 1- or 3-channel, 8-bit or 32-bit floating point.
                dst – Accumulator image with the same number of channels as input image, 32-bit or 64-bit floating-point.
                alpha – Weight of the input image.
                mask – Optional operation mask.

        averageValue = np.float32(imS)

        The function calculates the weighted sum of the input image src and the accumulator dst so that dst becomes a running average of a frame sequence:
        dst(x,y) <- (1- alpha) * dst(x,y) + alpha * src(x,y)

'''

print("\n\n\nHello World!\n\n\n")
import cv2
import matplotlib.pyplot as plt
import numpy as np
# empty list to store the frames
col_images=[]
RESULT_IMGS = []

#Step_1 : Capture the Video frames
cap = cv2.VideoCapture('cut.mp4')

#Steps 2 :Read the frames from the video_frames
ret, frame = cap.read()

# Step 3 : Pre-process the frames (optional)
frame_resize = cv2.resize(frame, (960, 540))
averageValue = np.float32(frame_resize)

video_name = 'Output_video.avi'

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Step_4 Read until video is completed
#      and calculate the accumulateWeighteds average of all frames
while (cap.isOpened()):

    # Read images frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        frame_resize = cv2.resize(frame, (960, 540))                    # Resize image
        col_images.append(frame_resize)

        #Step_5 Calculates the running average over the input image
        cv2.accumulateWeighted(frame_resize, averageValue, 0.01)

        resultingFrames1 = cv2.convertScaleAbs(averageValue)

        # Save image frames for later use
        RESULT_IMGS.append(resultingFrames)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

#Step_6 : Save the resulted frames as a Video output
height, width, layers = frame_resize.shape
fourcc = 0
video = cv2.VideoWriter(video_name,  0, 30, (width, height))

for image in RESULT_IMGS:
    video.write(image)

#Step 7 Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
