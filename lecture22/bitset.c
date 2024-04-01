/* bitset.c */

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* Type Definitions */

typedef int64_t Bitset;

/* Functions */

void	bitset_add(Bitset *b, int value) {
    *b |= (1L<<value);
}

bool	bitset_contains(Bitset *b, int value) {
    return *b & (1L<<value);
}

void	bitset_remove(Bitset *b, int value) {
    *b &= ~(1L<<value);
}

/* Main Execution */

int main(int argc, char *argv[]) {
    int numbers[] = {4, 6, 6, 3, 7, -1};
    Bitset bitset = 0;

    printf("Bitset: %ld\n", bitset);
    
    // Add numbers to bitset
    for (int *np = numbers; *np >= 0; np++) {
    	bitset_add(&bitset, *np);
    }
    printf("Bitset: %ld\n", bitset);

    // Check bitset for numbers
    for (int i = 0; i < 10; i++) {
    	printf("Bitset contains %d? %d\n", i, bitset_contains(&bitset, i));
    }
    
    // Remove numbers from bitset
    for (int *np = numbers; *np >= 0; np++) {
    	bitset_remove(&bitset, *np);
    }
    printf("Bitset: %ld\n", bitset);

    return 0;
}
