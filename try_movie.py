import cv2


def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow("sample data", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = "./sample.mp4"
    play_video(video_path)
