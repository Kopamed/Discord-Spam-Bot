import pyinputplus as pyip
import os

def edit_menu():
    pass

def new_cfg():
    cfg_filename = input("Enter the name of your new config file. I will automatically add .json to it.\n>") + ".json"
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    uhh = os.listdir(path=CURR_DIR+"/configs")
    for fi in uhh:
        if fi == cfg_filename:
            time_to_shit_myself = 63715/0
            




if __name__ == "__main__":
    new_cfg()
