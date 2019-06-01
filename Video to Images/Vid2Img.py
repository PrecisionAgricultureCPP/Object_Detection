import cv2
from tkinter.filedialog import askopenfilename

filename = askopenfilename()
origTokens = filename.split('/')
origFile = origTokens[-1]
justNameTokens = origFile.split('.')
justName = justNameTokens[0]
print(justName)

video = cv2.VideoCapture(filename)
if not video.isOpened():
    print("file not valid")
    exit()
success, image = video.read()
count = 0
success = True
while success:
    cv2.imwrite(justName + "-frame%d.png" % count, image)
    success, image = video.read()
    print('Read a new frame: ', success)
    count += 1



