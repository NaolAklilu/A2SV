class Node {
    int key;
    int val;
    Node prev;
    Node next;

    Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    Node head;
    Node tail;
    int capacity;
    int length;
    Map<Integer, Node> nodes;

    public LRUCache(int capacity) {
        this.head = null;
        this.tail = null;
        this.capacity = capacity;
        this.length = 0;
        this.nodes = new HashMap<>();
    }

    int get(int key) {
        if (!nodes.containsKey(key)) {
            return -1;
        }

        Node curNode = nodes.get(key);
        Node leftNode = curNode.prev;
        Node rightNode = curNode.next;

        if (curNode == tail) {
            return curNode.val;
        }

        tail.next = curNode;
        curNode.prev = tail;
        curNode.next = null;
        tail = curNode;

        if (leftNode != null) {
            leftNode.next = rightNode;
            if (rightNode != null) {
                rightNode.prev = leftNode;
            }
        } else {
            head = rightNode;
            if (rightNode != null) {
                rightNode.prev = null;
            }
        }

        return tail.val;
    }

    void put(int key, int value) {
        if (head == null) {
            Node newNode = new Node(key, value);
            head = newNode;
            tail = newNode;
            length++;

            nodes.put(key, newNode);
        } else {
            int result = get(key);

            if (result == -1) {
                if (length == capacity) {
                    nodes.remove(head.key);
                    head = head.next;
                    if (head != null) {
                        head.prev = null;
                    }
                } else {
                    length++;
                }

                Node newNode = new Node(key, value);
                tail.next = newNode;
                newNode.prev = tail;
                tail = newNode;

                if (head == null) {
                    head = newNode;
                }

                nodes.put(key, newNode);
            } else {
                tail.val = value;
                nodes.put(key, tail);
            }
        }
    }
}