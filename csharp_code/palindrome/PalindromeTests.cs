using System;
using Xunit;

namespace palindrome
{
    public class PalindromeTests
    {
        [Theory]
        [InlineData("otto", true)]
        [InlineData("hannah", true)]
        [InlineData("tacocat", true)]
        [InlineData("notpalindrome", false)]
        [InlineData("tacohat", false)]
        [InlineData("otot", false)]
        public void TestPalindrome(string str, bool isPalindrome)
        {
            Assert.Equal(isPalindrome, str.IsPalindrome());
        }
    }
}
