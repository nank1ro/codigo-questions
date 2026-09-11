A **linked list** stores values in separate **nodes** scattered in memory: each node holds a value and a pointer to the next node, and the last one points to `NULL`. The pointer inside refers to the type being declared, so the struct needs a **tag** to name itself; the `typedef` name does not exist yet inside the braces:
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Nodes are linked by storing the address of one in the `next` of another, and the members of the pointed node are reached with the arrow:
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Nodes declared as local variables disappear when their function returns, so lists are built on the **heap** with `malloc` from `stdlib.h`. It reserves the requested number of bytes and returns their address, or `NULL` when memory is exhausted; `sizeof(Node)` is the right amount for one node:
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
Heap memory is never released on its own: every node obtained from `malloc` must be handed back with `free(node)` once it is no longer needed. In these exercises `stdlib.h` is included and `Node` is declared above your code.

---

A list is held by a single pointer to its first node, the **head**. Every other node is reached from the head by following `next`, and the arrow can be chained: `head->next` is the second node and `head->next->next` the third. An empty list is a head equal to `NULL`, and the `next` of the last node is `NULL` too, so following one arrow too many dereferences `NULL` and crashes the program.

---

Walking a list, called **traversal**, is a loop that starts at the head and follows `next` until it reaches `NULL`. A `for` loop expresses it in a single line, with a pointer as the loop variable:
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
There is no index: the only way to reach a node is through the pointer stored in the one before it.

---

Adding a node at the **front** creates it, makes it point to the current head and returns it as the new head. The caller stores the result back into its head variable:
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Pushing onto an empty list works the same way: the new node points to `NULL` and becomes the whole list.

---

Freeing a list means freeing every node, one traversal step at a time. The `next` pointer must be saved **before** the node is freed, because a freed node must not be read any more, not even its `next`:
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Writing `free(head)` and then `head = head->next` reads memory that was just released, which is undefined behaviour. `free(NULL)` is allowed and does nothing, so an empty list needs no special case.

---

A list does not store its length: it has to be counted with a traversal. The `while` form of the loop keeps the pointer outside, which is handy when the loop body updates other variables:
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
For an empty list the loop body never runs and the count stays `0`.

---

Adding a node at the **back** needs the last node, the one whose `next` is `NULL`. The function walks until it finds it, then attaches the new node there and returns the unchanged head:
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
When the list is empty there is no last node to walk to: the new node is simply returned as the head.

---

Searching a list is a traversal that compares each value and stops at the first match. The function returns a pointer to the node it found, or `NULL` when it reaches the end of the list without a match:
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Returning the node rather than the value lets the caller modify it or use it as a starting point for another operation.

---

After `free(p)` the variable `p` still holds the old address, but the memory it points to is no longer yours: `p` is now a **dangling pointer**. Reading or writing through it, or freeing it a second time, is undefined behaviour: the program may print the old value, print garbage or crash, and the compiler will not complain. When a pointer must outlive the `free`, set it to `NULL` right after, so that any later use is caught by a `NULL` check instead.

---

Inserting **after** a given node needs no traversal: the new node takes over the successor of `node`, then `node` is pointed at the new one:
```c
new_node->next = node->next;
node->next = new_node;
```
The order of the two assignments matters: setting `node->next` first would overwrite the only pointer to the rest of the list, and those nodes would be lost. Inserting after the last node works too, since its `next` is `NULL`.

---

Removing the first node is the mirror of `push_front`: save the address of the second node, free the first one and return the saved address as the new head. The caller stores the result back into its head variable:
```c
Node *next = head->next;
free(head);
return next;
```
Popping until the head is `NULL` frees the whole list, one node per call.

---

Removing a node in the middle needs the node **before** it, so the traversal keeps two pointers: `prev`, the node already visited, and `cur`, the one being examined. When `cur` matches, `prev->next` is made to skip it and `cur` is freed. If the match is the head itself, `prev` is still `NULL` and the new head is `cur->next`:
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
When no node matches, the list is returned unchanged.

---

Reversing a list turns every `next` pointer around, in place, with three pointers: `prev` is the part already reversed, `head` the node being processed and `next` a copy of the rest of the list, saved before the link is changed. At each step the current node is pointed back at `prev`, then both `prev` and `head` move forward:
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
When `head` reaches `NULL` every link has been flipped and `prev` is the new head.

---

A linked list is cheap where an array is expensive, and the other way round. Adding or removing at the **front** is a couple of pointer assignments whatever the length, while an array would have to shift every element. On the other hand nodes are not contiguous, so there is no `list[i]`: reaching the n-th node, the last one or the total length means walking from the head through every node in between. Programs that append often keep a second pointer to the last node, the **tail**, to avoid that walk.

---

Putting it together: a list is often built from an array. Pushing at the front reverses the order, so the array is walked **backwards**, from the last element to the first, and the first element ends up at the head. The program then prints the list with a traversal and frees it node by node, so that every `malloc` is matched by a `free`.
