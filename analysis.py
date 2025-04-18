import cv2
import numpy as np
from skimage.restoration import estimate_sigma

def analyze_frame(video_path):
    # Open video and read the first frame
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return {"Error": "Unable to read video file"}

    # Exposure check (brightness)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    exposure = "Good"
    if brightness < 50:
        exposure = "Underexposed"
    elif brightness > 200:
        exposure = "Overexposed"

    # Sharpness check
    sharpness_value = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness = "Sharp" if sharpness_value > 100 else "Blurry"

    # Noise check
    noise_sigma = estimate_sigma(gray, channel_axis=None)
    noise = "Noisy" if noise_sigma > 10 else "Clean"

    return {
        "Exposure": exposure,
        "Sharpness": sharpness,
        "Noise": noise
    }

# Quick test:
if __name__ == "__main__":
    print(analyze_frame("samples/small_test.mp4"))
