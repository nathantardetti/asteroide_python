# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="assets/icon.ico") ]
cx_Freeze.setup(
    name = "Start Wars Python",
    options={
        "build_exe":{
            "packages":["pygame", "speech_recognition", "pyttsx3"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi
