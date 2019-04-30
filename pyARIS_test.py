import pyARIS
import cv2
from pyARIS import FrameRead

filename = '/home/gfernandez/post-doc/video_test/2017-08-30_015000.aris'

print("starting")

ARISdata, frame = pyARIS.DataImport(filename)

print("Frame count:", ARISdata.FrameCount)

frame = FrameRead(ARISdata, 56)

cv2.imshow('data',frame.remap)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#Uncomment the following line to test the VideoExport routine (ffmpeg based)
#pyARIS.VideoExport(ARISdata, 'test_video.mp4', start_frame = 1, end_frame = 100, timestamp = True, fontsize=30, ts_pos = (10,1200))
