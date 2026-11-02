```python
import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load trained model
model = tf.keras.models.load_model("handwritten_digit_model.keras")

def predict_digit(image):
    if image is None:
        return "Please draw a digit."

    # Convert image to grayscale
    image = image.convert("L")

    # Resize to MNIST dimensions
    image = image.resize((28, 28))

    # Invert colors if necessary
    image = ImageOps.invert(image)

    # Normalize image
    image_array = np.array(image).astype("float32") / 255.0

    # Reshape for model prediction
    image_array = image_array.reshape(1, 784)

    # Predict
    predictions = model.predict(image_array)
    probabilities = predictions[0]

    digit = int(np.argmax(probabilities))
    confidence = float(np.max(probabilities))

    return {
        str(i): float(probabilities[i])
        for i in range(10)
    }

# Gradio interface
demo = gr.Interface(
    fn=predict_digit,
    inputs=gr.Sketchpad(
        image_mode="L",
        canvas_size=(280, 280),
        type="pil"
    ),
    outputs=gr.Label(num_top_classes=10),
    title="Handwritten Digit Recognition",
    description="Draw a digit from 0 to 9 and let AI recognize it."
)

demo.launch()
```
