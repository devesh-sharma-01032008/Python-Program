import requests


def get_random_paragraph(no_of_paragraph=2, no_of_sentence=4):
	url = f"http://metaphorpsum.com/paragraphs/{no_of_paragraph}/{no_of_sentence}"
	return requests.get(url).text


def get_list_from_paragraph(text=get_random_paragraph()):
	sentences = text.split(".")
	result = []
	for sentence in sentences:
		words = sentence.split(" ")
		result.extend(words)
	return result
