class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<int> lower(26, 0), upper(26, 0);

        // Count lowercase and uppercase letters
        for (char ch : word) {
            if (islower(ch))
                lower[ch - 'a'] = 1;
            else
                upper[ch - 'A'] = 1;
        }

        int count = 0;

        // Check letters appearing in both cases
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i])
                count++;
        }

        return count;
    }
};