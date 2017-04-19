import tensorflow as tf, sys
import os



def process_image(path, label_lines, sess):

    image_path = path

    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
        # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    human_string = label_lines[top_k[0]]
    score = predictions[0][top_k[0]]
    return '%s %.1f' % (human_string, score)

    # os.remove(image_path)

# f.close()
