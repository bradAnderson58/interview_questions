var assert = require('assert')
var loginUtility = require('./remove_dups')


describe('Removing Duplicates', () => {

  it('should remove the duplicates', () => {
    assert.equal('hello'.length, 5);
    var noDuplicates = loginUtility.removeDuplicates([1, 2, 2, 2, 3, 4, 5])

    assert.equal(noDuplicates, [1, 2, 3, 4, 5]);
  });

});