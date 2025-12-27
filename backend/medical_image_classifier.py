import torch
import clip
from PIL import Image

# Device selection
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load CLIP model
model, preprocess = clip.load("ViT-B/32", device=device)

# Medical emergency prompts
MEDICAL_CLASSES = [
    "a photo of a bleeding cut wound on skin",
    "a photo of a burn injury on skin",
    "a photo of a broken bone injury",
    "a photo of healthy skin"
]

def classify_medical_image(image: Image.Image):
    """
    Classifies medical emergency from an image using CLIP.
    Returns best matching medical class and confidence score.
    """
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = clip.tokenize(MEDICAL_CLASSES).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

        similarity = (image_features @ text_features.T).softmax(dim=-1)

    best_index = similarity.argmax().item()
    confidence = similarity[0][best_index].item()

    return MEDICAL_CLASSES[best_index], round(confidence, 3)
