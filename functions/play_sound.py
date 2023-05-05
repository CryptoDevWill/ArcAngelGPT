import os
import pygame

def play_sound(sound_name, assets_path="assets/"):
    pygame.mixer.init()

    # Find the sound file in the given directory
    sound_path = None
    for file in os.listdir(assets_path):
        if file.endswith(".mp3") and file.startswith(sound_name):
            sound_path = os.path.join(assets_path, file)
            break

    # Play the sound if found
    if sound_path:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Sound '{sound_name}.mp3' not found in the assets directory.")