""" AI Model """

from transformers import pipeline

summarizer = pipeline("summarization", model="google-t5/t5-small")
translator = pipeline("translation_XX_to_YY", model="google-t5/t5-small")
