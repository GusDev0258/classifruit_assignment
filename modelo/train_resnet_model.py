import keras as ks
from keras.applications import ResNet50V2
import model_params as params


def create_resnet_model(input_shape):
    model_resnet = ResNet50V2(weights='imagenet', include_top=False, input_shape=input_shape)
    x = model_resnet.output
    x = ks.layers.GlobalAveragePooling2D()(x)
    x = ks.layers.Dense(1, activation='sigmoid')(x)
    resnet_model = ks.Model(inputs=model_resnet.input, outputs=x)

    for layer in model_resnet.layers:
        layer.trainable = False

    resnet_model.compile(optimizer='adam', loss='binary_crossentropy',
                         metrics=['accuracy', ks.metrics.Recall(), ks.metrics.Precision(), ks.metrics.F1Score()])

    return resnet_model


def train_and_save_model(train_dataset, model_name):
    input_shape = (params.IMG_HEIGHT, params.IMG_WIDTH, 3)
    model = create_resnet_model(input_shape)

    history = model.fit(train_dataset, epochs=params.NUM_EPOCHS)
    model.save(f'{model_name}.keras')


for fruit in params.FRUITS:
    train_dataset = params.load_and_prepare_data(fruit, params.DATASET_DIR)
    model_name = f'resnet_model_{fruit}_v1'
    train_and_save_model(train_dataset, model_name)
