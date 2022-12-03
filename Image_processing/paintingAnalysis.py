#command line access to the properties calculation
from painting import Painting

def main():
    imageAddress = input("enter the file path")
    painting1 = Painting("test", imageAddress)
    painting1.preprocessing()
    painting1.calculateProperties()
    print(painting1.getPropertiesList())

if __name__=='__main__':
    main()
