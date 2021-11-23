def swapFileDataText():
    file1 = input("Enter file name:- ")
    file2 = input("Enter file name:- ")


    with open(file1, 'read') as a:
        data_a = a.read()

	with open(file2, 'read') as b:
         datab = b.read()

    with open(file1, 'write') as a:
        a.write(datab)

    with open(file2, 'write') as b:
        b.write(data_a)

swapFileDataText()
