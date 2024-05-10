""" AI Model """

from transformers import pipeline


summarizer = pipeline(task="summarization", model="google-t5/t5-small")
translator = pipeline(task="translation_XX_to_YY", model="google-t5/t5-small")
question_answerer = pipeline(task="question-answering", model="google-t5/t5-small")
