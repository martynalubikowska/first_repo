import os

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop')
print(os.getcwd())
os.mkdir('new_folder')
os.rename('new_folder', 'new_folder_2')
os.rmdir('new_folder_2')
