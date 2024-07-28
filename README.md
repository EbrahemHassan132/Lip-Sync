# Lip-Syncing Audio to Video

## Introduction
This project aims to develop a pipeline that accurately lip-syncs provided audio to a given video, achieving a quality similar to the referenced video 13_K.mp4. The project uses three models: Wav2Lip, Wav2Lip_HQ, and MuseTalk, and includes audio preprocessing to remove leading and trailing silence.

## Audio Preprocessing
To preprocess the audio files and remove leading and trailing silence, use the provided script (Audio_preprocessing.py).

## Installation and Usage

### Wav2Lip
#### Installation
1. Follow the instructions for installation and model download in the original [Wav2Lip Repository](https://github.com/Rudrabha/Wav2Lip.git).
2. Clone the repository:
    ```bash
    git clone https://github.com/Rudrabha/Wav2Lip.git
    cd Wav2Lip
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the Model
1. Ensure you have downloaded the pretrained models and placed them in the `checkpoints` directory as per the instructions in the original repository.
2. Run the inference script:
    ```bash
    python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --segmentation_path checkpoints/face_segmentation.pth --sr_path checkpoints/esrgan_yunying.pth --face 13_K.mp4 --audio trimmed/96_K.wav --outfile results/result_voice.mp4 --nosmooth
    ```

### Wav2Lip_HQ
#### Installation
1. Follow the instructions for installation and model download in the original [Wav2Lip_HQ Repository](https://github.com/Markfryazino/wav2lip-hq.git).
2. Clone the repository:
    ```bash
    git clone https://github.com/Markfryazino/wav2lip-hq.git
    cd wav2lip-hq
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the Model
1. Ensure you have downloaded the pretrained models and placed them in the `checkpoints` directory as per the instructions in the original repository.
2. Run the inference script:
    ```bash
    python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --segmentation_path checkpoints/face_segmentation.pth --sr_path checkpoints/esrgan_yunying.pth --face 13_K.mp4 --audio trimmed/96_K.wav --save_frames --gt_path data/gt --pred_path data/lq --no_sr --no_seg --resize_factor 1
    ```

### MuseTalk
#### Installation
1. Follow the instructions for installation and model download in the original [MuseTalk Repository](https://github.com/TMElyralab/MuseTalk.git).
2. Clone the repository:
    ```bash
    git clone https://github.com/TMElyralab/MuseTalk.git
    cd MuseTalk
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the Model
1. Ensure you have downloaded the pretrained models and placed them in the `checkpoints` directory as per the instructions in the original repository.
2. Run the inference script:
    ```bash
    python -m scripts.inference --inference_config configs/inference/test.yaml
    ```

## Evaluation and Fine-Tuning
The evaluation criteria for the models include Lip Sync Accuracy, Code Quality, and Final Video Quality. Based on these criteria, MuseTalk produced the best results, followed by Wav2Lip_HQ and Wav2Lip.

For detailed results and fine-tuning parameters, refer to the report.

## References
- [Wav2Lip Repository](https://github.com/Rudrabha/Wav2Lip.git)
- [Wav2Lip_HQ Repository](https://github.com/Markfryazino/wav2lip-hq.git)
- [MuseTalk Repository](https://github.com/TMElyralab/MuseTalk.git)

For detailed installation and usage instructions, refer to the respective sections above.
