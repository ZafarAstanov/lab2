def child(masd):
    mas = []
    for d in masd:
        for ch in d['children']:
            if ch['age'] > 18:
                mas.append(d['name'])
                break
    return mas

Vasya = {
    "name": "Vasya",
    "age": 39,
    "children": [{
        "name": "Lena",
        "age": 13,
    }, {
          "name": "Sasha",
          "age": 23,
        }],
}

Vasilisa = {
    "name": "Vasilisa",
    "age": 43,
    "children": [{
        "name": "Anatoliy",
        "age": 19,
    }, {
        "name": "Gera",
        "age": 10,
    }],
}

Stiven = {
    "name": "Stiven",
    "age": 44,
    "children": [{
        "name": "Victor",
        "age": 14,
    }, {
        "name": "Samuel",
        "age": 44,
    }],
}
emps = [Vasya, Vasilisa, Stiven]
print(child(emps))