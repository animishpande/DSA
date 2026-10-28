using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DSAinC_.PracticeProblems;
// Intuition
/*
    To find the k most frequent elements, we need to first find out how many times each element appears. Once
    we get the count, we can sort the list based on how many times each element appears. After sorting, the 
    most frequent elements naturally appear at the end of the list.
    This approach is easy to reason about:
    count the frequencies -> sort by frequencies -> take the top k.
*/
// Algorithm
/*
    1. Create a hash map to store the frequency of each number
    2. Build the list of [frequency, number] pair from the map
    3. Sort this list in ascending order based on frequency
    4. Create an empty result list
    5. Repeatedly pop from the end of the sorted list (highest frequency) and append the number to the result
    6. Stop when the result contains k elements
    7. Return the result list
*/
public class TopKFrequentElements
{
    public static int[] FindTopKElements(int[] nums, int k)
    {
        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (count.ContainsKey(num)) count[num]++;
            else count[num] = 1;
        }

        List<int[]> arr = count.Select(entry => new int[] {entry.Value, entry.Key}).ToList();
        arr.Sort((a, b) => b[0].CompareTo(a[0]));

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = arr[i][1];
        }
        return res;
    }

}
