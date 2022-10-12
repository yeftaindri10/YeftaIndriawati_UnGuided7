class StackList:
    def __init__(self):
        self.stack_data = list()

    def push(self, new_data):
        self.stack_data.append(new_data)

    def top(self):
        if len(self.stack_data) ==0:
            return None
        else:
            return self.stack_data[-1]

    def pop(self):
        if len(self.stack_data) == 0:
            return None
        else:
            pop_data = self.stack_data.pop()
            return pop_data

    def size(self):
         len(self.stack_data)


class UndoRedo:
    def __init__(self):
        self.mainStack = StackList() #stack ini sebagai tempat menyimpan data pertama kali
        self.backupStack = StackList() #stack ini sebagai tempat menyimpan data yang di hapus

    def write(self,data):
            self.mainStack.push(data)
            print(f"{data} berhasil ditambahkan!")
            print()

    def undo(self):
        if self.mainStack.size() == 0 :
            print("Perintah Undo Tidak Dapat Di Lakukan")
            print(f"Data Undo = {None}")
            print()
        else:
            bantu = self.mainStack.pop()
            self.backupStack.push(bantu)
            for i in range (len(self.mainStack.stack_data)):
                print(self.mainStack.stack_data[i], end=" ")
            print()
            print()

    def redo(self):
        if self.backupStack.size() == 0 :
            print("Perintah Redo Tidak Dapat Di Lakukan")
            print(f"Data Redo = {None}")
            print()
        else:
            bantu = self.backupStack.pop()
            self.mainStack.push(bantu)
            for i in range (len(self.mainStack.stack_data)):
                print(self.mainStack.stack_data[i], end=" ")
            print()
            print()

    def printInfo(self):
        for i in range (len(self.mainStack.stack_data)):
            print(self.mainStack.stack_data[i], end=" ")
        print()
        print()





#TEST CASE 
if __name__ == '__main__':
    obj_undoredo = UndoRedo()
    obj_undoredo.undo() #Test case Jika belum ada data yang ditambahkan
    obj_undoredo.redo() #Test case jika belum ada data yang di undo
    obj_undoredo.write("ada Suatu Hari hiduplah seorang kakek-kakek")
    obj_undoredo.write("Dia tinggal sebatang kara di pegunungan")
    obj_undoredo.write("Dia kemudian turun gunung buat kuliah")
    obj_undoredo.write("SEMESTER 5 BANYAK TUGASSSSSSS !!!")
    obj_undoredo.printInfo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.redo()
    obj_undoredo.redo()
