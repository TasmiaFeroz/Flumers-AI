# img_classification/views.py
# Import necessary libraries and modules
import io
import os
import numpy as np
from PIL import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EfficientNetB1Model

# The views module contains functions that handle HTTP requests and responses.
# It defines the logic for processing image classification requests.

# Define the path to the ONNX model
onnx_path = os.path.join(os.path.dirname(__file__), 'efficientnet_b1.onnx')
if not os.path.exists(onnx_path):
    raise FileNotFoundError(f"Model not found at {onnx_path}")

# Initialize the EfficientNet-B1 model
model = EfficientNetB1Model(onnx_path)

# Define labels for classification
LABELS = [
    # The LABELS list contains the names of classes for image classification.
    # It is used to map the model's output to human-readable labels.
    'baby_products', 'beauty_health', 'clothing_accessories_jewellery',
    'electronics', 'grocery', 'hobby_arts_stationery',
    'home_kitchen_tools', 'pet_supplies', 'sports_outdoor'
]

# Define the API view for image classification
@api_view(['POST'])
def classify_image(request):
    # Check if an image file is provided in the request
    if 'image' not in request.FILES:
        return Response({'error': 'No image provided'}, status=400)

    try:
        # Read the image file from the request
        file = request.FILES['image']

        # Load the image
        image = Image.open(io.BytesIO(file.read()))

        # Perform model inference
        prediction, confidence = model.predict(image)

        # Return response
        return Response({
            'category': LABELS[prediction],
            'confidence': confidence
        }, status=200)

    except Exception as e:
        # Handle any errors during processing
        return Response({'error': 'Failed to process image', 'details': str(e)}, status=500)
