import pyARIS
import cv2
from pyARIS import FrameRead

filename = '/home/gfernandez/post-doc/video_test/2017-08-30_015000.aris'

print("starting")

ARISdata, frame = pyARIS.DataImport(filename)

print("Frame count:", ARISdata.FrameCount)

frame = FrameRead(ARISdata, 56)

pyARIS.VideoExport(ARISdata, 'test_video.mp4', start_frame = 1, end_frame = 100, timestamp = True, fontsize=30, ts_pos = (10,1200))
pyARIS.SubtractorMOG2('test_video.mp4','test_video_filtered.mp4')
