import os

JLC_Gerber_name = {
    '.GTL':'Gerber_TopLayer',
    '.GBL':'Gerber_BottomLayer',
    '.GTO':'Gerber_TopSilkscreenLayer',
    '.GBO':'Gerber_BottomSilkscreenLayer',
    '.GTP':'Gerber_TopPasteMaskLayer',
    '.GBP':'Gerber_BottomPasteMaskLayer',
    '.GTS':'Gerber_TopSolderMaskLayer',
    '.GBS':'Gerber_BottomSolderMaskLayer',
    '.GDL':'Gerber_DocumentLayer',
    '.GKO':'Gerber_BoardOutlineLayer',
                   }

titlestr1 = '''G04 Layer: '''
titlestr2 = '''*
G04 EasyEDA Pro v1.9.29.eba1c1, 2023-07-04 04:23:24*
G04 Gerber Generator version 0.3*
G04 Scale: 100 percent, Rotated: No, Reflected: No*
G04 Dimensions in millimeters*
G04 Leading zeros omitted, absolute positions, 3 integers and 3 decimals*'''

def get_all_files_in_folder(folder_path):
    file_path_list = []
    file_prefix_list = []
    file_extension_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)

            file_prefix, file_extension = os.path.splitext(file_name)

            file_path_list.append(file_path)
            file_prefix_list.append(file_prefix)
            file_extension_list.append(file_extension)


    return file_path_list, file_prefix_list, file_extension_list




def file_rename(path, file_path_list, file_prefix_list, file_extension_list):
    suc = 0
    for i in range(len(file_path_list)):
        if file_extension_list[i].upper() in JLC_Gerber_name:
            suc += 1
            new_path = path + '\\' + JLC_Gerber_name[file_extension_list[i].upper()] + file_extension_list[i].upper()

            new_title = titlestr1 + JLC_Gerber_name[file_extension_list[i].upper()][7:] + titlestr2

            try:
                with open(file_path_list[i], "r+", encoding="utf-8") as f:
                    old = f.read()
                    f.seek(0)
                    f.write(new_title)
                    f.write('\n')
                    f.write(old)
                os.rename(file_path_list[i], new_path)
                print('\033[32m[Success]\033[0m ' + os.path.basename(file_path_list[i]) + '  ->  ' + os.path.basename(new_path))
            except OSError as e:
                print('\033[31m[Error]\033[0m ' + os.path.basename(file_path_list[i]))

    if suc == 0:
        print('\033[31m[No LiChuang Gerber file found]\033[0m')


# folder_path = input("Please enter the file path:")

folder_path = 'C:/code_test/Python/test/'
file_path_list, file_prefix_list,  file_extension_list = get_all_files_in_folder(folder_path)
file_rename(folder_path, file_path_list, file_prefix_list, file_extension_list)




