import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ang = np.degrees(
        np.arctan2(c[1]-b[1], c[0]-b[0]) -
        np.arctan2(a[1]-b[1], a[0]-b[0])
    )
    ang = abs(ang)
    return 360-ang if ang > 180 else ang

MODEL_PATH = "pose_landmarker_heavy.task"

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_poses=1,
    min_pose_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
counter, stage = 0, None
timestamp_ms = 0

# --- Smoothing buffer ---
angle_buffer = []
BUFFER_SIZE = 5  # average over last 5 frames

def smoothed_angle(buffer, new_val):
    buffer.append(new_val)
    if len(buffer) > BUFFER_SIZE:
        buffer.pop(0)
    return sum(buffer) / len(buffer)

with vision.PoseLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

        timestamp_ms += 33
        result = landmarker.detect_for_video(mp_image, timestamp_ms)

        if result.pose_landmarks:
            lm = result.pose_landmarks[0]

            # Use visibility to check if landmarks are reliably detected
            if lm[11].visibility > 0.5 and lm[13].visibility > 0.5 and lm[15].visibility > 0.5:
                s = [lm[11].x, lm[11].y]
                e = [lm[13].x, lm[13].y]
                w = [lm[15].x, lm[15].y]

                raw_ang = angle(s, e, w)
                ang = smoothed_angle(angle_buffer, raw_ang)

                # Wider deadband to avoid jitter triggering
                if ang > 150:
                    stage = "down"
                if ang < 50 and stage == "down":
                    stage = "up"
                    counter += 1

        # Reps counter — bright yellow, hard to miss
        cv2.putText(frame, f"Reps: {counter}", (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)

        # Stage — white, secondary info
        cv2.putText(frame, f"Stage: {stage}", (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Counter", frame)

        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()