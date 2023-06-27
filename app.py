from fastapi import FastAPI
import subprocess
import pygetwindow
import pyautogui;

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/openApp/")
async def openApplication():
  subprocess.Popen("C:\Program Files (x86)\BPJS Kesehatan\Aplikasi Sidik Jari BPJS Kesehatan\After.exe")
  return {"message": "DONE"}

@app.get("/bringFront/{name}")
async def bringFront(name):
  win=bringAppToFront(name)
  writeSomeText('tes')
  return {"message":win}

@app.get("/minApp/{name}")
async def miniApp(name):
  win=minimizeApp(name)
  return {"message":win}


def bringAppToFront(appName):
  win =pygetwindow.getWindowsWithTitle(appName)[0]
  return win.activate()

def minimizeApp(appName):
  # win =pygetwindow.getWindowsWithTitle('jjl_pygetwindow.py - python - Visual Studio Code')[0]
  win =pygetwindow.getWindowsWithTitle(appName)[0]
  return win.minimize()

def writeSomeText(text):
  pyautogui.write(text, interval=1)