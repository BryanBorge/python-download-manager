import shutil, os
import zipfile
from time import sleep
from send2trash import send2trash

def movefile(source, dest):
    try:
        shutil.move(source,dest)
        print(f'Moved {file} to {dest}')
    except shutil.Error:
        print(f'{file} already moved')


desktop_path = 'C:\\Users\\Bryan\\OneDrive\\Desktop'
download_path = 'D:\\Downloads'
programming_path = 'D:\\Programming'
pdf_path = 'C:\\Users\\Bryan\\OneDrive\\Documents\\All PDFs'
pictures_path = 'D:\\Pictures'
picture_extentions = ('.jpeg', '.jpg', '.png','.gif')

video_path = 'D:\\Videos'
video_extentions = ('.mp4','.wmv', '.mov', '.flv')

zip_path = 'D:\\Downloads\\ZIP Files'
extracted_zip_path = 'D:\\Downloads\\ZIP Files\\Extracted ZIP Files'

while True:
    numberOfFiles = len(os.listdir(download_path))
    sleep(5)
    if numberOfFiles > 2:
        for root, folderName, fileNames in os.walk(download_path):
            print(f'The current folder is {folderName}')
            for file in fileNames:
                print(file)

                #Pictures
                if file.lower().endswith(picture_extentions):
                    movefile(f'{download_path}\{file}', pictures_path)
                    try:
                        shutil.move(f'{download_path}\{file}', pictures_path)
                        print(f'Moves {file} to {pictures_path}')
                    except shutil.Error:
                        print(f'{file} already moved')
                #Videos
                if file.lower().endswith(video_extentions):
                    try:
                        shutil.move(f'{download_path}\{file}', video_path)
                        print(f'Moves {file} to {video_path}')
                    except shutil.Error:
                        print(f'{file} already moved')
                #installs
                if file.lower().endswith(('.exe', '.msi')):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{download_path}\Installs' )
                        print(f'Moved {file} to D:\Downloads\Installs')
                    except shutil.Error:
                        print(f'{file} already moved')
                #PDF
                if file.lower().endswith('.pdf'):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{pdf_path}' )
                        print(f'Moved {file} to {programming_path}\Python')
                    except shutil.Error:
                        print(f'{file} already moved')
                #Python
                if file.lower().endswith('.py'):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{programming_path}\Python' )
                        print(f'Moved {file} to {programming_path}\Python')
                    except shutil.Error:
                        print(f'{file} already moved')
                #C-Sharp
                if file.lower().endswith('.cs'):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{programming_path}\C#' )
                        print(f'Moved {file} to {programming_path}\C#')
                    except shutil.Error:
                        print(f'{file} already moved')
                #C++
                if file.lower().endswith('.h') or file.lower().endswith('.cpp'):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{programming_path}\C++' )
                        print(f'Moved {file} to {programming_path}\C++')
                    except shutil.Error:
                        print(f'{file} already moved')
                #Docx
                if file.lower().endswith(('.docx','.doc')):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{desktop_path}')
                        print(f'Moved {file} to {programming_path}\C++')
                    except shutil.Error:
                        print(f'{file} already moved')
                #Zip Files
                if file.lower().endswith('.zip'):
                    try:
                        shutil.move(f'{download_path}\{file}',f'{zip_path}')
                        os.chdir(zip_path)
                        zip = zipfile.ZipFile(file)
                        zip.extractall(f'{extracted_zip_path}\\{file}'.replace('.zip',''))
                        print(f'Moved {file} to {extracted_zip_path}\\{file}')
                    except shutil.Error:
                        print(f'{file} already moved')


