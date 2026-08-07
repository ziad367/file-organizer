import extensions
import os
import shutil
import pyfiglet


def show_all_folders():

    print(folders)
    main_menu_options()


def show_all_files():

    files_without_extension = []
    for file in files:

        files_without_extension.append(file.split(".")[0])

    print(files_without_extension)
    main_menu_options()



def organize_files(current_working_dir):

    for file in files:
  
        extension = os.path.splitext(file)[1]
        found = False

        for cat_name, cat_extension in extensions.FILE_EXTENSIONS.items():

            if extension in cat_extension:

                organizer(current_working_dir,cat_name,file)
                found = True
                break

        if not found:
                organizer(current_working_dir,"other", file)

    main_menu_options()

def enter_folder(current_working_dir):

    c = {}
    for index, folder in enumerate(folders, 1):

        c[index] = folder 

    print(f"all folders inside the directory{c}")
    folder_number = int(input("enter the number of folder:\n"))
    os.chdir(os.path.join(current_working_dir, c[folder_number]))
    print(f"the current working dir is {os.path.join(
        current_working_dir, c[folder_number])}")
    spliter(os.path.join(current_working_dir, c[folder_number]))

def exit_program():

    print(
"""thank you for using my program =>> (:
The program has closed."""
)
    return 0

#this is the actions that are montioned in the main menu ==>
actions = {
    1:show_all_folders,
    2:show_all_files,
    3:organize_files,
    4:enter_folder,
    0:exit_program
}
def organizer(current_working_dir, category, file_name):
        
        os.makedirs(os.path.join(current_working_dir,category), 
                    exist_ok=True)
        shutil.move(file_name, os.path.join(current_working_dir,category))
   
        
def main_menu_banner():
    row=0
    while row<7:

        if row == 3:

            print(pyfiglet.figlet_format("main menu", font="banner3"))
            row += 1

        else:
          
            print("="*75 if row not in [2,4] else (" "*65).center(75, "="))
            row += 1


def spliter(current_working_dir):

    global folders
    global files


    list_of_dirs_and_files = os.listdir(current_working_dir)

    folders = [list_of_dirs_and_files for list_of_dirs_and_files in list_of_dirs_and_files
                if os.path.isdir(list_of_dirs_and_files)]

    files = [list_of_dirs_and_files for list_of_dirs_and_files in list_of_dirs_and_files
            if os.path.isfile(list_of_dirs_and_files)]
    main_menu_options(current_working_dir)

def main_menu_options(current_working_dir):




    try:
        print("""
====================================================
                                                |
[1] Show All Folders In Current Directory          |
                                                |
[2] Show All Files In Current Directory            |
                                                |
[3] Organize Files Into Organized Folder           |
                                                |
[4] Enter One Of The Existing Folders              |
                                                |
[0] Exit                                           |
                                                |
====================================================
""")
        answer_main_menu = int(input("just choose only one option, select numper and write it\n"))

        

        if answer_main_menu in [1,2,0]:

            actions[answer_main_menu]()
            

        elif answer_main_menu in [3,4]:

            actions[answer_main_menu](current_working_dir)
            


        else:

            print(1/0)


    except:

        main_menu_options(current_working_dir)

    


while True:

    try:

        current_working_dir = input("please enter the absalute path of"
                                    "the folder you want to organize it\n").strip()
        os.chdir(current_working_dir)
        break

    except:
        print("invalid input")


main_menu_banner()
spliter(os.getcwd())








