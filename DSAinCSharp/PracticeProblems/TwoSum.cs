namespace DSAinCSharp.PracticeProblems;

public class TwoSum
{
    public static int[] FindTwoSum(int[] nums, int target)
    {
        if (nums.Length == 1)
        {
            return [nums[0]];
        }

        var fin = new List<int>();
        for(int i = 0; i < nums.Length; i++)
        {
            for(int j = 1; j < nums.Length; j++)
            {
                if (i != j && nums[i] + nums[j] == target && fin.Count == 0)
                {
                    fin.Add(i);
                    fin.Add(j);
                    break;
                }
            }
        }
        return fin.ToArray();
    }
}
