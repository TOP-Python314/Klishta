phrase = input().split()
words = [word.strip('.,:;!?–—\'\"()*/') for word in  phrase]
right_phrase = " ".join(words)
print(right_phrase)

# ВВОД:
# Было темно в гостиной. Лаптев, не садясь и держа шляу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.
# ВЫВОД:
# Было темно в гостиной Лаптев не садясь и держа шляу в руках стал извиняться за беспокойство он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита