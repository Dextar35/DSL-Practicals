#include <iostream>
#include <string>
using namespace std;
struct Node {
    int prn;
    string name;
    Node* next;
};
class PinnacleClub {
private:
    Node* head; 

public:
    PinnacleClub() : head(nullptr) {}
    void addMember(int prn, const string& name) {
        Node* newNode = new Node{prn, name, nullptr};
        if (!head) {
            head = newNode;
        } else {
            newNode->next = head;
            head = newNode;
        }
    }
    void deleteMember(int prn) {
        Node* current = head;
        Node* prev = nullptr;

        while (current && current->prn != prn) {
            prev = current;
            current = current->next;
        }

        if (current) {
            if (prev) {
                prev->next = current->next;
            } else {
                head = current->next;
            }

            delete current;
        }
    }
    int totalMembers() {
        int count = 0;
        Node* current = head;

        while (current) {
            count++;
            current = current->next;
        }
        return count;
    }
    void displayMembers() {
        Node* current = head;

        while (current) {
            cout << "PRN: " << current->prn << ", Name: " << current->name << endl;
            current = current->next;
        }
    }
    void concatenateLists(PinnacleClub& otherList) {
        Node* current = head;

        while (current->next) {
            current = current->next;
        }

        current->next = otherList.head;
    }
};
void clearInputBuffer() {
    cin.clear();
}
void displayMenu() {
    cout << "\nMenu:\n"
         << "1. Add Member\n"
         << "2. Delete Member\n"
         << "3. Display Total Members\n"
         << "4. Display Members\n"
         << "5. Concatenate Lists\n"
         << "6. Exit\n"
         << "Enter your choice: ";
}
int main() {
    PinnacleClub division1, division2;
    int choice;
    do {
        displayMenu();
        cin >> choice;
        switch (choice) {
            case 1: {
                int prn;
                string name;
                cout << "\nEnter PRN: ";
                cin >> prn;
                cout << "Enter Name: ";
                cin>>name;
                division1.addMember(prn, name);
                cout << "Member added successfully.\n";
                break;
            }
            case 2: {
                int prn;
                cout << "\nEnter PRN to delete: ";
                cin >> prn;
                division1.deleteMember(prn);
                cout << "Member deleted successfully.\n";
                break;
            }
            case 3:
                cout << "\nTotal Members: " << division1.totalMembers() << endl;
                break;
            case 4:
                cout << "\nDivision 1 Members:" << endl;
                division1.displayMembers();
                break;
            case 5:
                cout << "\nEnter members for Division 2:" << endl;
                int numMembers;
                cout << "Enter the number of members: ";
                cin >> numMembers;
                for (int i = 0; i < numMembers; ++i) {
                    int prn;
                    string name;
                    cout << "Enter PRN: ";
                    cin >> prn;
                    clearInputBuffer();
                    cout << "Enter Name: ";
                    getline(cin, name);
                    division2.addMember(prn, name);
                }
                division1.concatenateLists(division2);
                cout << "Lists concatenated successfully.\n";
                break;
            case 6:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice. Please enter a valid option.\n";
                clearInputBuffer();
        }
    } while (choice != 6);
    return 0;
}
