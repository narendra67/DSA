#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node* next;
};

void Insert(Node** pointerToHead, int x) {
    struct Node* temp = (Node*) malloc(sizeof(Node*));
    temp->data = x;
    temp->next = NULL;
    if (*pointerToHead != NULL) temp->next = *pointerToHead;
    *pointerToHead = temp;
}

void Print(Node* head) {
    // struct Node* temp = head;
    printf("List: ");
   while(head != NULL) {
       printf(" %d", head->data);
       head = head->next;
   } 
    printf("\n");
}


int main() {
    Node* head = NULL;
    // head = NULL; //empty list
    printf("How many numbers do you like to enter? \n");
    int n,i,x;
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        printf("Enter the number: \n");
        scanf("%d", &x);
        Insert(&head, x);
        Print(head);
    }
}