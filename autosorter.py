import os, sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

def get_directory():
    logging.info('Введите название папки, которую нужно отсортировать...')
    try:
        directory = input('>>> ')
        return directory
    except KeyboardInterrupt:
        print()
        logging.info('Программа зашершена!')
        sys.exit()

def view_files(directory):
    try:
        files = os.listdir(f'./{directory}')
        logging.info('Добавленные файлы для сортировки\n')
        print(*files, sep='\n')
        print()
        return files
    except FileNotFoundError:
        logging.error('Папка не найдена!')
        sys.exit()
    

def check_directory():
    paths = ['./docs', './video', './music', './image', './program', './arhives']
    logging.info('Проверка директорий для сортировки...')
    for path in paths:
        if os.path.isdir(path):
            logging.info(f'Директория {path} есть!')
            continue
        else:
            logging.warning(f'Директории {path} добавлена!')
            os.makedirs(f'{path}', exist_ok=True)
    return paths


def parsing(files):
    logging.info('Парсинг файлов...')
    for file in files:
        extension = Path(file).suffix
        sorter(directory, file, extension)


def sorter(directory, file, extension):
    if extension in ['.pdf', '.ods', '.docx', '.xlsx', '.xls', 
                     '.csv', '.txt', '.md']:
        os.rename(f'./{directory}/{file}', f'./docs/{file}')
        logging.info('Файл добавлен в папку с документами...')

    elif extension in ['.mp4', '.avi', '.mkv', '.mov', '.wmv',
                       '.flv', '.webm', '.m4v', '.3gp', '.ts', '.mts']:
        os.rename(f'./{directory}/{file}', f'./video/{file}')
        logging.info('Файл добавлен в папку с видео...')

    elif extension in ['.mp3', '.wav', '.flac', '.acc', '.ogg',
                       '.wma', '.m4a', '.opus', '.mid', '.midi']:
        os.rename(f'./{directory}/{file}', f'./music/{file}')
        logging.info('Файл добавлен в папку с музыкой...')

    elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', 
                       '.tiff', '.tif', '.webp', '.svg', '.ico', 
                       '.psd', '.ai', '.raw', '.cr2', '.nef']:
        os.rename(f'./{directory}/{file}', f'./image/{file}')
        logging.info('Файл добавлен в папку с изображениями...')

    elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso',
                       '.deb']:
        os.rename(f'./{directory}/{file}', f'./arhives/{file}')
        logging.info('Файл добавлен в папку с архивами...')

    elif extension in ['.exe', '.msi', '.bin', '.sh', '.bat', '.cmd',
                       '.app', '.apk', '.jar', '.run']:
        os.rename(f'./{directory}/{file}', f'./program/{file}')
        logging.info('Файл добавлен в папку с программами...')

    else:
        logging.info(f'Неизвестный тип файла {file}')



def cleaner(check):
    paths = check
    for path in paths:
        try:
            if os.path.getsize(path) == 0:
                os.rmdir(f'{path}')
                logging.warning(f'Удаление {path} (не использовано)')
        except OSError:
            logging.info(f'Директория {path} используется')
            continue



directory = get_directory()
files = view_files(directory)
check = check_directory()
res = parsing(files)
clean = cleaner(check)


logging.info('Сортировка завершена!')