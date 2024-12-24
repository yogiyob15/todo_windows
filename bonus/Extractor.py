import FreeSimpleGUI as sg
import zip_extract

sg.theme("Black")

label1 = sg.Text("Select files to extract", key="textfiles")
input1 = sg.Input()
choose_file = sg.FileBrowse("Choose", key="file")

label2 = sg.Text("Select location folder")
input2 = sg.Input()
choose_folder = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract", key="extract", )
output_label = sg.Text("", key="output", text_color="green")

exit = sg.Button("Exit", key="exit")

window = sg.Window("Extract Window",
                   layout=[[label1, input1, choose_file],
                           [label2, input2, choose_folder],
                           [extract_button, output_label, exit]])

while True:
    event, value = window.read()
    archivepath = value["file"]
    destination = value["folder"]

    match event:
        case "extract":
            zip_extract.extract_archive(archivepath, destination)
            window["output"].update(value="Extracted Successfully")
        case "exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()



