from datetime import datetime
with open ("m.txt" , "a") as txt:
    txt.write('\nAccessed on ' + str(datetime.now()))