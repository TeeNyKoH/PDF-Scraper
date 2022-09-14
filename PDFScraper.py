from PyPDF2 import PdfReader



def readFromPDF(filename):
    reader = PdfReader(filename + ".pdf")
    number_of_pages = len(reader.pages)
    page_content = ''

    for page_number in range(number_of_pages):
        page = reader.getPage(page_number)
        page_content += page.extractText() 
        # page = reader.pages[number_of_pages]
        # text = page.extract_text()

    print(number_of_pages)
    print(page_content)
    
    print("Enter the name of the text file: ")
    filename = input()
    filename = filename + ".txt"
    with open(filename, 'w') as f:
        f.write(page_content)
    return filename





    

# working do not change!

def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()

    firstRead = []



    for i in lines:
        firstRead.append(i) #firstRead is the listname
        
    for i in firstRead:
        if i ==" \n":
            firstRead.remove(i)
                

    jsonfile=""

    def algo(firstRead):
        
    
        
        for i in firstRead:
            print(i)
            if "Bachelor" in i:
                course1 = i.split("Applicable", 1)[0] 
                print("course1", course1)
                return course1
            elif "YEAR" in i:
                year = i.split("TRIMESTER", 1)[0]
                tri = i.split("TRIMESTER", 1)[1]   
                print("year", year, "tri", tri) 
                return year,tri
            elif "YEAR" in i and firstRead.index(i) !=  "YEAR"   :
                num = firstRead.index(i)
                num = num + 1
                
                print("num", num)
                return num
                
            elif i[0:2].isdigit() is False and i[3:7].isdigit() is True:
                modcode = i[0:8]
                print("test")
                print("modcode", modcode)
                return modcode
                
    for i in firstRead:
        if "Bachelor" in i:
            course1 = i.split("Applicable", 1)[0] 
            print("course1", course1)
                

        # print(i)
        
        if "YEAR" in i:
            year = i.split("TRIMESTER", 1)[0]
            tri = i.split("TRIMESTER", 1)[1]   
            print("year", year, "tri", tri) 

        
         
        if i[0:2].isdigit() is False and i[3:7].isdigit() is True:
            modcode = i[0:8]
            modName = i.split()
            modName = modName[:-2]
            modName = modName[1:]
            modName = ' '.join(modName)
            if "Core" in i:
                core = "Core"
            else:
                core = "Elective"
            credits = i[-3:]
            print("Course: ", course1)
            print("modcode: ", modcode)
            print("modName: " , modName)
            print("year", year, "tri", tri) 
            print("Module Type: " , core)
            print("credits: " , credits)
            
            # jsonfile = {"CourseName":course1, "ModCode": modcode , "ModName": modName, "Year":year, "Tri":tri, "ModType": core, "Credits": credits}
            # '{"CourseName":' + course1 + ', "ModCode": ' + modcode + ', "ModName": ' + modName + ', "Year":' + year + ', "Tri":' + tri + ', "ModType": ' + core + ', "Credits": ' + credits + '}'
            jsonfile = jsonfile +'{"CourseName":' + course1 + ', "ModCode": ' + modcode + ', "ModName": ' + modName + ', "Year":' + year + ', "Tri":' + tri + ', "ModType": ' + core + ', "Credits": ' + credits + '}'
            

    print(jsonfile)
    print("what json file do you want to write into?")
    jsonfilename = input()
    jsonfilename = jsonfilename + '.txt'
    f = open(jsonfilename, "a")
    f.write(jsonfile)
    print("Sucessfully write into " + jsonfilename)
    f.close()



def main():
    print("Enter the name of the pdf file: ")
    pdfname = input()
    filename = readFromPDF(pdfname)
    readfile(filename)
        
main()
