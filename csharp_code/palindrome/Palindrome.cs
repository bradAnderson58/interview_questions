using System;
using System.Linq;

namespace palindrome
{
    static class Palindrome
    {
        public static bool IsPalindrome(this string str)
            => str is null
            ? false
            : str.Reverse().SequenceEqual(str);
    }
}
