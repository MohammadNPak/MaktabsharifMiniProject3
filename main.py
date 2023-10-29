from pathlib import Path

file_path=Path("/home/tears/Desktop/Maktabshrif/miniproject/MaktabsharifMiniProject3/front/images")
for images in file_path.iterdir():
    print(images)

