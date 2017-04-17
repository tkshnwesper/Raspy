import tensorflow as tf, sys
import os

# Unpersists graph from file
f = tf.gfile.FastGFile("/tf_files/retrained_graph.pb", 'rb')

def process_image(path):

    image_path = path

    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("/tf_files/retrained_labels.txt")]

    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        human_string = label_lines[top_k[0]]
        score = predictions[0][top_k[0]]
        print('%s %.1f' % (human_string, score))

    os.remove(image_path)

f.close()
