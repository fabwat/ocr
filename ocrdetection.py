import time
from threading import Thread
import pytesseract
import cv2
# -------------------- OCR CLASS -----------------------------------------------------------------
class OCRWebCam():
    def __init__(self, capture):
               
        self.t_ocr = Thread(target=self.update_ocr, args=())
        self.t_ocr.daemon=True
        self.result=None
        self.capture = capture
        self.stopped = False
    
    def start(self):         
        self.t_ocr.start()
        
    def update_ocr(self):
        delay = 0.03 # delay value in seconds 
        while True :
            if self.stopped is True :
                break
            
            frame = self.capture.get()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
            # apply thresholding to preprocess the image
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]            
            gray = cv2.medianBlur(gray, 3)

            self.result = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)              
            time.sleep(delay)

            
    def get_ocr(self):      
        return self.result
   
    def stop(self):
        self.stopped = True
