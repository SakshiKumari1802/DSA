import java.util.*;

class Solution {

    class SegmentTree {
        int[] tree;
        int n;

        SegmentTree(int n) {
            this.n = n;
            tree = new int[4 * (n + 1)];
        }

        void update(int idx, int val) {
            update(1, 0, n, idx, val);
        }

        private void update(int node, int l, int r, int idx, int val) {
            if (l == r) {
                tree[node] = val;
                return;
            }

            int mid = (l + r) >> 1;

            if (idx <= mid) {
                update(node * 2, l, mid, idx, val);
            } else {
                update(node * 2 + 1, mid + 1, r, idx, val);
            }

            tree[node] = Math.max(tree[node * 2], tree[node * 2 + 1]);
        }

        int query(int left, int right) {
            if (left > right) return 0;
            return query(1, 0, n, left, right);
        }

        private int query(int node, int l, int r, int ql, int qr) {
            if (ql > r || qr < l) return 0;

            if (ql <= l && r <= qr) {
                return tree[node];
            }

            int mid = (l + r) >> 1;

            return Math.max(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            );
        }
    }

    public List<Boolean> getResults(int[][] queries) {
        final int MAXX = 50000;

        TreeSet<Integer> obstacles = new TreeSet<>();
        obstacles.add(0);

        // Add all obstacles that will ever exist
        for (int[] q : queries) {
            if (q[0] == 1) {
                obstacles.add(q[1]);
            }
        }

        SegmentTree seg = new SegmentTree(MAXX);

        // Build initial gaps
        Integer prev = 0;
        for (Integer pos : obstacles) {
            if (pos == 0) continue;
            seg.update(pos, pos - prev);
            prev = pos;
        }

        List<Boolean> ans = new ArrayList<>();

        // Process queries in reverse
        for (int i = queries.length - 1; i >= 0; i--) {
            int[] q = queries[i];

            if (q[0] == 2) {
                int x = q[1];
                int sz = q[2];

                Integer pre = obstacles.floor(x);

                int bestGap = seg.query(0, x);
                int tailGap = x - pre;

                ans.add(Math.max(bestGap, tailGap) >= sz);

            } else {
                int pos = q[1];

                Integer left = obstacles.lower(pos);
                Integer right = obstacles.higher(pos);

                if (right != null) {
                    seg.update(right, right - left);
                }

                seg.update(pos, 0);
                obstacles.remove(pos);
            }
        }

        Collections.reverse(ans);
        return ans;
    }
}