def VersionValue(val):
    NewVal = str(val).replace(".","")
    if len(NewVal) == 2:
        return str(NewVal+"0")
    elif len(NewVal) == 3:
        return str(NewVal)