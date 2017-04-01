''' Executes the command '''

import cherrypy

IMAGE_DIRECTORY = "server-image"
DOCKER_COMMAND = "dir"

class Command(object):
    @cherrypy.expose
    def index(self, imgname):
        ''' executes command '''
        result = subprocess.check_output(DOCKER_COMMAND.format(imgname), shell=True)
        delete file
        if os.path.exists(fname):
            os.remove(fname)