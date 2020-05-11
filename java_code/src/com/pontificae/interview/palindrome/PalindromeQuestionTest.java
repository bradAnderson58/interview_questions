package com.pontificae.interview.palindrome;

import org.junit.Assert;
import org.junit.Test;

public class PalindromeQuestionTest {

    @Test
    public void testPalindrome() {
        final String otto = "otto";
        final String hannah = "hannah";
        final String tacocat = "tacocat";

        Assert.assertTrue(PalindromeQuestion.isPalindrome(otto));
        Assert.assertTrue(PalindromeQuestion.isPalindrome(hannah));
        Assert.assertTrue(PalindromeQuestion.isPalindrome(tacocat));
    }

    @Test
    public void testNotPalindrome() {
        Assert.assertFalse(PalindromeQuestion.isPalindrome("notpalindrome"));
        Assert.assertFalse(PalindromeQuestion.isPalindrome("tacohat"));
        Assert.assertFalse(PalindromeQuestion.isPalindrome("otot"));
    }
}
