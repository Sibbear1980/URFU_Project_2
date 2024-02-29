from fastapi import FastAPI
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

app = FastAPI()
tokenizer = BertTokenizerFast.from_pretrained(
    "blanchefort/rubert-base-cased-sentiment"
    )
model = AutoModelForSequenceClassification.from_pretrained(
    "blanchefort/rubert-base-cased-sentiment", return_dict=True
)
result = ["нейтральный", "позитивный :)", "негативный (("]


@app.post("/predict/")  # адрес для вызова модели методом post
# функция для расчета модели
# в "input" передаётся текст
def predict(input: dict) -> dict:
    inputs = tokenizer(
        input["text"],
        max_length=512,
        padding=True,
        truncation=True,
        return_tensors="pt",
    )
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    # формируем результат
    output = {
        "Исходный текст": input["text"],
        "Результат:": result[int(predicted[0])]
        }
    return output
