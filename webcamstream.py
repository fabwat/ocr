from threading import Thread
import cv2

# ---------- WEB CAM CLAS -------------------------------------------------------------------
class WebcamStream :
   
    def __init__(self, stream_id=0):
        self.stream_id = stream_id 

        self.video      = cv2.VideoCapture(self.stream_id)
        if self.video.isOpened() is False :            
            exit(0)
  
        self.ocr_txt=""
        
        self.cam_width  = self.video.get(3)  
        self.cam_height = self.video.get(4)     
            
  
        self.grabbed , self.frame = self.video.read()
        if self.grabbed is False :           
            exit(0)
       
        self.stopped = True
        
        self.t_cam = Thread(target=self.update, args=())
        self.t_cam.daemon = True 
        
   
    def start(self):
        self.stopped = False
        self.t_cam.start()
    
    def get_cam_dim(self):
        return (self.cam_width,self.cam_height)    
        
 
    def update(self):
        try:
            while True :
                if self.stopped is True :
                    break
                
                self.grabbed , self.frame = self.video.read()         
            
                if self.grabbed is False :
                    print('[Exiting] No more frames to read')
                    self.stopped = True
                    break 
                
            self.video.release()        

        except Exception as e:
            print(e)   
   
    def get(self):
        return self.frame
    

    def stop(self):
        self.stopped = True
