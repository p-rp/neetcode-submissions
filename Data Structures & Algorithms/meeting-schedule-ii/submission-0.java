/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort((a, b) -> a.start-b.start);

        int days = 1;

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals.get(i).start < intervals.get(i-1).end)
                days++;
        }

        return days;
    }
}
