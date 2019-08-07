from google.cloud import vision
from google.oauth2 import service_account
from picamera import PiCamera
from time import sleep
import datetime
import os, io

CRED_ERROR = \
    """
    Error: No service account credentials passed in. The Alarm class needs a
    Google Cloud Service Account with Vision API activated: look through the 
    following link. 
    """

SCOPE = 'https://www.googleapis.com/auth/cloud-platform'
PEOPLE_NOT_FOUND = "Google Vision API did not find any person"

PEOPLE_LABELS = set(['Arm', 'Leg', 'Waist', 'Face', 'Man', 'Woman', 
    'Shoulder', 'Hand', 'Eye', 'Nose', 'Mouth', 'Human'
    ])

class Alarm:

    def __init__(self, path=None):
        """
        Sets up the credentials for the Google Cloud Platform and API service
        with the camera module
        """
        creds = service_account.Credentials.from_service_account_file(path)
        scoped_credentials = creds.with_scopes([SCOPE])
        self.client = vision.ImageAnnotatorClient(credentials=creds)

        # Initializes the PiCamera
        self.camera = PiCamera()

    def take_a_picture(self):
        """
        Takes a picture and stores the result in the /pictures sub-directory,
        used for debugging
        """
        dir_name = os.path.dirname(__file__) + '/pictures/' 
        
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        file_name = dir_name + str(datetime.datetime.now()) + '.jpg'
        self.camera.capture(file_name, format='jpeg')

    def find_people_in_feed(self):
        """
        Finds if Vision API labels any human body parts in the picture,
        returns true if so.
        """
        labels = []
        
        with io.BytesIO() as stream:
           self.camera.capture(stream, format='jpeg')
           content = stream.getvalue()
           response = self.client.label_detection({
                'content': content,
           })
        
           labels = response.label_annotations

        for label in labels:
            if label.description in PEOPLE_LABELS:
                return True

        print(PEOPLE_NOT_FOUND)
        return False
