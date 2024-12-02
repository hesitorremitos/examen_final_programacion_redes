#!/usr/bin/env python3

import requests

# Se requiere la biblioteca json para authenticarse
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"


def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(f"{APIHOST}/api/v1/loginViaBasic", auth=authCreds)
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(
            f"Status code {r.status_code} and text {r.text}, while trying to Auth."
        )


def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={"Content-type": "application/json", "X-API-Key": apiKey},
        data=json.dumps(book),
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(
            f"Error code {r.status_code} and text {r.text}, while trying to add book {book}."
        )


# Get the Auth Token Key
apiKey = getAuthToken()


# Insersion de libro a la bliblioteca
libro = {
    "id": 20,
    "title": "Examen Final",
    "author": "Hector Condori Chambi",
}

addBook(libro, apiKey)

# COmprobamos que el libro se a aniadido
response = requests.get(f"{APIHOST}/api/v1/books")

print("Peticion GET a la api ")
print(response.json())
