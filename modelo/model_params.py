import os
import keras as ks
import random

IMG_HEIGHT = 300
IMG_WIDTH = 300
BATCH_SIZE = 24
NUM_EPOCHS = 101

ROTATION_RANGE = 40,
WIDTH_SHIFT_RANGE = 0.2,
HEIGHT_SHIFT_RANGE = 0.2,
SHEAR_RANGE = 0.2,
ZOOM_RANGE = 0.2,
HORIZONTAL_FLIP = True,
FILL_MODE = 'nearest'

STRAWBERRY_DIR = '.././dataset_ajustado/morangos'
PEACH_DIR = ".././dataset_ajustado/pessegos"
POMEGRANATE_DIR = ".././dataset_ajustado/romas"
DATASET_DIR = ".././dataset_ajustado/"

FRUITS = ['morangos', 'pessegos', 'romas']
CLASSES = {
    'morangos': ['ms', 'mp'],
    'pessegos': ['ps', 'pp'],
    'romas': ['rs', 'rp']
}


def load_and_prepare_data(fruit, base_dir):
    train_data_dir = os.path.join(base_dir, fruit, 'train')
    print(train_data_dir)
    train_dataset = ks.utils.image_dataset_from_directory(
        directory=train_data_dir,
        batch_size=BATCH_SIZE,
        shuffle=True,
        image_size=(IMG_HEIGHT, IMG_WIDTH),
        labels='inferred',
        label_mode='binary',
        class_names=CLASSES[fruit]
    )
    return train_dataset
