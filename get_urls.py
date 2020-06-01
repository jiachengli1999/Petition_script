file1 = open('urls.txt', 'r') 
file2 = open('change_urls.txt', 'w')
Lines = file1.readlines() 

for line in Lines:
    if '.change.org' in line:
        file2.writelines(line)

file1.close()
file2.close()