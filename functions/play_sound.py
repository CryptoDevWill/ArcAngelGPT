import os
import sys
import pygame


def play_sound(sound_name, assets_path="assets/"):
    pygame.mixer.init()

    # Get the script's directory and join it with the assets_path
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    assets_dir = os.path.join(script_dir, assets_path)

    # Find the sound file in the given directory
    sound_path = None
    for file in os.listdir(assets_dir):
        if file.endswith(".mp3") and file.startswith(sound_name):
            sound_path = os.path.join(assets_dir, file)
            break

    # Play the sound if found
    if sound_path:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Sound '{sound_name}.mp3' not found in the assets directory.")
