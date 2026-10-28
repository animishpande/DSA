using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DSAinC_.PracticeProblems;

public class ProductOfArrayExceptSelf
{
    public int[] ProductExceptSelf(int[] nums)
    {
        int[] res = new int[nums.Length];

        for(int i = 0; i < nums.Length; i++)
        {
            int val = 1;
            for (int j = 0; j < nums.Length; j++)
            {
                if (i != j)
                {
                    val *= nums[j];
                }
            }
            res[i] = val;
        }
        return res;
    }
}
