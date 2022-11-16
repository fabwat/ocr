
import cv2


from ocrdetection import OCRWebCam as ocrwebcam
from webcamstream import WebcamStream as webcam
import faulthandler

# ----------  TASK OCR ------------------------------------------------------------------- -------------
def draw_ocr( frame, cam_stream):
    ocr_results=cam_stream.get_ocr()            
    if ( ocr_results != None ):
        for i in range(0, len(ocr_results['text'])):
        # extract the bounding box coordinates of the text region from
        # the current result
            text = ocr_results["text"][i]
            if( text != "" ):
                conf = int(ocr_results["conf"][i])
                            
                x = ocr_results["left"][i]
                y = ocr_results["top"][i]
                w = ocr_results["width"][i]
                h = ocr_results["height"][i]
                # extract the OCR text itself along with the confidence of the
                # text localization                   
                
                cv2.putText(frame, text, (x,y), cv2.FONT_HERSHEY_PLAIN,1, (255,0,0), 1, cv2.LINE_AA   )


       
def main_task():         
    icon_size = 68
    cam= webcam(0)
    cam.start()  
    
    ocr_stream = ocrwebcam(capture=cam) # 0 id for main camera
    ocr_stream.start()

    cv2.namedWindow("window")    
    
    while True :
        if cam.stopped is True :
            break
        else :            
            frame = cam.get()                          
                                        
        draw_ocr(frame, ocr_stream)
        
        cv2.imshow('window', frame)
   
        if(  cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == 27 ) :
            break
   
    cam.stop()  
    cv2.destroyAllWindows()


if __name__=="__main__": 
    faulthandler.enable()
    main_task()