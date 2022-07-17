from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from yoloface import face_analysis
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pickle
import os

size = (60, 40, 3)

model_path = "../Model_test_acc_95.70_Image_size_60x40_Mar31.pkl"
UPLOADS_ROOT_DIR = './Uploads/'
image_path = ""

label_reverse_lookup = {
    0: 'Sanna Marin',
    1: 'Narendra Modi',
    2: 'Vladimir Putin',
    3: 'Tsai Ing-wen',
    4: 'Iván Duque Márquez',
    5: 'Alberto Fernández',
    6: 'Joe Biden',
    7: 'Felix Tshisekedi',
    8: 'Jacinda Ardern',
    9: 'Carlos Alvarado Quesada'
}

pkl_file = open(model_path, 'rb')

model = pickle.load(pkl_file)
pkl_file.close()

# Create server object
app = Flask(__name__, template_folder=".")
app.config['UPLOAD_FOLDER'] = UPLOADS_ROOT_DIR


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def get_index_html():
    file = open('./Index/index.html', 'r')
    data = file.read()
    file.close()
    return data


@app.route('/index.css', methods=['GET'])
def get_index_css():
    file = open('./Index/index.css', 'r')
    data = file.read()
    file.close()
    return data


@app.route('/index.js', methods=['GET'])
def get_index_js():
    file = open('./Index/index.js', 'r')
    data = file.read()
    file.close()
    return data


@app.route('/Sanna_Marin_0.jpg', methods=['GET'])
def get_index_sana_marine():
    file = open('./Photos/Sanna_Marin_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Finland.jpg', methods=['GET'])
def get_index_finland():
    file = open('./Photos/Finland.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Alberto_Fernández_0.jpg', methods=['GET'])
def get_index_alberto():
    file = open('./Photos/Alberto_Fernández_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Argentina.png', methods=['GET'])
def get_index_argentina():
    file = open('./Photos/Argentina.png', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Carlos_Alvarado_Quesada_2.jpg', methods=['GET'])
def get_index_carlos():
    file = open('./Photos/Carlos_Alvarado_Quesada_2.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Costa_Rica.jpg', methods=['GET'])
def get_index_cost_rica():
    file = open('./Photos/Costa_Rica.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Felix_Tshisekedi_6.jpg', methods=['GET'])
def get_index_felix():
    file = open('./Photos/Felix_Tshisekedi_6.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/DRC.jpg', methods=['GET'])
def get_index_drc():
    file = open('./Photos/DRC.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Iván_Duque_Márquez_0.jpg', methods=['GET'])
def get_index_ivan():
    file = open('./Photos/Iván_Duque_Márquez_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Columbia.jpg', methods=['GET'])
def get_index_columbia():
    file = open('./Photos/Columbia.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Jacinda_Ardern_0.jpg', methods=['GET'])
def get_index_jacinda():
    file = open('./Photos/Jacinda_Ardern_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/NZ.jpg', methods=['GET'])
def get_index_nz():
    file = open('./Photos/NZ.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Joe_Biden_1.jpg', methods=['GET'])
def get_index_joe():
    file = open('./Photos/Joe_Biden_1.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/USA.jpg', methods=['GET'])
def get_index_usa():
    file = open('./Photos/USA.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Narendra_Modi_0.jpg', methods=['GET'])
def get_index_narendra():
    file = open('./Photos/Narendra_Modi_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/India.jpg', methods=['GET'])
def get_index_india():
    file = open('./Photos/India.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Tsai_Ing-wen_0.png', methods=['GET'])
def get_index_tsai():
    file = open('./Photos/Tsai_Ing-wen_0.png', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Taiwan.png', methods=['GET'])
def get_index_taiwan():
    file = open('./Photos/Taiwan.png', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/background_0.jpg', methods=['GET'])
def get_index_background_0():
    file = open('./Photos/background_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Vladimir_Putin_0.jpg', methods=['GET'])
def get_index_vladimir():
    file = open('./Photos/Vladimir_Putin_0.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/Russia.jpg', methods=['GET'])
def get_index_russia():
    file = open('./Photos/Russia.jpg', 'rb')
    data = file.read()
    file.close()
    return data


@app.route('/predict.html', methods=['POST'])
def get_predict_html():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = UPLOADS_ROOT_DIR + filename
    face = predict(path)
    global image_path
    image_path = path
    return render_template('./Prediction/predict.html', label=face)


@app.route('/predict.css', methods=['GET'])
def get_predict_css():
    print(image_path.split('/')[-1])
    return render_template('./Prediction/predict.css', image=image_path)


@app.route(f"/{image_path}", methods=['GET'])
def get_image():
    file = open(image_path, 'rb')
    data = file.read()
    file.close()
    return data


# @app.route('/predict.html', methods=['POST'])
# def get_predict_html():
#     file = request.files['file']
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     images = get_face(UPLOADS_ROOT_DIR + filename)
#
#     if images.shape[0] == 0:
#         return "Zero faces detected in image please provide image with visible face"
#
#     print(images.shape)
#
#     predictions = model.predict(images)
#     print(len(predictions))
#
#     ret_str = ""
#     for i in range(len(predictions)):
#         # plt.imsave(f'{UPLOADS_ROOT_DIR}/{i}.jpg', images[i])
#
#         prediction = np.argmax(predictions[i])
#         probability = np.max(predictions[i])
#         ret_str += f"Prediction = {label_reverse_lookup[prediction]}, Probability = {probability * 100:.2f}%"
#     return ret_str


def predict(path):
    images = get_face(path)

    if images.shape[0] == 0:
        return "Zero faces detected in image please provide image with visible face"

    print(images.shape)

    predictions = model.predict(images)
    print(len(predictions))

    ret = []
    for i in range(len(predictions)):
        # plt.imsave(f'{UPLOADS_ROOT_DIR}/{i}.jpg', images[i])

        prediction = np.argmax(predictions[i])
        probability = np.max(predictions[i])
        # ret_str += f"Prediction = {label_reverse_lookup[prediction]}, Probability = {probability * 100:.2f}%"
        ret.append(label_reverse_lookup[prediction])
    return "The image is of " + " & ".join(ret)


def crop_image(path):
    face = face_analysis()
    img, boxes, confs = face.face_detection(image_path=path, model='full')
    imgs = []
    for box in boxes:
        x, y, h, w = box
        tmp = img[y:y + h, x:x + w]
        imgs.append(tmp)
    return imgs, confs


def get_face(path):
    imgs, confs = crop_image(path)

    print(f"inside get face 1: {len(imgs)}")
    images = []
    weird_size = size[1], size[0]
    for img in imgs:
        try:
            if size[0] < img.shape[0] and size[1] < img.shape[1]:
                # This is For shrinking an Image
                tmp = cv2.resize(img, weird_size, interpolation=cv2.INTER_AREA)
            elif size[0] > img.shape[0] and size[1] > img.shape[1]:
                # This is for Enlarging an image
                tmp = cv2.resize(img, weird_size, interpolation=cv2.INTER_CUBIC)
            else:
                # This is default behaviour
                tmp = cv2.resize(img, weird_size)

            images.append(tmp)
        except Exception as msg:
            print(f"{msg}\n{img.shape}")

    images = np.asarray(images, dtype=np.uint8)
    return images


app.run(host="0.0.0.0", debug=True)
