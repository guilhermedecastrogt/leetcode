public class Solution
{
    public int MissingNumber(int[] nums)
    {
        int x = 0;

        foreach (int num in nums)
        {
            x ^= num;
        }

        for (int i = 0; i <= nums.Length+1; i++)
        {
            x ^= i;
        }

        return x;
    }
}