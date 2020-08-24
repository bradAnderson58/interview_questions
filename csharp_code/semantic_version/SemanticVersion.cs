using System;
using System.Linq;

namespace semantic_version
{
    static class SemanticVersion
    {
        /// <summary>
        /// A normal version number
        /// MUST take the form X.Y.Z where X, Y, Z are non-negative integers
        /// MUST NOT contain leading zeroes.X is the major version,
        /// Each element MUST increase numerically.For instance 1.9.0 -> 1.10.0 -> 1.11.0
        /// </summary>
        public static string GetGreaterVersion(string v1, string v2)
        {
            var splitV1 = v1?.Split(".");
            var splitV2 = v2?.Split(".");

            if (splitV1.Length + splitV1.Length != 6)
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
