using System.Runtime.InteropServices;

public class Solution {
    public int FirstUniqChar(string s) {
        var map = new Dictionary<char, int>();

        for(int i = 0; i < s.Length; i++){
            if(map.ContainsKey(s[i]!))
            {
                map[s[i]] = 1;
            }
            else
            {
                map[s[i]]++;
            }
        }

        int i = 0;
        foreach(var ch in map)
        {
            if(map[i] == 1)
            {
                return i;
            }
            i++;
        }
        return -1;
    }
}