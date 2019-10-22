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
                    
                #Videos
                if file.lower().endswith(video_extentions):
                    movefile(f'{download_path}\{file}', video_path)  
                   
                #installs
                if file.lower().endswith(('.exe', '.msi')):
                    movefile(f'{download_path}\{file}',f'{download_path}\Installs' )
                
                #PDF
                if file.lower().endswith('.pdf'):
                    movefile(f'{download_path}\{file}', pdf_path)
                   
                #Python
                if file.lower().endswith('.py'):
                    movefile(f'{download_path}\{file}',f'{programming_path}\Python' )
                   
                #C-Sharp
                if file.lower().endswith('.cs'):
                    movefile(f'{download_path}\{file}', f'{programming_path}\C#')
                   
                #C++
                if file.lower().endswith('.h') or file.lower().endswith('.cpp'):
                    movefile(f'{download_path}\{file}',f'{programming_path}\C++' )
                
                #Docx
                if file.lower().endswith(('.docx','.doc')):
                    movefile(f'{download_path}\{file}', desktop_path)
                
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


