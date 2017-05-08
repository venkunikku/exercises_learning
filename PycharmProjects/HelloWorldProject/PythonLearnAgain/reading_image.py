with open('/home/venku/Pictures/frenchflag.png','rb') as b:
    all_lines = b.readlines()
    for line in all_lines:
        print(line)
        #print('{:02x}'.format(ord(line)))