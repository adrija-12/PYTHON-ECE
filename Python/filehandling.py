import os
class Filehandling:
    def main():
        x=str(input("Enter a file name: "))
        y=str(input("Enter some text in the file: "))
        b=open(x,"w")
        b.write(y)
        b.close()
        print(x,"\nFile created successfully")
        print("\n\t\t............Reading fie contents............")
        z=open(x,"r")
        print("\n")
        print(z.read())
    def filedelete():
        xyz=input("Enter the file to delete: ")
        a=os.remove(xyz)
        print("File deleted successfully")
Filehandling.main()
Filehandling.filedelete()