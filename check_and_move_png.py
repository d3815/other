import os
import shutil
from PIL import Image

'''
    проходим по всем файлам в папке
    проверяем размеры (должны быть не больше 256 по обеим сторонам)
    переносим их в новую папку
'''

path_to_png_dir = '/ipad-hd'

for d, dirs, files in os.walk(os.getcwd() + path_to_png_dir):
    for one_file in files:
        if one_file.endswith('.png'):
            path = os.path.join(d, one_file)
            print(path)
            work_img = Image.open(path)
            (width, height) = work_img.size
            if width < 256:
                if height < 256:
                    res = '/result'
                    c = d
                    new_path = d + res
                    print(new_path)
                    if not os.path.exists(new_path):
                        os.mkdir(new_path)
                    print(f'Файл {path} перемещен')
                    shutil.move(path, new_path)
