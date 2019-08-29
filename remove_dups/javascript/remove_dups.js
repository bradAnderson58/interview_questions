
module.exports = ListUtility();


function ListUtility() {
  return {
    removeDuplicates: removeDuplicates,
    squareSorted: squareSorted
  }


  /*
    Removes duplicate entries from a list
   */
  function removeDuplicates(dupsList) {
    return dupsList;
  }

  function squareSorted(sortedList) {
    return sortedList.map(num => num * num);
  }
}
