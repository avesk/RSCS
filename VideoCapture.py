import cv2 as cv

class VideoCapture(cv.VideoCapture):
    '''Subclass class of cv2.VideoCapture implemented
    to simplify the interface for this Applications
    VideoCapturing requirements
    '''
    def __init__(self, fps=30):
        super().__init__(0)
        self.set_frame_rate(fps)

    def set_frame_rate(self, fps):
        '''Sets the framerate of capture object

        Params:
            fps (float) : framerate in frames per second
        '''
        self.set(
            int(self.get(cv.CAP_PROP_FPS)), 
            fps
        )
    
    def capture(self):
        '''Captures next frame, and returns a .JPG encoded 
        image
        
        Returns jpg (obj) : encoded jpg object
        '''
        _, frame = self.read()
        _, jpg = cv.imencode('.jpg', frame)
        return jpg
    
    def get_frame_rate(self):
        return self.get(cv2.CAP_PROP_FPS)
