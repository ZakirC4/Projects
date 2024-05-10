import os

full_path = "C:\\Users\\drzak\\OneDrive\\Documents\\Code\\audio_player"

src_file = "main.cpp"
print("building ...")
os.system(f"g++ {full_path}\\src\\{src_file} -o {full_path}\\bin\\AudioPlayer.exe -I{full_path}\\include -L{full_path}\\lib -lfltk -lsfml-audio")
print("\nfinished ...")