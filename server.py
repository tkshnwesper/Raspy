''' Executes the command '''

import subprocess
import os
import sys
import threading
import time
import cherrypy
from label_image1 import process_image

IMAGE_DIRECTORY = "server-image"
# DOCKER_COMMAND = "python /tf_files/label_image1.py /tf_files/Raspy/server-image/{}"

JOBS = []
COMPLETED_JOBS = {}

class ThreadLoop(threading.Thread):
    def run(self):
        global JOBS, COMPLETED_JOBS
        from label_image1 import process_image
        while(True):
            if len(JOBS) == 0:
                time.sleep(1)
            else:
                fname = JOBS.pop()
                COMPLETED_JOBS[fname] = process_image(fname)

            

class Command(object):
    def __init__(self):
        self.firstTime = True

    @cherrypy.expose
    def analyse(self, imgname):
        global JOBS, COMPLETED_JOBS
        ''' executes command '''
        if self.firstTime:
            ThreadLoop().start()
            self.firstTime = False
        # result = subprocess.check_output(DOCKER_COMMAND.format(imgname), shell=True)
        ## delete file
        fname = '{}/{}'.format(IMAGE_DIRECTORY, imgname)
        JOBS.append(fname)
        while fname not in COMPLETED_JOBS.keys():
            pass
        result = COMPLETED_JOBS[fname]
        del COMPLETED_JOBS[fname]
        if os.path.exists(fname):
            os.remove(fname)
        return result

if __name__ == "__main__":
    from cherrypy.process import servers
    def fake_wait_for_occupied_port(host, port): return
    servers.wait_for_occupied_port = fake_wait_for_occupied_port
    # cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_timeout' : 60,
            'server.socket_port': 8080
        }
    }
    cherrypy.quickstart(Command(), '/', config)
