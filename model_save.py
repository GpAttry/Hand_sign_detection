from keras.models import model_from_json
from keras.preprocessing import image
model = model_from_json(open("model1.json", "r").read())
model.load_weights('weights.h5')
print(model.summary())