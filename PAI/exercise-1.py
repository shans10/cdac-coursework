import cv2
import os

# Set the path to the folder where you want to save the frames
output_folder = 'saved_frames'

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
video_path = 'video.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

frame_number = 0
saved_frame_count = 0

# Loop through the video
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Check if the frame is the 10th one
    if frame_number % 10 == 0:
        frame_name = os.path.join(output_folder, f'frame_{saved_frame_count}.jpg')  # Name the saved frame
        cv2.imwrite(frame_name, frame)  # Save the frame
        print(f"Saved : {saved_frame_count}")
        saved_frame_count += 1

    frame_number += 1

# Release the video capture object
cap.release()
cv2.destroyAllWindows()

print(f"Saved {saved_frame_count} frames to '{output_folder}' folder.")
