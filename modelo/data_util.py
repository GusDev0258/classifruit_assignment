import os
from keras.src.legacy.preprocessing.image import ImageDataGenerator
import model_params as params
import keras as ks
import shutil
import random

def count_images(directory):
    return sum([len(files) for r, d, files in os.walk(directory)])

def generate_augmented_images(source_dir, target_dir, num_augmented_images, datagen):
    generator = datagen.flow_from_directory(
        source_dir,
        target_size=(params.IMG_HEIGHT, params.IMG_WIDTH),
        batch_size=1,
        class_mode=None,
        shuffle=True
    )

    i = 0
    for batch in generator:
        if i >= num_augmented_images:
            break
        img_path = os.path.join(target_dir, f'aug_{i}.png')
        ks.preprocessing.image.save_img(img_path, batch[0])
        i += 1

def balance_classes(source_dir, class_a, class_b):
    class_a_dir = os.path.join(source_dir, class_a)
    class_b_dir = os.path.join(source_dir, class_b)

    count_class_a = count_images(class_a_dir)
    count_class_b = count_images(class_b_dir)

    if count_class_a < count_class_b:
        num_augmented_images = count_class_b - count_class_a
        generate_augmented_images(source_dir, class_a_dir, num_augmented_images, datagen)
    elif count_class_b < count_class_a:
        num_augmented_images = count_class_a - count_class_b
        generate_augmented_images(source_dir, class_b_dir, num_augmented_images, datagen)

def split_data(source_dir, train_dir, test_dir, split_ratio=0.8):
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    for class_name in os.listdir(source_dir):
        class_source_dir = os.path.join(source_dir, class_name)

        if class_name in ['train', 'test']:
            continue

        class_train_dir = os.path.join(train_dir, class_name)
        class_test_dir = os.path.join(test_dir, class_name)

        if not os.path.exists(class_train_dir):
            os.makedirs(class_train_dir)
        if not os.path.exists(class_test_dir):
            os.makedirs(class_test_dir)

        images = os.listdir(class_source_dir)
        random.shuffle(images)
        split_point = int(len(images) * split_ratio)

        train_images = images[:split_point]
        test_images = images[split_point:]

        for image in train_images:
            src = os.path.join(class_source_dir, image)
            dst = os.path.join(class_train_dir, image)
            try:
                shutil.copyfile(src, dst)
            except PermissionError as e:
                print(f"Permission denied: {e} for file {src}")

        for image in test_images:
            src = os.path.join(class_source_dir, image)
            dst = os.path.join(class_test_dir, image)
            try:
                shutil.copyfile(src, dst)
            except PermissionError as e:
                print(f"Permission denied: {e} for file {src}")

dataset = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=params.ROTATION_RANGE,
    width_shift_range=params.WIDTH_SHIFT_RANGE,
    height_shift_range=params.HEIGHT_SHIFT_RANGE,
    shear_range=params.SHEAR_RANGE,
    zoom_range=params.ZOOM_RANGE,
    horizontal_flip=params.HORIZONTAL_FLIP,
    fill_mode=params.FILL_MODE,
)

for fruit in params.FRUITS:
    fruit_dir = os.path.join(params.DATASET_DIR, fruit)
    train_dir = os.path.join(params.DATASET_DIR, f"{fruit}/train")
    test_dir = os.path.join(params.DATASET_DIR, f"{fruit}/test")
    class_a, class_b = params.CLASSES[fruit]

    balance_classes(fruit_dir, class_a, class_b)
    split_data(fruit_dir, train_dir, test_dir)
