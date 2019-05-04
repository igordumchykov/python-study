"""Save people to db"""
import pickle
from lutz.initdata import db

dbfilename = 'people-file-pickle'


def storeDbase(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    dbfile = open(dbfilename, 'rb')
    db = pickle.load(dbfile)
    dbfile.close()
    return db


def print_db(db):
    for key in db:
        print(key, '=>', db[key])


if __name__ == '__main__':
    storeDbase(db)
    loaded_db = loadDbase()
    print_db(loaded_db)
