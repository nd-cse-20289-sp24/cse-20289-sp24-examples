/* list.c */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <dirent.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

/* Node Structure */

typedef struct Node Node;
struct Node {
    char *  path;
    size_t  size;
    Node *  next;
};

Node *  node_create(const char *path, size_t size) {
    Node *n = calloc(1, sizeof(Node));
    if (n) {
        n->path = strdup(path);
        n->size = size;
    }
    return n;
}

void    node_delete(Node *n) {
    // Base case: invalid Node
    if (!n) return;

    // Recursive case: delete next Node
    node_delete(n->next);

    // Release path string
    free(n->path);

    // Release Node structure
    free(n);
}

/* List Structure */

typedef struct {
    Node *head;
} List;

void    list_add(List *l, const char *path, size_t size) {
    Node *n = node_create(path, size);

    if (!l->head) { // Case 1: Empty list
        l->head = n;
    } else {        // Case 2: Add to end of list
        Node *tail = l->head;
        while (tail->next) {
            tail = tail->next;
        }

        tail->next = n;
    }
}

/* Functions */

void    add_files(const char *root, List *files) {
    /* Open directory for reading */
    DIR *d = opendir(root);
    if (!d) {
        fprintf(stderr, "Unable to opendir on %s: %s\n", root, strerror(errno));
        return;
    }

    /* Iterate through directory entries */
    for (struct dirent *e = readdir(d); e; e = readdir(d)) {
        if (strcmp(e->d_name, ".") == 0 || strcmp(e->d_name, "..") == 0) {
            continue;
        }

        // Construct full path
        char path[BUFSIZ];
        sprintf(path, "%s/%s", root, e->d_name);

        // Get file metadata
        struct stat s;
        if (stat(path, &s) < 0) {
            continue;
        }

        // Only add files
        if (e->d_type == DT_REG) {
            list_add(files, path, s.st_size);
        }
    }

    closedir(d);
}

void    print_files(List *files) {
    /* Iterate through list of files and print path and size */
    for (Node *curr = files->head; curr; curr = curr->next) {
        printf("[%8lu] %s\n", curr->size, curr->path);
    }
}

/* Main Execution */

int main(int argc, char *argv[]) {
    char root[BUFSIZ];

    /* Determine directory */
    if (argc == 2) {
        strncpy(root, argv[1], BUFSIZ);
    } else {
        getcwd(root, BUFSIZ);
    }

    /* Add files and print them */
    List files = {0};
    add_files(root, &files);
    print_files(&files);

    /* Release resources */
    node_delete(files.head);

    return EXIT_SUCCESS;
}

/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
