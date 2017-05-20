''' Takes photo and saves '''
import subprocess
import uuid
import os
from picamera import PiCamera

IMAGE_DIR = 'client-image'
# COMMAND = 'raspistill -o {}'

def capture():
    ''' Captures photo and names it as param '''
    name = uuid.uuid4().hex + '.jpeg'
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    loc = os.path.join(IMAGE_DIR, name)
    # subprocess.check_output(COMMAND.format(loc), shell=True)
    with PiCamera() as camera:
        camera.capture(loc)
    return loc

if __name__ == '__main__':
    print(capture())