import extensions
import os
import shutil
import pyfiglet
import sys

def files_without_extension():

    files_without_extension = []

    for file in files:

        files_without_extension.append(file.split(".")[0])

    print(f"all files inside {os.getcwd()} are:-\n{files_without_extension}")

def show_all_folders():

    print(f"all folders inside {os.getcwd()} are:-\n{folders}")
    main_menu_options()


def show_all_files():

    files_without_extension()
    main_menu_options()



def organize_files(current_working_dir):

    files_without_extension()

    while True:

        try:

            answer_to_start_organize = input("you want to continue (Yes => Y, No => N)\n").lower()

            if answer_to_start_organize in ["yes","y"]:

                break

            else:

                main_menu_options(os.getcwd())

        except Exception:

            print("invalid input")

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

    folders_inside_the_dir_you_want_to_enter = {}
    for index, folder in enumerate(folders, 1):

        folders_inside_the_dir_you_want_to_enter[index] = folder 

    print(f"all folders inside the directory{folders_inside_the_dir_you_want_to_enter}")

    folder_number = int(input("enter the number of folder:\n"))

    new_dir = os.path.join(current_working_dir, folders_inside_the_dir_you_want_to_enter[folder_number])

    os.chdir(new_dir)

    print(f"the current working dir is {new_dir}")
    
    spliter(new_dir)

def exit_program():

    print(
"""thank you for using my program =>> (:
The program has closed."""
)
    sys.exit()

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

    
    if not bool(files):

        print("there are no files in this directory")

        while True:
            try:

                if bool(folders):

                    exit_return_or_chdir_dict = {
                                        2 : exit_program,
                                        3 : lambda: enter_folder(current_working_dir),
                                        1 : None
                                        }   
                                 
                    exit_or_return  = int(input("do you want to come back or enter folder inside this directory"
                                            " or exit program (1 => return, 2 => exit, 3 => enter_folder)\n"))

                    if exit_or_return not in exit_return_or_chdir_dict:

                        print(1/0)

                    if exit_or_return in [2,3]:

                        exit_return_or_chdir_dict[exit_or_return]()
                        
                    if exit_or_return == 1:

                        os.chdir(os.path.dirname(current_working_dir))
                        print(f"current working directory if {os.getcwd()}")
                        spliter(os.getcwd())

                else:

                    exit_or_return  = int(input("do you want to come back"
                                            " or exit program (1 => return, 2 => exit)"))
                    
                    if exit_or_return == 2:

                        exit_return_or_chdir_dict[exit_or_return]()

                    if exit_or_return == 1:

                        os.chdir(os.path.dirname(current_working_dir))
                        print(f"current working directory if {os.getcwd()}")
                        spliter(os.getcwd())

            except ValueError :

                print("input must be number only")

            except Exception:

                print("this option doesn't exit")
    
    main_menu_options(os.getcwd())

def main_menu_options(current_working_dir):


    try:
        print("""
========================================================
                                                       |
[1] Show All Folders In Current Directory              |
                                                       |
[2] Show All Files In Current Directory                |
                                                       |
[3] Show Files and organize them Into Organized Folder |
                                                       |
[4] Enter One Of The Existing Folders                  |
                                                       |
[0] Exit                                               |
                                                       |
========================================================
""")
        answer_main_menu = int(input("just choose only one option, select numper and write it\n"))

        

        if answer_main_menu in [1,2,0]:

            actions[answer_main_menu]()
            

        elif answer_main_menu in [3,4]:

            actions[answer_main_menu](current_working_dir)
            


        else:

            print(1/0)


    except Exception:

        main_menu_options(os.getcwd())

    


while True:

    try:

        current_working_dir = input("please enter the absalute path of"
                                    "the folder you want to organize it\n").strip()
        os.chdir(current_working_dir)
        break

    except Exception:
        print("invalid input")


main_menu_banner()
spliter(os.getcwd())








