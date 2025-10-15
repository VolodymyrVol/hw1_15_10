# '''Створіть програму, що містить інформацію про відомих баскетболістів. 
# Збережіть ПІБ та зріст кожного баскетболіста.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. 
# Використовуйте словник для збереження інформації.'''

# players = {"Michael Jordan": 198, "LeBron James": 206}

# print(players)

# #create
# name = "Kobe Bryant"
# height = 198
# players[name] = height
# print(players)

# #update
# name = "Kobe Bryant"
# height = 199
# players[name] = height
# print(players)

# #delete
# name = "Michael Jordan"
# del players[name]
# print(players)

# #edit
# rep_name = "Kobe Bryant"
# new_name = "Shaquille O'Neal"
# players[new_name] = players.pop(rep_name)
# print(players)

# #find
# name = "LeBron James"
# if name in players:
#     print(name, "-", players[name])

# '''Створіть програму «Англо-французький словник». 
# Збережіть слово англійською та його переклад на французьку. 
# Реалізуйте можливість додавати, видаляти, знахо­дити та змінювати дані. 
# Використовуйте словник для збереження інформації.'''

# eng_fra = {"hello": "bonjour", "goodbye": "au revoir", "please": "s'il vous plaît"}
# print(eng_fra)

# #create
# word = "thank you"
# translation = "merci"
# eng_fra[word] = translation
# print(eng_fra)

# #update
# word = "thank you"
# translation = "je vous remercie"
# eng_fra[word] = translation
# print(eng_fra)

# #delete
# word = "hello"
# del eng_fra[word]
# print(eng_fra)

# #edit
# rep_word = "please"
# new_word = "excuse me"
# eng_fra[new_word] = eng_fra.pop(rep_word)
# print(eng_fra)

# #find
# word = "goodbye"
# if word in eng_fra:
#     print(word, "-", eng_fra[word])

'''Створіть програму «Фірма», яка зберігає інформацію про працівників: 
ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype.
Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. 
Використовуйте словник для збереження інформації.'''

# employees = {
#     "John Smith": {
#         "phone": "+1234567890",
#         "email": "john.smith@company.com",
#         "position": "Software Engineer",
#         "room": "404",
#         "skype": "john.smith.work"
#     },
#     "Jane Doe": {
#     "phone": "+1987654321",
#     "email": "jane.doe@company.com",
#     "position": "Project Manager",
#     "room": "405",
#     "skype": "jane.doe.work"
#     }
# }
# print(employees)


# #create

# name = "Alice Johnson"
# employees[name] = {
#     "phone": "+1122334455",
#     "email": "Alice@company.com",
#     "position": "Data Analyst"
# }
# #print(employees)

# #update
# name = "Alice Johnson"
# update_param = "room"
# new_value = "406"
# if name in employees:
#     employees[name][update_param] = new_value
# #print(employees)

# #delete
# name = "John Smith"
# if name in employees:
#     del employees[name]
# #print(employees)

# #edit
# rep_name = "Jane Doe"
# new_name = "Janet Doe"
# if rep_name in employees:
#     employees[new_name] = employees.pop(rep_name)
# #print(employees)

# #find
# name = "Alice Johnson"
# if name in employees:
#     print(name, "-", employees[name])

books = {
    "1984": {
        "author": "George Orwell",
        "genre": "Science Fiction",
        "year": 1949,
        "pages": 328,
        "publisher": "Secker and Warburg"
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "genre": "Novel",
        "year": 1925,
        "pages": 180,
        "publisher": "Charles Scribner's Sons"
    }
}
print(books)

# create
title = "The Hobbit"
books[title] = {
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "year": 1937,
    "pages": 310,
    "publisher": "Allen & Unwin"
}
# print(books)

# update
title = "The Hobbit"
update_param = "pages"
new_value = 320
if title in books:
    books[title][update_param] = new_value
# print(books)

# delete
title = "1984"
if title in books:
    del books[title]
# print(books)

# edit 
old_title = "The Great Gatsby"
new_title = "Gatsby"
if old_title in books:
    books[new_title] = books.pop(old_title)
# print(books)

# find
title = "The Hobbit"
if title in books:
    print({title} - books[title])


