import cv2 as cv

class VideoCapture(cv.VideoCapture):
    '''Subclass class of cv2.VideoCapture implemented
    to simplify the interface for this Applications
    VideoCapturing requirements
    '''
    _1080p = (1920, 1080)
    _720p = (1280, 720)
    _480p = (480, 640)

    def __init__(self, res=_1080p):
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
    
    def capture(self, fps=None):
        '''Captures next frame, and returns a .JPG encoded 
        image
        
        Returns jpg (obj) : encoded jpg object
        '''

        _, frame = self.read()
        texted_image =cv.putText(
            img=frame, text=f"{fps}", org=(200,200),
            fontFace=3, fontScale=3, color=(0,0,255), thickness=5
        )
        _, jpg = cv.imencode('.jpg', frame)

        return jpg
    

