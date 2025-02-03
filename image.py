from transformers import CLIPProcessor, CLIPModel
import torch
from PIL import Image
import numpy as np
import sys
import os

#img = np.loadtxt('./db/image_vector.txt')

image_dir = 'data'


image_list = []


for filename in os.listdir(image_dir):
    if filename.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
        image_path = os.path.join(image_dir, filename)
        img = Image.open(image_path)
        image_list.append(img)

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


print(f'Total data {len(image_list)}')

inputs = processor(images=image_list, return_tensors="pt")


image_features = model.get_image_features(**inputs)


for i, feature in enumerate(image_features):
    # Flatten the feature vector
    image_vector = feature.detach().numpy().flatten()

    image_filename = os.listdir(image_dir)[i]
    embedding_filename = f"db/{image_filename}_embedding.txt"

    np.savetxt(embedding_filename, image_vector)
    print(f"Saved embedding for {image_filename} to {embedding_filename}")

