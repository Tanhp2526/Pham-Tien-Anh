class TextAnalyzer(object):
    def __init__(self, text):
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText

    def freAll(self):
        wordlist = self.fmtText.split(' ')
        arr = {}
        for word in wordlist:
            arr[word] = wordlist.count(word)
        return arr
    
    def freOf(self,word):
        freDict = self.freAll()

        if word in freDict:
            return freDict[word]
        else:
            return 0
        
string = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Tạo object từ class
analyzer = TextAnalyzer(string)

# Task 2: tần suất tất cả từ
print("Tần suất tất cả từ:")
print(analyzer.freAll())

# Task 3: tần suất 1 từ cụ thể
print("\nTần suất từ 'diam':", analyzer.freOf("diam"))
print("Tần suất từ 'lorem':", analyzer.freOf("lorem"))
print("Tần suất từ 'hello':", analyzer.freOf("hello"))  # từ không tồn tại


