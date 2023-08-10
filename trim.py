import os
import sox

input_folder = "C:/Users/LENOVO_User/Documents/datasets/daniel dona/wav_orig"
output_folder = "C:/Users/LENOVO_User/Documents/datasets/daniel dona/wav"

# Creates a sox object to call sox commands
tfm = sox.Transformer()

for file_name in os.listdir(input_folder):
    if file_name.endswith(".wav") or file_name.endswith(".mp3"):
        audio_path = os.path.join(input_folder, file_name)
        
        # Detect and remove silence from the beginning of audio
        tfm.silence(1, 0.1, 0.3, False, )
        tfm.build(audio_path, os.path.join(output_folder, file_name))
