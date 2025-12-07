#File handling

#If any file has content and need to open via python


# f=open("give file name with extension")
# And to READ the file c=f.read()
# Print that file content print(c)

#To WRITE in that file f.write("banana")

# if the file mode is in r=read mode we cannot write

# so to make it in write mode add w in open("filename.txt","w")

#After wrting the content inside the file we need to give f.close to make it save and exit

#if not it will show blank in file nothing will save
#But it will overwrite the content so old data will get delete and new data will store

#if we give read after close we cannot do cause file is closed so need to give open again

# To make the file reand and write give open("file.txt","r+")



# To avoid overwrite use opne(.txt,a)
# a-- append the value with out delete the old values


a=open("test.txt","r+")
print(a.read())
a=open("test.txt","a")
a.write("hi\n")
a.close()
a=open("test.txt","r+")
print(a.read())