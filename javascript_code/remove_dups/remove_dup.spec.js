// npm test
var assert = require('assert');
var listUtil = require('./remove_dups');


describe('Removing Duplicates', () => {

  it('should remove the duplicates', () => {
    const noDuplicates = listUtil.removeDuplicates([1, 2, 2, 2, 3, 4, 5]);

    assert.deepEqual(noDuplicates, [1, 2, 3, 4, 5]);
  });

  it('should remove duplicates out of order', () => {
    const noDuplicates = listUtil.removeDuplicates([5, 2, 4, 6, 2, 7, 4, 99, 5, 2, 11]);

    assert.deepEqual(noDuplicates, [5, 2, 4, 6, 7, 99, 11]);
  });

  it('should work for strings as well', () => {
    const noDuplicates = listUtil.removeDuplicates(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']);

    assert.deepEqual(noDuplicates, ['one', 'fish', 'two', 'red', 'blue']);
  });

  /*
  it('should work for objects also', () => {
    const noDuplicates = listUtil.removeDuplicates([{one: 'fish'}, {two: 'fish'}, {one: 'fish'}, {one: 'blue'}]);

    assert.deepEqual(noDuplicates, [{one: 'fish'}, {two: 'fish'}, {one: 'blue'}]);
  });
  */

  
  it('should square the numbers', () => {
    var squares = listUtil.squareSorted([1, 2, 3, 4, 5]);
    assert.deepEqual(squares, [1,4,9,16,25]);
  });

  it('should handle negatives', () => {
    var squares = listUtil.squareSorted([-5, -4, 0, 3, 7]);
    assert.deepEqual(squares, [0, 9, 16, 25, 49])
  });

});