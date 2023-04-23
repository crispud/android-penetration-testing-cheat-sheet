#!/usr/bin/env python3

import pyrebase

config = {
	"apiKey": "apiKey",
	"authDomain": "authDomain.firebaseapp.com",
	"databaseURL": "https://databaseURL.firebaseio.com",
	"storageBucket": "storageBucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

print(db.get())
