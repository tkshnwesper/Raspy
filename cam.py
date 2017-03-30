''' Takes photo and saves '''
import subprocess
import uuid
import os

IMAGE_DIR = 'client-image'
COMMAND = 'raspistill -o {}'

def capture():
    ''' Captures photo and names it as param '''
    name = uuid.uuid4().hex
    loc = os.path.join(IMAGE_DIR, name)
    subprocess.check_output(COMMAND.format(loc), shell=True)
    return loc
