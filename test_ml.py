import numpy as np
from ml.model import compute_model_metrics, inference, train_model


# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """ Test that train_model returns a trained model """
    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert model is not None


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    Test that inference returns once prediciton for each input row.
    """
    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    assert len(preds) == len(X_train)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test metrics using known labels and predicitions.
    """
    y = np.array([0, 0, 1, 1])
    preds = np.array([0, 0, 1, 1])

    p, r, fb = compute_model_metrics(y, preds)

    assert p == 1.0
    assert r == 1.0
    assert fb == 1.0
