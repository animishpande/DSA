namespace DSAinCSharp.PracticeProblems;

// Group Anagrams Problem LeetCode
public class Solution
{
    public static List<List<string>> GroupAnagrams(string[] strs)
    {
        var dict = new Dictionary<string, List<string>>();
        foreach(string s in strs)
        {
            var cArr = s.ToCharArray();
            Array.Sort(cArr);
            var sVal = new string(cArr);
            if (!dict.ContainsKey(sVal))
            {
                dict[sVal] = new List<string>();
            }
            dict[sVal].Add(s);
        }
        return dict.Values.ToList();
    }
}