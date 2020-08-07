using System;
using System.Linq;

namespace semantic_version
{
    static class SemanticVersion
    {
        public static string GetGreaterVersion(string v1, string v2)
        {
            var splitV1 = v1?.Split(".").Where(s => s != "").ToArray();
            var splitV2 = v2?.Split(".").Where(s => s != "").ToArray();

            if (splitV1 is null ||
                splitV2 is null ||
                splitV1.Length + splitV1.Length != 6)
            {
                throw new InvalidFormatException();
            }

            
            foreach (var (first, second) in splitV1.Zip(splitV2))
            {
                if (!int.TryParse(first, out var firstInt))
                    throw new NonNumericValueException();

                if (!int.TryParse(second, out var secondInt))
                    throw new NonNumericValueException();

                if (firstInt > secondInt)
                    return v1;
                else if (secondInt > firstInt)
                    return v2;
            }

            return v1;
        }

    }

    class NonNumericValueException : Exception
    {

    }

    class InvalidFormatException : Exception
    {

    }
}
