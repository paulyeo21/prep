class Substitute:
    def getValue(self, key, code):
        keys = {}
        for i in range(len(key)):
            keys[key[i]] = (i + 1) % 10
        output = ""
        for char in code:
            if char in keys:
            	output += str(keys[char])
        return output

substitute = Substitute()
print(substitute.getValue("TRADINGFEW", "LGXWEV"))
