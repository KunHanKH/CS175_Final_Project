import os

imdir = 'images'

if not os.path.isdir(imdir):
    os.mkdir(imdir)

hand_folders = [folder for folder in os.listdir('.') if 'hand' in folder]

print(hand_folders)

n = 0
for folder in hand_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1
