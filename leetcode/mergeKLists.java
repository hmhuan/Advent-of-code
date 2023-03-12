// https://leetcode.com/problems/merge-k-sorted-lists/description/
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        ListNode result = null;
        ListNode next = null;
        for (int i= 0; i<lists.length; i++) {
            while (lists[i] != null) {
                minHeap.add(lists[i].val);
                lists[i] = lists[i].next;
            }
        }
        
        while (minHeap.size() > 0) {
            if (result == null) {
                result = new ListNode(minHeap.poll());
                next = result;
            } else {
                next.next = new ListNode(minHeap.poll());
                next = next.next;
            }
        }
        return result;
    }
}
