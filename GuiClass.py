# img_viewer.py

import PySimpleGUI as sg
import os.path
import psutil

# First the window layout in 2 columns

exe = ""
values = []
for i in psutil.process_iter():
    values.append(i.name())
values.sort()
valuesSet = set(values)
valuesSet = sorted(valuesSet, key=str.lower)
exe_list_column = [
    [
         sg.Text("What excecutable would you like to track?"),
        
    ],
    [
       sg.Listbox(
            valuesSet, enable_events=True, size=(40, 20), key="-String-"
        )
    ],
]

    # For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an Exceucutable from the left:")]

    
]

# ----- Full layout -----
layout = [
    [
        sg.Column(exe_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

layout2 = [
   [[sg.T("Ttab 2")]]
]

tabbedLayout = [[sg.TabGroup([[sg.Tab('Pick an executable to track', layout, tooltip='tip'), sg.Tab('Track progress', layout2)]], tooltip='TIP2')],    
         [sg.Button('Read')]]    


window = sg.Window("Image Viewer", tabbedLayout)


# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
        
    exeList = values["-String-"]
    exe = exeList[0]
        
   
    window.close() 
    