#include <iostream>
#include <limits> // for numeric_limits

template <typename T>
class PriorityQueueNode {
public:
    T data;
    int priority;

    PriorityQueueNode(T d, int p) : data(d), priority(p) {}

    // Overload <= to compare priorities
    bool operator<=(const PriorityQueueNode& other) const {
        return priority >= other.priority;
    }
};

template <typename T>
class PriorityQueue {
private:
    struct Node {
        PriorityQueueNode<T> value;
        Node* next;
    };

    Node* head;

public:
    PriorityQueue() : head(nullptr) {}

    ~PriorityQueue() {
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    void enqueue(const T& data, int priority) {
        PriorityQueueNode<T> newNode(data, priority);

        // If the list is empty or the new node has higher priority than the head
        if (head == nullptr || newNode <= head->value) {
            Node* temp = new Node{newNode, head};
            head = temp;
        } else {
            // Traverse the list to find the correct position
            Node* current = head;
            while (current->next != nullptr && current->next->value <= newNode) {
                current = current->next;
            }

            // Insert the new node
            Node* temp = new Node{newNode, current->next};
            current->next = temp;
        }

        displayQueue();
    }

    T dequeue() {
        if (isEmpty()) {
            throw std::out_of_range("PriorityQueue is empty");
        }

        T result = head->value.data;
        Node* temp = head;
        head = head->next;
        delete temp;

        displayQueue();

        return result;
    }

    bool isEmpty() const {
        return head == nullptr;
    }

    void displayQueue() const {
        std::cout << "Queue: ";
        Node* current = head;
        while (current != nullptr) {
            std::cout << "(" << current->value.data << ", " << current->value.priority << ") ";
            current = current->next;
        }
        std::cout << std::endl;
    }
};

int main() {
    PriorityQueue<std::string> pq;

    while (true) {
        std::cout << "1. Enqueue Task\n";
        std::cout << "2. Dequeue Task\n";
        std::cout << "3. Quit\n";

        int choice;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        if (choice == 1) {
            std::string task;
            int priority;

            std::cout << "Enter task: ";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::getline(std::cin, task);

            std::cout << "Enter priority: ";
            std::cin >> priority;

            pq.enqueue(task, priority);
        } else if (choice == 2) {
            if (!pq.isEmpty()) {
                std::cout << "Dequeued: " << pq.dequeue() << std::endl;
            } else {
                std::cout << "Queue is empty.\n";
            }
        } else if (choice == 3) {
            break;
        } else {
            std::cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}
