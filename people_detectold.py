import cv2
import numpy as np
def count_ppl():
    # Load YOLO
    net = cv2.dnn.readNet('./models/yolov3.weights', './models/yolov3.cfg')
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    classes = ["person"]  # Assuming you are only interested in detecting people

    # Start capturing video from the camera
    cap = cv2.VideoCapture(1)

    while True:
        count = 0
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        height, width, channels = frame.shape

        # Convert the frame to a blob and pass through the network
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Information to put on the frame
        class_ids = []
        confidences = []
        boxes = []

        # Analyze the outs array
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Drawing bounding boxes and labels on the image
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                try:
                    label = str(classes[class_ids[i]])
                except:
                    pass
                if label == "person":
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    count += 1
        print(count)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    count_ppl()
