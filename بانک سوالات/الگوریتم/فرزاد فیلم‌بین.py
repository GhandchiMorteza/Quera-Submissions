for i in range(int(input())):
    words = input().split()
    print(*[word[0].upper() + word[1:].lower() for word in words])