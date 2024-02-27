"""
тестирование модели
эмоционального окраса текста
"""

from fastapi.testclient import TestClient

# импорт приложения из App.py
from Api import app


client = TestClient(app)


# тест 1
def test_predict_1():
    response = client.post(
        "/predict/",
        json={
            "text":
            """It was a wonderful journey.
            We have visited many beautiful places
            and seen many sightings! I am happy!"""
        },
    )
    json_data = response.json()
    # проверка ответа приложения
    assert response.status_code == 200
    # проверка правильности работы модели определения эмоц окраса текста
    assert json_data["Результат:"] == "позитивный :)"


# тест 2
def test_predict_2():
    response = client.post("/predict/", json={"text": "I hate traffic jams"})
    json_data = response.json()

    assert json_data["Результат:"] == "негативный (("


# тест 3
def test_predict_3():
    response = client.post("/predict/", json={"text": "Today spring has come"})
    json_data = response.json()

    assert json_data["Результат:"] == "нейтральный"
