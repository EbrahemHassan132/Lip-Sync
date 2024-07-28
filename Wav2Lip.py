import os
import subprocess
import torch

# Example: Move model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set up paths and variables for the output file
output_file_path = "results/result_voice.mp4"

# Delete existing output file before processing, if any
if os.path.exists(output_file_path):
    os.remove(output_file_path)

rescaleFactor = 1
nosmooth = False
checkpoint_path = 'checkpoints/wav2lip_gan.pth'

# Define the command and its arguments
command = [
    "python", "inference.py",
    "--checkpoint_path", "checkpoints/wav2lip_gan.pth",
    "--segmentation_path", "checkpoints/face_segmentation.pth",
    "--sr_path", "checkpoints/esrgan_yunying.pth",
    "--face", "13_K.mp4",
    "--audio", "trimmed/96_K.wav",
    "--save_frames",
    "--gt_path", "data/gt",
    "--pred_path", "data/lq",
    "--no_sr",
    "--no_seg",
    "--resize_factor", str(rescaleFactor)
]

# Execute the command
try:
    subprocess.check_call(command)
except subprocess.CalledProcessError as e:
    print(f"Error during processing: Command returned exit status {e.returncode}")