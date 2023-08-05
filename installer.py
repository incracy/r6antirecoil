import os
import shutil
import psutil
import ctypes
import sys
import time
import uuid
import json

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin() == False:
    print("You need to run this script as administrator so it can properly install the scripts")
    input("")
    sys.exit()

username = os.getlogin()
defaultInstall = os.path.join(os.getenv('LOCALAPPDATA'), 'LGHUB', 'scripts')

processes = ["lghub.exe", "lghub_agent.exe", "lghub_system_tray.exe", "lghub_updater.exe"]
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] in processes:
        try:
            proc.terminate()
            print(f"Terminated {proc.info['name']} (PID: {proc.info['pid']})")
        except psutil.NoSuchProcess:
            print(f"No such process: {proc.info['name']}")
        except psutil.AccessDenied:
            print(f"Access denied to terminate {proc.info['name']} (PID: {proc.info['pid']})")

installPathOption = print("Finding LGHUB on your system")
time.sleep(2)
print("Found: ", defaultInstall)
time.sleep(0.5)
cleanInstallOption = input("Do you want a clean install? This will remove every script that you have (yes or no) ")
newOldOption = input("Do you want old or new scripts? (new or old) ")

print("Using default install path")
for file in os.listdir(defaultInstall):
    item_path = os.path.join(defaultInstall, file)
    if os.path.isfile(item_path):
        print("File found: ", item_path)
        if cleanInstallOption.lower() == "yes":
            print("Removing file: ", item_path)
            os.remove(item_path)
        else:
            continue
    elif os.path.isdir(item_path):
        print(f"Directory found: {item_path}")
        if cleanInstallOption.lower() == "yes":
            print("Removing directory: ", item_path)
            shutil.rmtree(item_path)
        else:
            continue

print("\n")

if newOldOption.lower() == "old":
    currentDir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    attOldDir = os.path.join(currentDir, "resources", "attack", "old")
    defOldDir = os.path.join(currentDir, "resources", "defense", "old")
    print("Installing attackers (old)")
    for filename in os.listdir(attOldDir):
        attOldFilePath = os.path.join(attOldDir, filename)
        if os.path.isfile(attOldFilePath):
            try:
                folder = os.path.join(defaultInstall, str(uuid.uuid4()))
                os.makedirs(folder, exist_ok=True)
                shutil.copy(attOldFilePath, folder)
                config_data = {
                    "name": f"{filename[:-4]}",
                    "description": "",
                    "fileName": f"./{filename}"
                }
                with open(os.path.join(folder, "config.json"), "w") as config_file:
                    json.dump(config_data, config_file, indent=4)
            except Exception as e:
                print(e)
                input("")
    print("Finished installing attackers\nInstalling defenders (old)")
    for filename in os.listdir(defOldDir):
        defOldFilePath = os.path.join(defOldDir, filename)
        if os.path.isfile(defOldFilePath):
            try:
                folder = os.path.join(defaultInstall, str(uuid.uuid4()))
                os.makedirs(folder, exist_ok=True)
                shutil.copy(defOldFilePath, folder)
                config_data = {
                    "name": f"{filename[:-4]}",
                    "description": "",
                    "fileName": f"./{filename}"
                }
                with open(os.path.join(folder, "config.json"), "w") as config_file:
                    json.dump(config_data, config_file, indent=4)
            except Exception as e:
                print(e)
                input("")

    resources_dir = os.path.join(currentDir, "resources")
    shutil.rmtree(resources_dir)

elif newOldOption.lower() == "new":
    currentDir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    attNewDir = os.path.join(currentDir, "resources", "attack", "new")
    print("Installing attackers (new)")
    for filename in os.listdir(attNewDir):
        attOldFilePath = os.path.join(attNewDir, filename)
        if os.path.isfile(attOldFilePath):
            try:
                folder = os.path.join(defaultInstall, str(uuid.uuid4()))
                os.makedirs(folder, exist_ok=True)
                shutil.copy(attOldFilePath, folder)
                config_data = {
                    "name": f"{filename[:-4]}",
                    "description": "",
                    "fileName": f"./{filename}"
                }
                with open(os.path.join(folder, "config.json"), "w") as config_file:
                    json.dump(config_data, config_file, indent=4)
            except Exception as e:
                print(e)
                input("")
    print("Finished installing attackers\nThere's no new scripts for defenders.")

    resources_dir = os.path.join(currentDir, "resources")
    shutil.rmtree(resources_dir)

print("Finished installing")
print("")
input("Press Enter to exit...")
