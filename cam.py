''' Takes photo and saves '''
import subprocess
import uuid

IMAGE_DIR = 'client-image'
COMMAND = 'raspistill -o {}'

def capture():
    ''' Captures photo and names it as param '''
    name = uuid.uuid4().hex
    subprocess.check_output(COMMAND.format(name), shell=True)
    return '{}/{}'.format(IMAGE_DIR, name)
    