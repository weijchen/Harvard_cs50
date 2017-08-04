
# clean:
	# rm -f *.o a.out core fifteen log.txt
 # Hacked-together make file for use with Harvard cs50 on-line course excercises
  # Type terminal commands as follows: make EXE=yourFileName (don't add extensions)
  
# the compiler: gcc for C program, define as g++ for C+ use clang for Harvard stuff
CC = clang

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -ggdb3 -O0 -std=c11 -Wall -Werror
  
# link THIS for the cs50 functions (add others as needed):
LDLIBS = -lcs50 -lm

# the build target executable:
TARGET = $(EXE)

all: $(TARGET)

$(TARGET): $(TARGET).c
	$(CC) $(CFLAGS) $(LDLIBS) $(TARGET).c