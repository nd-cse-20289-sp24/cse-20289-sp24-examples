SOURCE=		$(wildcard *.c)
TARGET=		$(SOURCE:.c=)

all:		$(TARGET)

%:		%.c
	gcc -Wall -g -std=gnu99 -o $@ $<

clean:
	rm -f $(TARGET)
