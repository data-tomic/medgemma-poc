# Make sure you have installed the accelerate library:
# pip install accelerate

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText

# --- 1. LOAD MODEL AND PROCESSOR ---
model_id = "google/medgemma-4b-it"

print("Loading model and processor...")
# Use the correct model class and device_map
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)
print("Model and processor loaded successfully.")


# --- 2. LOAD LOCAL IMAGE ---
try:
    image = Image.open("xray.jpg")
    if image.mode != "RGB":
        image = image.convert("RGB")
except FileNotFoundError:
    print("Error: File 'xray.jpg' not found. Make sure it is in the same directory as app.py.")
    exit()


# --- 3. CREATE THE CORRECT DATA STRUCTURE (from the example) ---
# The image is passed as an object within the content list
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What are the findings in this chest x-ray?"},
            {"type": "image", "image": image}
        ]
    }
]

# --- 4. PROCESS DATA AND GENERATE RESPONSE (from the example) ---
print("Preparing data for the model...")
# Use apply_chat_template with the correct parameters
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt"
).to(model.device)

input_len = inputs["input_ids"].shape[-1]

print("Generating response...")
# Generate the response
with torch.inference_mode():
    generation = model.generate(**inputs, max_new_tokens=512, do_sample=False)
    generation = generation[0][input_len:]

# Decode and print the result
decoded = processor.decode(generation, skip_special_tokens=True)

print("\n--- Model Response ---")
print(decoded)
print("----------------------\n")