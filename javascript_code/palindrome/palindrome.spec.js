const assert = require('assert');
const palindrome = require('./palindrome');

describe('Determining Palindromes', () => {

  it('should detect palindromes', () => {
    const otto = 'otto';
    const hannah = 'hannah';
    const tacocat = 'tacocat';

    assert.ok(palindrome.isPalindrome(otto));
    assert.ok(palindrome.isPalindrome(hannah));
    assert.ok(palindrome.isPalindrome(tacocat));
  });

  it('should reject non-palindromes', () => {
    assert.fail(palindrome.isPalindrome('notpalindrome'));
    assert.fail(palindrome.isPalindrome('tacohat'));
    assert.fail(palindrome.isPalindrome('otot'));
  });
});