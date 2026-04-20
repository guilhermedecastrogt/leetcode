using System.Formats.Tar;
using System.Globalization;

public class Solution {
    public int MaximumLengthSubstring(string s) {
        int pl = 0;
        int pr = 0;
        int _max = 1;
        var map = new Dictionary<int, string>();

        map[s[0]] = 1;

        while (pr < (s.Length()-1))
        {
            pr++;
            if(map[s[pr]])
            {
                map[s[pr]] += 1;
            }
            else
            {
                map[s[pr]] = 1;
            }

            while (map[s[pr]] == 3)
            {
                map[s[pl]] = -1;
                pl++;
            }
            
            if (_max < pr - pl + 1)
            {
                _max = pr-pl+1;
            }
        }

        return _max;
    }
}