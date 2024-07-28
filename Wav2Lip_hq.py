import os
import subprocess
from IPython.display import clear_output
import torch

# Move model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set up paths and variables for the output file
output_file_path = "results/result_voice.mp4"

# Delete existing output file before processing, if any
if os.path.exists(output_file_path):
    os.remove(output_file_path)

rescaleFactor = 1
checkpoint_path = 'checkpoints/wav2lip_gan.pth'

# Construct the command
command = [
    "python", "inference.py",
    "--checkpoint_path", checkpoint_path,
    "--segmentation_path", "checkpoints/face_segmentation.pth",
    "--sr_path", "checkpoints/esrgan_yunying.pth",
    "--face", "13_K.mp4",
    "--audio", "96_E.wav",
    "--resize_factor", str(rescaleFactor),
    "--outfile", output_file_path,
    "--nosmooth"
]
# Ensure that you are in the wav2lip-hq directory
# Execute the command
try:
    subprocess.check_call(command)
except subprocess.CalledProcessError as e:
    print(f"Error during processing: Command returned exit status {e.returncode}")
else:
    # Preview output video
    if os.path.exists(output_file_path):
        clear_output()
        print("The video is created sucsessfully")
        print("See this video at", output_file_path)
    else:
        print("Processing failed. Output video not found.")