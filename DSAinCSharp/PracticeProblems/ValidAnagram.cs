namespace PracticeProblems;

public class ValidAnagrams
{
    public static bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length)
        {
            return false;
        }

        var sChar = s.ToCharArray();
        var tChar = t.ToCharArray();
        Array.Sort(sChar);
        Array.Sort(tChar);
        var sString = new string(sChar);
        var tString = new string(tChar);
        return sString.Equals(tString);
    }
}