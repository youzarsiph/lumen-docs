""" AI Model """

from transformers import pipeline


summarizer = pipeline(
    task="summarization",
    model="google-t5/t5-small",
    framework="pt",
    max_length=1024,
    truncation=True,
)
translator = pipeline(
    task="translation_XX_to_YY",
    model="google-t5/t5-small",
    framework="pt",
    max_length=1024,
    truncation=True,
)
question_answerer = pipeline(
    task="question-answering",
    model="google-t5/t5-small",
    framework="pt",
    max_length=1024,
    truncation=True,
)
