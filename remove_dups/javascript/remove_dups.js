
module.exports = ListUtility();


function ListUtility() {
  return {
    removeDuplicates: removeDuplicates
  }


  /*
    Removes duplicate entries from a list
   */
  function removeDuplicates(dupsList) {
    var firsts = {};
    var noDups = []
    for (ind in dupsList) {
      var key = dupsList[ind];
      if (typeof(key) === 'object') {
        key = JSON.stringify(key);
      } 

      if (!firsts[key]) {
        firsts[key] = true;
        noDups.push(dupsList[ind])
      }
    }
    return noDups;
  }
}
