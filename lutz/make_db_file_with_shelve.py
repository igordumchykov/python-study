from lutz.initdata import db
import shelve

if __name__ == '__main__':
    dbfilename = 'people-file-shelve'
    with shelve.open(dbfilename) as file_db:
        for key in db:
            file_db[key] = db[key]

    with shelve.open(dbfilename) as loaded_db:
        for key in loaded_db:
            print(key, '=>', loaded_db[key])
