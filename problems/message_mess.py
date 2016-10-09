class MessageMess:
    def restore(self, dictionary, message):
        d = {}
        max_length = 0
        for word in dictionary:
            d[word] = True
            if len(word) > max_length:
                max_length = len(word)

        output = []
        for i in range(len(message)):
            for j in range(i + 1, i + max_length + 1):
                if j <= len(message):
                    if message[i:j] in d:
                        output.append(message[i:j])
        return " ".join(output)


message_mess = MessageMess()
print(message_mess.restore(["HI", "YOU", "SAY"], "HIYOUSAYHI"))
print(message_mess.restore(["ABC", "BCD", "CD", "ABCB"], "ABCBCD"))
print(message_mess.restore(["IMPOSS", "SIBLE", "S"], "IMPOSSIBLE"))
