import FreeSimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress", key="textfiles")
input1 = sg.Input()
choose_file = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select location folder")
input2 = sg.Input()
choose_folder = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_file],[label2, input2, choose_folder], [compress_button, label]])

while True:
    event, values = window.read()

    match event:
        case "Compress":
            print(event, '-', values)
            files = values['files'].split(";")
            folder = values['folder']
            print(files, folder)
            zip_creator.make_archive(files, folder)
            window["output"].update(value="Compressed Successfully")
        case sg.WIN_CLOSED:
            break



window.close()