# CODIGO PARA PRACTICA 1.4 PALINDROMOS

# Codigo para las clases
words = ['anita', 'lava', 'la', 'tina']
words_result = []
for item in words:
    for word in item.split():
        words_result.append(word)

print(words)
print(words_result)