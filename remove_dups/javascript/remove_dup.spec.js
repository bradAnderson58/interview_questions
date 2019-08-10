var assert = require('assert')
var listUtil = require('./remove_dups')


describe('Removing Duplicates', () => {

  it('should remove the duplicates', () => {
    var noDuplicates = listUtil.removeDuplicates([1, 2, 2, 2, 3, 4, 5])

    assert.deepEqual(noDuplicates, [1, 2, 3, 4, 5]);
  });

  it('should remove duplicates out of order', () => {
    var noDuplicates = listUtil.removeDuplicates([5, 2, 4, 6, 2, 7, 4, 99, 5, 2, 11]);

    assert.deepEqual(noDuplicates, [5, 2, 4, 6, 7, 99, 11]);
  });

  it('should work for strings as well', () => {
    var noDuplicates = listUtil.removeDuplicates(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])

    assert.deepEqual(noDuplicates, ['one', 'fish', 'two', 'red', 'blue']);
  });

  it('should work for objects also', () => {
    var noDuplicates = listUtil.removeDuplicates([{one: 'fish'}, {two: 'fish'}, {one: 'fish'}, {one: 'blue'}]);

    assert.deepEqual(noDuplicates, [{one: 'fish'}, {two: 'fish'}, {one: 'blue'}]);
  });

});