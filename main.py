import os
path = r"file"
file = os.listdir(path)
class find:
    def filecount(self,file):
        i = 0
        a = True
        for e in file:
            if i>=2:
                print('file count is more than 2 ')
                a = False
                break
            else:
                i+=1
                continue
        return a
    def filetype(self,file):
        for e in file:
            print(f"file name '{e}' extension is '{e.split('.')[1]}'")
    def display(self,file):
        a = self.filecount(file)
        if a==True:
           self.filetype(file)
        else:

            print("cant process")
x = find()
x.display(file)
