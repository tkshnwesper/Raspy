''' Executes the command '''

import subprocess
import os
import sys
import threading
import time
import cherrypy
import tensorflow as tf

IMAGE_DIRECTORY = "server-image"
# DOCKER_COMMAND = "python /tf_files/label_image1.py /tf_files/Raspy/server-image/{}"

JOBS = []
COMPLETED_JOBS = {}

class ThreadLoop(threading.Thread):
    def run(self):
        global JOBS, COMPLETED_JOBS
        from label_image1 import process_image
        # Unpersists graph from file
        f = tf.gfile.FastGFile("/home/nitin/tf_files/retrained_graph.pb", 'rb')
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
        label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("/home/nitin/tf_files/retrained_labels.txt")]
        with tf.Session() as sess:
            while(True):
                if len(JOBS) == 0:
                    time.sleep(1)
                else:
                    fname = JOBS.pop()
                    COMPLETED_JOBS[fname] = process_image(fname, label_lines, sess)

            

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
            # time.sleep(5)
        # result = subprocess.check_output(DOCKER_COMMAND.format(imgname), shell=True)
        ## delete file
        fname = '{}/{}'.format(IMAGE_DIRECTORY, imgname)
        # fname = 'img.jpg'
        JOBS.append(fname)
        while fname not in COMPLETED_JOBS.keys():
            pass
        result = COMPLETED_JOBS[fname]
        del COMPLETED_JOBS[fname]
        if os.path.exists(fname):
            os.remove(fname)
        print
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
