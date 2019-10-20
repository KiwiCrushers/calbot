def detect_labels(path):
    from google.cloud import vision
    import io, json

    with open("json/config.json") as h:
	config = json.load(h)

    client = vision.ImageAnnotatorClient.from_service_account_json(config["gcloud"]["tokenFile"])

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels