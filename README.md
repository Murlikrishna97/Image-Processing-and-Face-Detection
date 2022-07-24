# Image-Processing-and-Face-Detection

This project mainly focuses on Image Classification. Image classification is very significant for human-computer interaction. In this repository, we can see a method for face recognition from an image. In our framework, we pass an image to YOLO face analysis model which detects the face/faces in the image and gives relevant co-ordinates of the face in the image. Using the co-ordinates given by the model we crop the face from the image. The cropped image is further pre-processed by upscaling or downscaling the dimensions so as to have a uniform size throughout the dataset to be passed to the TensorFlow model for training.

This project is an end to end project wherein Flask app has been developed to host.
