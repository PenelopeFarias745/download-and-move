import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/penel/Downloads"
to_dir = "C:/Users/penel/Desktop/Arquivos_baixados"

dir_tree = {
    "Image_files": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".jfif"],
    "Video_files": [[".mpg", ".mp2", ".mpeg", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".mov"]],
    "Document_files": [".ppt", ".xls", ".csv", ".doc", ".pdf", ".txt", ".pptx", ".xlsx", ".docx"],
    "Setup_files": [".exe", ".bin", ".cmd", ".msi", ".dmg"]
}

class FileMovementHandler(FileSystemEventHandler):
    # Código para gerenciar o evento de criação de um novo arquivo no diretório
    def on_created(self, event):
        # print(event)
        name, extension = os.path.splitext(event.src_path)

        for key, value in dir_tree.items():
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Baixado " + file_name)

                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name


                time.sleep(3)

                if os.path.exists(path2):
                    print("Diretório existe.....")
                    time.sleep(1)
                    if os.path.exists(path3):
                        print("Arquivo já existente em " + key + ".....")
                        print('Renomeando arquivo' + file_name + ".....")

                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]

                        path4 = to_dir + "/" + key + "/" + new_file_name 

                        print("Movendo " + new_file_name + ".....")

                        shutil.move(path1, path4)
                        time.sleep(1)
                    else:
                        os.makedirs(path2, exist_ok=True)
                        print("Movendo " + file_name + ".....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Criando diretório......")
                    os.makedirs(path2, exist_ok=True)
                    print("Movendo " + file_name + ".....")
                    shutil.move(path1, path3)
                    time.sleep(1)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
    print("Interrompido")
    observer.stop
