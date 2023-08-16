import cv2
import tensorflow as tf
import numpy as np

# Load the pre-trained model
model = tf.keras.applications.ResNet50(weights='imagenet')

# Load the class labels
with open('imagenet_labels.txt') as f:
    labels = f.readlines()
labels = [label.strip() for label in labels]

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Preprocess the frame for the model
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # Make predictions
    predictions = model.predict(image)
    top_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=5)[0]

    # Display the predictions
    for i, (_, label, prob) in enumerate(top_predictions):
        cv2.putText(frame, f'{label}: {prob*100:.2f}%', (10, 30+i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Object Recognition', frame)

    # Check for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
