import tkinter as tk
from Engine.internals.saveLoad import save as saveFile
from Engine.internals.saveLoad import load as loadFile
from Engine.internals.saveLoad import loadObject
import sys
import importlib
from pathlib import Path

def load_all_objects():
    rootDir = Path(currentSavePath)
    for file in rootDir.rglob("*.py"):
        if "__pycache__" in file.parts:
            continue
        module_name = file.relative_to(rootDir).with_suffix("")
        module_name = ".".join(module_name.parts)
        spec = importlib.util.spec_from_file_location(module_name, file)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

def updateWindow():
    global currentSavePath
    currentSavePath = pathVar.get()
    root.update_idletasks()
    root.update()

def switchToLocalUpdate(withSaveObject=None):
    global localupdate
    localupdate = True
    currentRootContainer = None
    while localupdate:
        updateWindow()

    #start updating from rootContainer and start rootcontainer
    currentRootContainer = loadObject(withSaveObject or currentSaveObject)
    currentRootContainer.rootUiUpdate = updateWindow
    currentRootContainer.StartMainLoop()

def start():
    load_all_objects()
    global localupdate
    #reload all parts of the game source code
    localupdate = False

def stop(withSaveObject=None):
    currentRootContainer.StopMainLoop()
    currentRootContainer = None
    switchToLocalUpdate(withSaveObject)

def reload(withSaveObject=None):
    stop(withSaveObject)
    start()

def load():
    global currentSaveObject
    if not currentSavePath == "":
        currentSaveObject = loadFile(currentSavePath)

def save():
    currentSaveObject = currentRootContainer.generateSaveObject()
    if not currentSavePath == "":
        saveFile(currentSaveObject, currentSavePath)

# Create window
root = tk.Tk()
root.title("Game Engine")
root.geometry("300x200")

pathVar = tk.StringVar()

currentSaveObject = None
currentSavePath = pathVar.get()

currentRootContainer = None

#start button
tk.Button(root, text="Start", command=start).pack(fill="x")
#stop button
tk.Button(root, text="Stop", command=stop).pack(fill="x")
#reload button
tk.Button(root, text="Reload", command=reload).pack(fill="x")
#load button
tk.Button(root, text="Load", command=load).pack(fill="x")
#save button
tk.Button(root, text="Save", command=save).pack(fill="x")
#path entry
tk.Entry(root, textvariable=pathVar).pack(fill="x")

localupdate = True
switchToLocalUpdate()