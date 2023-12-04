#include <iostream>
#include <cstdlib>
using namespace std;
struct Node {
    int data;
    Node* next;
    Node* prev;
};
class DoublyLinkedList {
private:
    Node* head;
public:
    DoublyLinkedList() : head(nullptr) {}
    void insertAtBeginning(int digit) {
        head = new Node{digit, head, nullptr};
        if (head->next) {
            head->next->prev = head;
        }
    }
    void onesComplement() {
        Node* current = head;
        while (current) {
            current->data = 1 - current->data;
            current = current->next;
        }
    }
    void twosComplement() {
        onesComplement();
        int carry = 1;
        Node* current = head;
        while (current) {
            int sum = current->data + carry;
            current->data = sum % 2;
            carry = sum / 2;
            current = current->next;
        }
        if (carry) {
            head = new Node{1, head, nullptr};
            if (head->next) {
                head->next->prev = head;
            }
        }
    }
    static DoublyLinkedList addBinaryNumbers(const DoublyLinkedList& num1, const DoublyLinkedList& num2) {
        DoublyLinkedList result;
        int carry = 0;
        Node* node1 = num1.head;
        Node* node2 = num2.head;
        while (node1 || node2) {
            int sum = carry + (node1 ? node1->data : 0) + (node2 ? node2->data : 0);
            result.insertAtBeginning(sum % 2);
            carry = sum / 2;
            if (node1) node1 = node1->next;
            if (node2) node2 = node2->next;
        }
        if (carry) {
            result.insertAtBeginning(carry);
        }
        return result;
    }
    void displayBinaryNumber() const {
        Node* current = head;
        while (current) {
            cout << current->data;
            current = current->next;
        }
        cout << endl;
    }
};
void clearInputBuffer() {
    cin.clear();
}
void displayMenu() {
    cout << "\nMenu:\n1. 1's Complement\n2. 2's Complement\n3. Add Binary Numbers\n4. Exit\nEnter choice: ";
}
int main() {
    DoublyLinkedList binaryNum1, binaryNum2, result;
    int choice;
    do {
        displayMenu();
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "\nEnter a binary number: ";
                while (true) {
                    int digit;
                    cin >> digit;
                    if (digit == 0 || digit == 1) {
                        binaryNum1.insertAtBeginning(digit);
                    } else {
                        cout << "Invalid input. Enter binary digits only (0 or 1).\n";
                        clearInputBuffer();
                        continue;
                    }
                    char ch;
                    cout << "Add another binary digit? (y/n): ";
                    cin >> ch;
                    if (ch != 'y') {
                        break;
                    }
                }
                cout << "1's Complement: ";
                binaryNum1.onesComplement();
                binaryNum1.displayBinaryNumber();
                break;
            case 2:
                cout << "\nEnter a binary number: ";
                while (true) {
                    int digit;
                    cin >> digit;
                    if (digit == 0 || digit == 1) {
                        binaryNum1.insertAtBeginning(digit);
                    } else {
                        cout << "Invalid input. Enter binary digits only (0 or 1).\n";
                        clearInputBuffer();
                        continue;
                    }
                    char ch;
                    cout << "Add another binary digit? (y/n): ";
                    cin >> ch;
                    if (ch != 'y') {
                        break;
                    }
                }
                cout << "2's Complement: ";
                binaryNum1.twosComplement();
                binaryNum1.displayBinaryNumber();
                break;
            case 3:
                cout << "\nEnter the first binary number: ";
                while (true) {
                    int digit;
                    cin >> digit;
                    if (digit == 0 || digit == 1) {
                        binaryNum1.insertAtBeginning(digit);
                    } else {
                        cout << "Invalid input. Enter binary digits only (0 or 1).\n";
                        clearInputBuffer();
                        continue;
                    }
                    char ch;
                    cout << "Add another binary digit? (y/n): ";
                    cin >> ch;
                    if (ch != 'y') {
                        break;
                    }
                }
                cout << "\nEnter the second binary number: ";
                while (true) {
                    int digit;
                    cin >> digit;
                    if (digit == 0 || digit == 1) {
                        binaryNum2.insertAtBeginning(digit);
                    } else {
                        cout << "Invalid input. Enter binary digits only (0 or 1).\n";
                        clearInputBuffer();
                        continue;
                    }
                    char ch;
                    cout << "Add another binary digit? (y/n): ";
                    cin >> ch;
                    if (ch != 'y') {
                        break;
                    }
                }
                result = DoublyLinkedList::addBinaryNumbers(binaryNum1, binaryNum2);
                cout << "Sum of Binary Numbers: ";
                result.displayBinaryNumber();
                break;
            case 4:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice. Please enter a valid option.\n";
                clearInputBuffer();
        }
    } while (choice != 4);
    return 0;
}
