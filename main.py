import extensions
import os
import shutil
import pyfiglet
import sys

def files_without_extension():

    files_without_extension = []

    for file in files:

        files_without_extension.append(os.path.splitext(file)[0])

    print(f"all files inside {os.getcwd()} are:-\n{files_without_extension}\n")

def show_all_folders():

    print(f"all folders inside {os.getcwd()} are:-\n{folders}\n")
        



def file_organizer():

    files_without_extension()

    cat_names_and_file_names = {}

    while True:

        try:

            answer_to_start_organize = input("you want to continue (Yes => Y, No => N)\n").lower()

            if answer_to_start_organize in ["yes","y"]:

                break

            elif answer_to_start_organize in ["No","n"]:

                return 

        except Exception:

            print("invalid input")

        else:

            print("invalid input")


    for file in files:
  
        extension = os.path.splitext(file)[1]
        found = False

        for cat_name, cat_extensions in extensions.FILE_EXTENSIONS.items():

            if extension in cat_extensions:

                cat_names_and_file_names.setdefault(cat_name, [])
                cat_names_and_file_names[cat_name].append(file)
                found = True
                break

        if not found:
                
                cat_names_and_file_names.setdefault("other", [])
                cat_names_and_file_names["other"].append(file)

    for cat_name, file_names in cat_names_and_file_names.items():

            while True:

                original_cat_name = cat_name
                i = 1

                try:
            
                    if cat_name in os.listdir(os.getcwd()):

                        answer_to_know_if_you_want_to_put_in_the_same_folder_or_no =\
                        input(f"A folder with the name '{cat_name}' already exists\n"
                            f"Do you want to put these files: {cat_names_and_file_names[cat_name]}\nin the same folder or create another one with different name?\n"
                            "(Yes i want => 'Y', No create another one  => 'N' )\n").lower()

                    else:

                        break

                except:

                    print("invalid input")
                    continue
                
                if answer_to_know_if_you_want_to_put_in_the_same_folder_or_no in ["no","n"]:
                        
                    while cat_name in os.listdir(os.getcwd()):

                            cat_name = original_cat_name
                            cat_name = f"{cat_name} (FO, CP number {i})"
                            i += 1           

                    for file in file_names:

                        os.makedirs(os.path.join(os.getcwd(), cat_name), exist_ok=True)
                        shutil.move(file, os.path.join(os.getcwd(), cat_name))

                    break
                elif answer_to_know_if_you_want_to_put_in_the_same_folder_or_no in ["yes","y"]:

                        for file in file_names:

                            if file in os.listdir(os.path.join(os.getcwd(), cat_name)):

                                destination_folder = os.path.join(os.getcwd(), cat_name)
                                shutil.move(file, os.path.join(destination_folder, f"{file} (fo){os.path.splitext(file)[1]}"))
                                

                            else:

                                os.makedirs(os.path.join(os.getcwd(), cat_name), exist_ok=True)
                                shutil.move(file, os.path.join(os.getcwd(), cat_name))

                        break

                else:

                    print("just enter yes or no y or n")
                    continue

            if original_cat_name not in os.listdir(os.getcwd()):

                for file in file_names:

                    os.makedirs(os.path.join(os.getcwd(), cat_name), exist_ok=True)
                    shutil.move(file, os.path.join(os.getcwd(), cat_name))
    spliter()
        
def enter_folder():

    folders_inside_the_dir_you_want_to_enter = {}

    for index, folder in enumerate(folders, 1):

        folders_inside_the_dir_you_want_to_enter[index] = folder 

    print(f"all folders inside the directory{folders_inside_the_dir_you_want_to_enter}")

    while True:

        try:

            folder_number = int(input("enter the number of folder:\n"))

            if folder_number not in folders_inside_the_dir_you_want_to_enter.keys():

                raise ValueError("Invalid option selected")

            break

        except:

            print("invalid error")
    ء
    new_dir = os.path.join(os.getcwd(), folders_inside_the_dir_you_want_to_enter[folder_number])

    os.chdir(new_dir)

    print(f"the current working dir is {new_dir}")
    
    spliter()

def exit_program():

    print(
"""thank you for using my program =>> (:
The program has closed."""
)
    sys.exit()

def returnn():

    os.chdir(os.path.dirname(os.getcwd()))
    print(f"your current working dir is: {os.getcwd()}")
    spliter()

#this is the actions that are montioned in the main menu ==>
actions = {
    1:show_all_folders,
    2:files_without_extension,
    3:file_organizer,
    4:enter_folder,
    5:returnn,
    0:exit_program
}
           
def main_menu_banner():
    row=0
    while row<7:

        if row == 3:

            print(pyfiglet.figlet_format("main menu", font="banner3"))
            row += 1

        else:
          
            print("="*75 if row not in [2,4] else (" "*65).center(75, "="))
            row += 1


def spliter(): 

    while True:

        Return = False

        global folders
        global files


        list_of_dirs_and_files = os.listdir(os.getcwd())

        folders = [list_of_dirs_and_files for list_of_dirs_and_files in list_of_dirs_and_files
                    if os.path.isdir(list_of_dirs_and_files)]

        files = [list_of_dirs_and_files for list_of_dirs_and_files in list_of_dirs_and_files
                if os.path.isfile(list_of_dirs_and_files)]

        
        if not bool(files):

            print("there are no files in this directory")

            exit_return_or_chdir_dict = {
                                2 : exit_program,
                                3 : enter_folder,
                                1 : None
                                }   

            while True:

                try:

                    if bool(folders):
                                    
                        exit_or_return  = int(input("do you want to come back or enter folder inside this directory"
                                                " or exit program (1 => return, 2 => exit, 3 => enter_folder)\n"))

                        if exit_or_return not in exit_return_or_chdir_dict:

                            raise ValueError

                        if exit_or_return in [2,3]:

                            exit_return_or_chdir_dict[exit_or_return]()
                            
                        if exit_or_return == 1:

                            os.chdir(os.path.dirname(os.getcwd()))
                            print(f"current working directory if {os.getcwd()}")
                            Return = True
                            break
                    else:


                        exit_or_return  = int(input("do you want to come back"
                                                " or exit program (1 => return, 2 => exit)"))
                        
                        if exit_or_return == 2:

                            exit_return_or_chdir_dict[exit_or_return]()

                        if exit_or_return == 1:

                            current_working_dir = os.path.dirname(os.getcwd())
                            os.chdir(current_working_dir)
                            print(f"current working directory if {os.getcwd()}")
                            Return = True
                            break

                except ValueError :

                    print("\ninput must be number only and 1, 2, or 3 if you can enter a folder and 1,2 if there is no folders in that directory\n")

                except Exception:

                    print("this option doesn't exist")

        if Return == True:
            continue
        else:
            main_menu_options()

def main_menu_options():

    while True:
        
        try:
            print("""
============================================================
                                                           |
[1] Show All Folders In Current Directory                  |
                                                           |
[2] Show All Files In Current Directory                    |
                                                           |
[3] Show Files and organize them Into Organized Folder     |
                                                           |
[4] Enter One Of The Existing Folders                      |
                                                           |   
[5] return back                                            |
                                                           |
[0] Exit                                                   |
                                                           |
============================================================
    """)
            answer_main_menu = int(input("just choose only one option, select number and write it\n"))

            

            if answer_main_menu in [0,1,2,3,5,4]:

                actions[answer_main_menu]()


            else:

                raise ValueError("Invalid option selected")


        except Exception:

            continue



while True:

    try:

        current_working_dir = input("please enter the absolute path of"
                                    "the folder you want to organize it\n").strip()
        os.chdir(current_working_dir)
        break

    except Exception:
        print("invalid input")


main_menu_banner()
spliter()

