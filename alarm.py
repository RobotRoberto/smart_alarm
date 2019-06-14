from google.cloud import vision
from google.oauth2 import service_account
from picamera import PiCamera
from time import sleep

CRED_ERROR = \
    """
    Error: No service account credentials passed in. The Alarm class needs a
    Google Cloud Service Account with Vision API activated: look through the 
    following link. 
    """

SCOPE = 'https://www.googleapis.com/auth/cloud-platform'

class Alarm:

    def __init__(self, path=None):
        
        creds = service_account.Credentials.from_service_account_file(path)
        scoped_credentials = creds.with_scopes([SCOPE])
        self.client = vision.ImageAnnotatorClient(credentials=creds)


        self.camera = PiCamera()

    def take_a_picture(self):
        sleep(1)
        self.camera.capture('pic.jpg')
