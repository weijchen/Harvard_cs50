# encoding: utf-8

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

# rewind 倒轉；轉回
# seek() 用於移動文件讀取指針到指定的位置
# 0 代表移至文件開頭
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

# print whole file
print "First let's print the whole file:\n"

print_all (current_file)

# rewind part, for printing purpose
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# seperatly print the line 1, 2 and 3
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
