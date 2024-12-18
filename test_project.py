import pytest
from project import predict, model_test, print_model_details, model


def test_predict():
    result = predict(100)
    assert "Predicted price:" in result
    assert isinstance(float(result.split(":")[1]), float)


def test_model_test():
    r2 = model_test()
    assert isinstance(r2, float)
    assert 0 <= r2 <= 1


def test_print_model_details(capsys):
    print_model_details()
    captured = capsys.readouterr()
    assert "Model Coefficient:" in captured.out
    assert "Model Intercept:" in captured.out

    coef = float(captured.out.split("Coefficient:")[1].split("\n")[0])
    intercept = float(captured.out.split("Intercept:")[1].split("\n")[0])
    assert isinstance(coef, float)
    assert isinstance(intercept, float)
