import eel, os, random, hashlib


eel.init('web')


@eel.expose
def pick_file(folder):
    def get_hash_md5(file):
        m = hashlib.md5()
        m.update(file.encode('utf-8'))
        print(m.hexdigest())
        return m.hexdigest()
    if os.path.isdir(folder):
        path = os.listdir(folder)
        file = random.choice(path)
        print(file)
        return file, get_hash_md5(file)
    else:
        return 'Ошибочный путь 😩'

eel.start('file_access.html', size=(960, 400))

