import os
import keras as ks
import numpy as np
import model_params as params
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def load_and_prepare_image(image_path, target_size):
    img = ks.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = ks.preprocessing.image.img_to_array(img)
    img_array = np.array([img_array])
    return img_array


def predict_and_collect_results(model, image_array):
    prediction = model.predict(image_array)
    pred_label = (prediction > 0.5).astype("int32")[0][0]
    return pred_label, prediction[0][0]


def evaluate_model(model, test_dir, class_names, img_height, img_width):
    y_true = []
    y_pred = []
    y_prob = []

    for class_name in class_names:
        class_dir = os.path.join(test_dir, class_name)
        true_label = 0 if class_name.endswith('s') else 1

        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            img_array = load_and_prepare_image(
                image_path, (img_height, img_width))
            pred_label, prob = predict_and_collect_results(model, img_array)

            y_true.append(true_label)
            y_pred.append(pred_label)
            y_prob.append(prob)

            result = "Not healthy" if pred_label == 1 else "Healthy"
            print(
                f"Image: {image_path} - True Label: {true_label} - Prediction: "
                f"{pred_label}({result}) ({prob:.4f})")

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return accuracy, precision, recall, f1


def main():
    resnet_models = {}
    effnet_models = {}

    for fruit in params.FRUITS:
        resnet_model_path = f'resnet_model_{fruit}.keras'
        effnet_model_path = f'effnet_model_{fruit}.keras'

        if os.path.exists(resnet_model_path):
            resnet_models[fruit] = ks.models.load_model(resnet_model_path)

        if os.path.exists(effnet_model_path):
            effnet_models[fruit] = ks.models.load_model(effnet_model_path)

    for fruit in params.FRUITS:
        test_dir = os.path.join(params.DATASET_DIR, fruit, 'test')
        class_names = params.CLASSES[fruit]

        if fruit in resnet_models:
            print(f'\nTesting ResNet model for {fruit}')
            accuracy, precision, recall, f1 = evaluate_model(resnet_models[fruit], test_dir, class_names,
                                                             params.IMG_HEIGHT, params.IMG_WIDTH)
            print(
                f'\nResNet {fruit} - Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1 Score: {f1:.4f}')

        if fruit in effnet_models:
            print(f'\nTesting EfficientNet model for {fruit}')
            accuracy, precision, recall, f1 = evaluate_model(effnet_models[fruit], test_dir, class_names,
                                                             params.IMG_HEIGHT, params.IMG_WIDTH)
            print(
                f'\nEfficientNet {fruit} - Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1 Score: {f1:.4f}')


if __name__ == '__main__':
    main()
