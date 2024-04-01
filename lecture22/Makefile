CC=		gcc
CFLAGS=		-Wall -g -std=gnu99
LD=		gcc
LDFLAGS=

all:		bitset list

%:		%.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f bitset list
