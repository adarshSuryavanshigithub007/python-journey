from pathlib import Path

file = open("/home/adarshsuryavanshi/Documents/Python/chapter_09_file/exercises/poem.txt", "r")
data = file.read()
if("Twinkle" in data):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")

file.close()
