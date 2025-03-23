import os

folder_to_read = r"C:\Users\Virgil MESLE\Nextcloud\ROBUSTA-1U\ROBUSTA-1E_ENSO\ENSO-DATA\ENSO-DATA-PFM"

exit_file = 'all_file.txt'


with open(exit_file,'w') as fichier :
    for path, subdirs, files in os.walk(folder_to_read):
        for name in files:
            print(os.path.join(path, name))
            fichier.write(os.path.join(path, name)+'\n')


            