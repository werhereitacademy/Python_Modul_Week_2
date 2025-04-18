import json,sys
#save movie data in dictionary
try:
    def write_json(new_data, filename='data.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data.append(new_data)
            file.seek(0)
            return json.dump(file_data, file, indent = 4)

    mname = input("Enter movie name ")
    mdirector = input("Enter movie director name ")
    myear = int(input("Enter year "))
    genre = input("Enter Genre ")
    dic={}
    dic.update({"title":mname,"director":mdirector,"year":myear,"genre":genre})
    write_json(dic)
    print("Data saved in file and showing data from file")
    f = open('data.json')
    data = json.load(f)
    for i in data:
        print(f"{i}\n")
    f.close()
    sys.exit()
except:
    print("Please eneter numbers")
