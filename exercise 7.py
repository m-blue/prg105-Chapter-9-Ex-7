fin = open('words.txt')

def three(word):
    letter_n = 0
    count = 0
    while letter_n < len(word)-1:
        if word[letter_n] == word[letter_n+1]:
            count = count + 1
            if count == 3:
                return True
            letter_n = letter_n + 2
        else:
            count = 0
        letter_n = letter_n + 1
    return False


hi = fin.readline().strip()
i = 0
total = 113809

while i < total:

    if three(hi):
        print hi
    hi = fin.readline().strip()
    i = i + 1

