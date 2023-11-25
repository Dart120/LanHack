import cv2
import numpy as np
from sort.tracker import SortTracker
import math
import multiprocessing
import time

def count_ppl(duration,queue):
    # Load YOLO
    net = cv2.dnn.readNet('./models/yolov3.weights', './models/yolov3.cfg')
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    classes = ["person"]  # Assuming you are only interested in detecting people

    # Initialize SORT tracker
    tracker = SortTracker()

    # Start capturing video from the camera
    cap = cv2.VideoCapture(1)
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    diag = math.sqrt((width) ** 2 + (height) ** 2)
    hashmap = {}
    start_time = time.time()
    while True:
        # Capture frame-by-frame
        speed = 0
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape

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

        # Convert YOLO detections to SORT format (x, y, w, h)
        detections = []
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                detections.append([x, y, x + w, y + h,1,1])

        # Update SORT tracker with current frame detections
        try:
            track_bbs_ids = tracker.update(np.array(detections),"")
        except:
            pass
       
      

        # Drawing tracked objects on the image
        items = 0
        for track in track_bbs_ids:
            # print(track)
            # exit(0)
            x, y, w, h, track_id,_,_ = track
            if track_id in hashmap.keys():
                items += 1
                old_x, old_y = hashmap[track_id]
                dist = math.sqrt((old_x - x) ** 2 + (old_y - y) ** 2)
                norm_dist = dist / diag
                speed += dist
            
            hashmap[track_id] = (x,y)

            cv2.rectangle(frame, (int(x), int(y)), (int(w), int(h)), (255, 0, 0), 2)
            cv2.putText(frame, f"ID {track_id}", (int(x), int(y - 10)), 0, 0.5, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        if items:
            print(speed/items)
        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > duration:
            
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
   
    queue.put((items,speed))

if __name__ == "__main__":

    queue = multiprocessing.Queue()
    duration = 5

    process = multiprocessing.Process(target=count_ppl, args=(duration, queue))
    process.start()

    # Non-blocking wait
    while process.is_alive():
        # Here, you can execute other tasks in a non-blocking manner
        print("Waiting for process to complete...")
        time.sleep(1)  # Sleep for a short duration to prevent busy waiting

    # Process has finished, now retrieve the data
    count,speed = queue.get() if not queue.empty() else None

    # count_ppl()
