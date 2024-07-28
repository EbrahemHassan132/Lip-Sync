import os
from pydub import AudioSegment

def detect_leading_silence(sound, silence_threshold=-40.0, chunk_size=10):
    """
    Detects the duration of leading silence in an audio segment.

    Parameters:
    sound (AudioSegment): The audio segment to analyze.
    silence_threshold (float): The threshold below which sound is considered silence (in dBFS).
    chunk_size (int): The size of each chunk to analyze (in milliseconds).

    Returns:
    int: The duration of leading silence in milliseconds.
    """
    trim_ms = 0  # ms
    assert chunk_size > 0  # to avoid infinite loop
    while trim_ms < len(sound) and sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size
    return trim_ms

def remove_silence(audio_path, output_path, silence_thresh=-40, chunk_size=10):
    """
    Removes leading and trailing silence from an audio file and exports the trimmed audio.

    Parameters:
    audio_path (str): The path to the input audio file.
    output_path (str): The path to save the trimmed audio file.
    silence_thresh (float): The threshold below which sound is considered silence (in dBFS).
    chunk_size (int): The size of each chunk to analyze (in milliseconds).

    Returns:
    None
    """
    audio = AudioSegment.from_file(audio_path, format="wav")
    start_trim = detect_leading_silence(audio, silence_threshold=silence_thresh, chunk_size=chunk_size)
    end_trim = detect_leading_silence(audio.reverse(), silence_threshold=silence_thresh, chunk_size=chunk_size)
    duration = len(audio)
    trimmed_audio = audio[start_trim:duration-end_trim]
    trimmed_audio.export(output_path, format="wav")

def preprocess_audio_files(directory):
    """
    Preprocesses all .wav audio files in a directory by removing leading and trailing silence.

    Parameters:
    directory (str): The path to the directory containing the audio files.

    Returns:
    None
    """
    # Create necessary directories
    trimmed_dir = os.path.join(directory, 'trimmed')
    os.makedirs(trimmed_dir, exist_ok=True)

    for file_name in os.listdir(directory):
        if file_name.endswith(".wav"):
            input_path = os.path.join(directory, file_name)
            output_path_trimmed = os.path.join(trimmed_dir, file_name)
            
            print(f"Processing {input_path}...")
            # Remove silence
            remove_silence(input_path, output_path_trimmed)
            print(f"Processed {output_path_trimmed}")

# Specify the directory containing the audio files
directory = "C:/Users/ebrahem/Data Science/Lip-Sync/Resources/Audio files"

# Preprocess the audio files
preprocess_audio_files(directory)
