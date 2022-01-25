def FindFromFile(s, file):
    TextData = open(file).readlines()
    if s == "INSTRUCTIONS":
        LineNumber = 0
        for Line in TextData:  
            if Line.startswith(s):
                    break
            else: LineNumber = LineNumber + 1
        Instruc = ''
        for i in range(LineNumber+1,LineNumber+5):
                temp = "\n" if i < LineNumber + 4 else ''
                Instruc += TextData[i]+temp
        return Instruc

    else:
        for Line in TextData:  
            if Line.startswith(s):
                return Line[len(s)+1:len(Line)].strip()

def FindInText(s, text):
    Line = text[text.find(s):len(text)]
    return Line[len(s)+1:len(Line)].strip() #added 1 for colon