def swapFileDate():

    file1 = input("enter the file")
    file2 = input("enter file to be swapped")

    with open(file1, 'r') as a:
    data_a = a.read()

     with open(file2, 'r') as b:
    data_b = b.read()


    with open(file1, 'w') as a:
    a.write(data.b)
    with open(file2, 'w') as b:
    b.write(data.a)

    swapFileData():