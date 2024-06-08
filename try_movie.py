import cv2

data = cv2.VideoCapture("./sample.mp4")
type(data)
data.isOpened()


def detect_cat_faces(frame, cat_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cats = cat_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in cats:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame


def play_video_with_cat_detection(video_path, cascade_path):
    cat_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    while True:
        ret, frame = cap.read()

        if ret:
            frame_with_cat_faces = detect_cat_faces(frame, cat_cascade)
            cv2.imshow("Cat Face Detection", frame_with_cat_faces)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = "./sample.mp4"
    cascade_path = "./cascade.xml"
    play_video_with_cat_detection(video_path, cascade_path)
