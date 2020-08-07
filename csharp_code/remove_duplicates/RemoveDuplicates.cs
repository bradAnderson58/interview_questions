using System.Collections.Generic;
using System.Linq;

namespace remove_duplicates
{
    static class RemoveDuplicatesExtension
    {
        public static IEnumerable<T> RemoveDuplicates<T>(this IEnumerable<T> one)
            => one?.Distinct();
    }
}