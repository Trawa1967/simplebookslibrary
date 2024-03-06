#book_view

from book_model import Book

def showAllView(list):
    
    for entry in list:
        print('|'+"{:^5}".format(entry[0])+'|'+ "{:<70}".format(entry[1])+'|'+"{:<30}".format(entry[2])+'|'+"{:<30}".format(entry[3])+'|'+"{:^6}".format(entry[4])+'|')
    # print("|----------------------------------------------------------------------------------------------------|")
    # input("\n\nNaciśnij [ENTER]...")
    # print('In our db we have %i books. Here they are:' % len(list))
    # for item in list:
    #     print(item.position())
def startView():
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("| id  |                    Title                                             |          Author              !          Publisher           | Year |")
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")

def endView():
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")
    input("\n\nNaciśnij [ENTER]...")
    print("Goodbye")

