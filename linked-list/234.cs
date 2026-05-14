using System.Diagnostics.Contracts;

public class Solution {
    public bool IsPalindrome(ListNode head) {
        var arr = new List<int>();
        int p = 0;

        while (head != null)
        {
            arr.Add(head.val);
            head = head.next;
            p++;
        }

        var pl = 0;
        var pr = arr.Count-1;
        var arrReverted = new List<int>();
        while (pr > pl)
        {
            if(arr[pr] != arr[pl]) return false;
            pl++;
            pr--;
        }
        return true;
    }
}

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
        next = null;
    }
}