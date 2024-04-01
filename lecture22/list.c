/* list.c */

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

/* Node Structure */

typedef struct Node Node;
struct Node {
    int	   data;
    Node  *next;
};

Node *	node_create(int data, Node *next) {
    Node *n = malloc(sizeof(Node));
    if (n) {
    	n->data = data;
    	n->next = next;
    }
    return n;
}

void	node_delete(Node *n, bool recursive) {
    if (!n) {
    	return;
    }

    if (recursive) {
	node_delete(n->next, recursive);
    }
    free(n);
}

/* List Structure */

typedef struct {
    Node *head;
} List;

bool	list_contains(List *l, int value) {
    for (Node *curr = l->head; curr; curr = curr->next) {
    	if (curr->data == value)
    	    return true;
    }
    return false;
}

void	list_add(List *l, int value) {
    if (list_contains(l, value)) {
    	return;
    }

    l->head = node_create(value, l->head);
}

void	list_remove(List *l, int value) {
    Node *prev = NULL;
    Node *curr = l->head;

    while (curr && curr->data != value) {
    	prev = curr;
    	curr = curr->next;
    }

    if (!curr) {
    	return;
    }

    if (!prev) {
    	l->head = curr->next;
    } else {
    	prev->next = curr->next;
    }

    node_delete(curr, false);
}

void	list_dump(List *l) {
    for (Node *curr = l->head; curr; curr = curr->next) {
    	printf("%d\n", curr->data);
    }
}

/* Main Execution */

int main(int argc, char *argv[]) {
    int numbers[] = {4, 6, 6, 3, 7, -1};
    List list     = {NULL};

    // Add numbers to bitset
    for (int *np = numbers; *np >= 0; np++) {
    	list_add(&list, *np);
    }
    list_dump(&list);

    // Check bitset for numbers
    for (int i = 0; i < 10; i++) {
    	printf("List contains %d? %d\n", i, list_contains(&list, i));
    }

    // Remove numbers from bitset
    for (int *np = numbers; *np >= 0; np++) {
    	list_remove(&list, *np);
    }
    list_dump(&list);

    return 0;
}
