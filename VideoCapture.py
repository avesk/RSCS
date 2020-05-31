import cv2 as cv

class VideoCapture(cv.VideoCapture):
    '''Subclass class of cv2.VideoCapture implemented
    to simplify the interface for this Applications
    VideoCapturing requirements
    '''
    def __init__(self, fps=30, res=(1920,1080)):
        super().__init__(0)
        self.set_resolution(res)

    def set_frame_rate(self, fps):
        '''Sets the framerate of capture object

        @todo investigate if this has any affect on PiCam
        streaming.

        Params:
            fps (float) : framerate in frames per second
        '''
        self.set(cv.CAP_PROP_FPS, fps)
    
    def set_resolution(self, resolution):
        '''Sets the frameresolution rate of capture object

        Params:
            resolution (tuple(int)) : WxH resolution
        '''
        w, h = resolution
        self.set(cv.CAP_PROP_FRAME_WIDTH, w)
        self.set(cv.CAP_PROP_FRAME_HEIGHT, h)
    
    def capture(self):
        '''Captures next frame, and returns a .JPG encoded 
        image
        
        Returns jpg (obj) : encoded jpg object
        '''
        _, frame = self.read()
        _, jpg = cv.imencode('.jpg', frame)
        return jpg
    

