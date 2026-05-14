function reverseList(head: ListNode | null): ListNode | null {
    let new_list = null;

    while (head) {
        let next_node = head.next
        head.next = new_list
        new_list = head
        head = next_node
    }
    return new_list;
};

class ListNode2 {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
