import os
import re
import os
import glob
#Q2-1
CODE_DIR= os.path.dirname(os.path.abspath(__file__))
# DIR_IMAGE = os.path.join(CODE_DIR,"front/images/")
# list_of_files = sorted(  glob.glob(DIR_IMAGE+'*') )

#Q2-2
# for path in list_of_files :
#     print(path)
# list_of_icons = glob.glob(DIR_IMAGE+'*icon*')
# with open('icons.txt','w') as i:
#     for image in list_of_icons:
#         i.write(image+'\n')

# print(DIR_IMAGE,CODE_DIR_IMAGE)
# path ='/home/flatlife/PycharmProjects/MaktabsharifMiniProject3/front/images'
# images = os.listdir(DIR_IMAGE)


#
# # re.match(r"icon")
# with open("icons.txt", "a") as file:
#     for image in images:
#         # print(str(image))
#         if re.match(r".*icon.*", str(image)):
#             file.writelines(DIR_IMAGE+str(image)+"\n")
#Q2-4
def get_html(CODE_DIR):
    DIR_FRONT = os.path.join(CODE_DIR,"front/")
    list_of_files = sorted(glob.glob(DIR_FRONT + '*.html'))
    return list_of_files

def replacment(html_files):
    pattern = "(images.*-icon.*png)"
    pattern = re.compile(pattern)
    for file in html_files:
        with open(file, "r") as file_reader:
            files_data = file_reader.readlines()
        with open(file, "w") as file_data:
            for data in files_data:
                if re.search(pattern, data):
                    file_data.writelines(data.replace("images","../icons"))
                else:
                    file_data.writelines(data)

replacment(get_html(CODE_DIR))






