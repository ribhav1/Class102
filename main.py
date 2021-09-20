import cv2
import time
import random
import dropbox

start_time = time.time()

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def take_snapshot():
    number = random.randint(0, 100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = VideoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
    return img_name
    print("Snapshot taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_picture(img_name):
    access_token = ""
    file = img_name
    file_from = file
    file_to = "/test_folder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("Files uploaded")

def main():
    while (True):
        if time.time() - start_time >= 5:
            name = take_snapshot()
            upload_picture(name)

main()