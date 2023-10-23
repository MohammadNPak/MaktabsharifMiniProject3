import os
import re

CODE_DIR= os.path.dirname(os.path.abspath(__file__))
DIR_IMAGE = os.path.join(CODE_DIR,"front/images/")
# print(DIR_IMAGE,CODE_DIR_IMAGE)
# path ='/home/flatlife/PycharmProjects/MaktabsharifMiniProject3/front/images'
images = os.listdir(DIR_IMAGE)

# re.match(r"icon")
with open("icons.txt", "a") as file:
    for image in images:
        # print(str(image))
        if re.match(r".*icon.*", str(image)):
            file.writelines(DIR_IMAGE+str(image)+"\n")
