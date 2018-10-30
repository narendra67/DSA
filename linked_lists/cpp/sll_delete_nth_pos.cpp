#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    Node* next;
};

Node* head;

void Insert(int data, int pos){
    Node* node = new Node();
    node->data = data;
    node->next = NULL;
    if(pos == 1) {
        node->next = head;
        head = node;
        return;
    }
    Node* temp = head;
    for(int i=0; i<pos-2; i++) {
        temp = temp->next;
    }
    node->next = temp->next;
    temp->next = node;
}

void Delete(int pos) {
    Node* temp = head;
    if (pos == 1) {
        head = temp->next;
        return;
    }
    for(int i = 0; i < pos-2; i++) {
        temp = temp->next;
    }
    temp->next = temp->next->next;
}

void Print() {
    Node* temp = head;
    printf(" List: ");
    while(temp != NULL) {
        printf("%d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    head = NULL;
    Insert(4, 1);
    Insert(3, 2);
    Insert(9, 3);
    Print();
    Delete(1);
    Print();
}