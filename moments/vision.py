import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from pathlib import Path
from flask import current_app

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

# Create an Image Analysis client for synchronous operations,
# using API key authentication
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)


def analyze_image(image_path) -> list:
    with open(image_path, "rb") as f:
        # Analyze the image
        image_data = f.read()
    result = client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.OBJECTS],
        gender_neutral_caption=True,
    )
    objects_list = []
    if result.objects is not None:
        for object in result.objects.list:
            objects_list.append(object.tags[0].name)
            print(f"   '{object.tags[0].name}', {object.bounding_box}, Confidence: {object.tags[0].confidence:.4f}")
    return objects_list
