import subprocess
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Ensure you are in the MuseTalk directory and have edited the configs/inference/test.yaml file
# to include the correct paths for the video, audio, and the bbox_shift parameter as needed.

# Define the command and its arguments
command = [
    "python", "-m", "scripts.inference",
    "--inference_config", "configs/inference/test.yaml"
]

# Execute the command
try:
    subprocess.check_call(command)
except subprocess.CalledProcessError as e:
    print(f"Error during processing: Command returned exit status {e.returncode}")


# I used google colab for this model and I ran out of compute resources (GPU) so I continued in Kaggle
# And I will include both of the notebooks in the assignment folder