import cv2
import mediapipe as mp
import numpy as np
import json
import sys
import os

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def analyze_pose_landmarks(landmarks, image_width, image_height):
    scores = {}

    try:
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

        lx, ly = int(left_wrist.x * image_width), int(left_wrist.y * image_height)
        rx, ry = int(right_wrist.x * image_width), int(right_wrist.y * image_height)

        horizontal_diff = abs(ly - ry)
        scores["bat_straightness"] = max(0, 100 - horizontal_diff)

    except:
        scores["bat_straightness"] = 0

    return scores

def process_video(input_path, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("❌ Error: Could not open video.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_path = os.path.join(output_dir, "annotated_video.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    all_scores = []
    frame_count = 0

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
                )
                scores = analyze_pose_landmarks(
                    results.pose_landmarks.landmark, width, height
                )
                all_scores.append(scores)

                cv2.putText(frame, f"Bat Straightness: {scores['bat_straightness']:.1f}",
                            (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            writer.write(frame)

    cap.release()
    writer.release()

    if all_scores:
        avg_straightness = np.mean([s["bat_straightness"] for s in all_scores])
    else:
        avg_straightness = 0

    evaluation = {
        "total_frames": frame_count,
        "average_bat_straightness": avg_straightness,
        "comments": "Good cover drive form" if avg_straightness > 70 else "Needs improvement"
    }

    eval_path = os.path.join(output_dir, "evaluation.json")
    with open(eval_path, "w") as f:
        json.dump(evaluation, f, indent=2)

    print(f"✅ Processing complete!")
    print(f"  ▶ Annotated video: {out_path}")
    print(f"  ▶ Evaluation report: {eval_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cover_drive_analysis_realtime.py path/to/video.mp4")
        sys.exit(1)

    input_video = sys.argv[1]
    process_video(input_video)