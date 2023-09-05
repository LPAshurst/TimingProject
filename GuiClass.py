# img_viewer.py

import PySimpleGUI as sg
import os.path
import psutil

# First the window layout in 2 columns
values = []
for i in psutil.process_iter():
    values.append(i.name())
values.sort()
valuesSet = set(values)
sorted(valuesSet, key=str.lower)
file_list_column = [
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
    [sg.Text("Choose an Exceucutable from the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
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
    event, valuesSet = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()