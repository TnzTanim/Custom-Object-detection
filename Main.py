import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

# Load the pre-trained model from the file
model = load_model('Your Model Path')

# Initialize the webcam
cap = cv2.VideoCapture(0)
class_labels=['Class 1','Class 2]

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Pre-process the frame for classification
    img = cv2.resize(frame, (224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    
    # Use the model to classify the frame
    prediction = model.predict(img_tensor)
    
    # Get the class label for the frame
    class_index = np.argmax(prediction[0])
    
    
    # Get the class label for the frame
    class_label =class_labels[class_index]
    print(class_label)
    
    # Display the frame with the class label
    cv2.putText(frame, class_label, (10, 30), cv2.FONT_HERSHEY_COMPLEX,
                1.0, (255, 255, 255), 3)
    cv2.imshow('Webcam', frame)
    
    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
