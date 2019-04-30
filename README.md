## pyARIS

This package provides an interface between python and ARIS files.

This version of the package provides the basis for the data treatement and ML analysis developed by G. Fernandez Garcia

###Additional sources of information:

Soundmetrics GitHub Repo.: https://github.com/SoundMetrics

Original pyARIS Repo.: https://github.com/EminentCodfish/pyARIS

Currently this packages has only been tested with the ARIS Explorer 3000
in 128 beam mode.  It should work with other versions, but they have yet to 
be tested.  This package currently doesn't support the tele-photo len.

### Requirements
* Python (2.7.10)
* Numpy (1.10.1) 
* PIL (1.1.7)
* tqdm (4.11.2)
* Pytz (2015.4)
* ffmpeg (Optional for exporting to video)

Soon it will be compatible with Py3 and Py3.7

### Getting Started

#### Importing package and opening a file.

The script "pyARIS_test.py" can be run (commenting the various sections) in order to test
the different functionalities of pyARIS.

```python
	import pyARIS
        from pyARIS import FrameRead
	filename = '~/Test_file.aris'
	ARISdata, frame = pyARIS.DataImport(filename)
```

The DataImport function opens the aris file, mines the metadata, populates the ARISdata
data structure.  It then opens the first file, populates the frame data structure with the
frame metadata and raw data.  A look-up table is created to remap the data from the raw
data structure (i.e. beam number and bin number) to a real-world mapping.  

Additional arguments:
startFrame: The first frame to be populated into the data structure (Default = 1). 
frameBuffer: Adds a specified number of pixels to be added to the remapped frame.
	Primarily for display purposes.

#### Retrieving Frame Data

Once the data file has been opened, specific frames can be loaded. It is important
to notice that the real-world mappin is done by FrameRead

```python
	frame = pyARIS.FrameRead(ARISdata, 2)
```

This methods could be used with a loop to iterate through the frames in the file. 

```python
	for i in range(ARISdata.FrameCount):
        frame = FrameRead(ARISdata, i)
```

Additional arguments: 
frameBuffer: Adds a specified number of pixels to be added to the remapped frame.
	Primarily for display purposes.

####Using the ARIS data
At this point the data can be passed into different packages.  To view and save
the remapped image with matplotlib:

```python
	import matplotlib.pyplot as plt
	plt.imshow(frame.remap, origin = "lower", vmin = 0, vmax = 255)
	plt.savefig('frame.png', bbox_inches = 'tight', pad_inches = 0.25)
	plt.show()
```

To view using PIL
```python
	from PIL import Image
	im = Image.fromarray(frame.remap)
	im.show()
```

The data is OpenCV compatable.  To view:
```python
	import cv2
	cv2.imshow('data',frame.remap)
	cv2.waitKey(5000)
	cv2.destroyAllWindows()
```

#### Exporting video
The VideoExport() method utilizes FFMpeg to pipe the frame data into a MP4 container.
If FFMpeg is not in your filepath then I typically put the FFMpeg.exe file in the 
working directory.  An optional timestamp argument will place the sonar timestamp on 
the frame.  Timestamp parameters include the fontsize and position (ts_pos).

To implement:
```python
	pyARIS.VideoExport(data, 'test_video.mp4', start_frame = 10, end_frame = 50, timestamp = True, fontsize=30, ts_pos = (10,1200))
```
