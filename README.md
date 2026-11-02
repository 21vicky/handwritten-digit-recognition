# ✍️ Handwritten Digit Recognition using Deep Learning

An AI-powered handwritten digit recognition application built using **Python, TensorFlow, Keras, MNIST and Gradio**.

The application uses a trained Artificial Neural Network (ANN) to recognize handwritten digits from 0 to 9. Users can draw a digit on an interactive canvas and receive an AI prediction with a confidence score.

## 🚀 Project Demo

Draw a digit (0–9) using the interactive canvas and click **Predict Digit** to see the model's prediction.

## 🎯 Project Objectives

* Understand the fundamentals of Neural Networks.
* Learn image preprocessing and normalization.
* Train a deep learning model using the MNIST dataset.
* Evaluate model performance.
* Build an interactive AI application using Gradio.
* Save and reuse a trained machine learning model.

## 🧠 Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Programming language           |
| TensorFlow   | Deep learning framework        |
| Keras        | Neural network development     |
| NumPy        | Numerical computations         |
| Matplotlib   | Data visualization             |
| MNIST        | Handwritten digit dataset      |
| Gradio       | Interactive web application    |
| Google Colab | Model development and training |

## 📚 Dataset

This project uses the **MNIST Handwritten Digit Dataset**.

* 60,000 training images
* 10,000 testing images
* Image dimensions: 28 × 28 pixels
* Grayscale images
* 10 digit classes (0–9)

## 🏗️ Neural Network Architecture

The project uses a Sequential Neural Network with the following layers:

1. Input Layer – 28 × 28 pixels
2. Flatten Layer – Converts the image into 784 features.
3. Hidden Layer – 128 neurons with ReLU activation.
4. Output Layer – 10 neurons with Softmax activation.

### Model Configuration

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Evaluation Metric: Accuracy
* Training Epochs: 5
* Batch Size: 32

## ⚙️ How It Works

1. User draws a handwritten digit.
2. Gradio receives the drawing.
3. The image is converted into grayscale.
4. The image is resized to 28 × 28 pixels.
5. Pixel values are normalized.
6. The trained neural network processes the image.
7. The model predicts the digit.
8. The application displays the prediction and confidence score.

## 📂 Project Structure

```text
handwritten-digit-recognition/
│
├── Handwritten_Digit_Recognition.ipynb
├── handwritten_digit_model.keras
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
└── screenshots/
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/21vicky/handwritten-digit-recognition.git
```

### 2. Navigate to the project folder

```bash
cd handwritten-digit-recognition
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local Gradio URL displayed in your terminal.

## 📊 Model Evaluation

The model was evaluated using the MNIST test dataset.

The notebook includes:

* Training and validation accuracy
* Test accuracy
* Individual digit predictions
* Prediction confidence scores
* Visualization of correctly and incorrectly classified digits

## 🔮 Future Improvements

* Improve image preprocessing and digit centering.
* Improve recognition of different handwriting styles.
* Add prediction probability visualization for all 10 digits.
* Deploy the application using Hugging Face Spaces.
* Explore more advanced neural network architectures.

## 👨‍💻 Author

**Vignesh U**

GitHub: [@21vicky](https://github.com/21vicky)

## ⭐ Acknowledgements

* MNIST Handwritten Digit Dataset
* TensorFlow and Keras
* Gradio
* Google Colab

---


Handwritten Digit Recognition ✅
