using System;
using Xunit;

namespace semantic_version
{
    public class SemanticVersionTests
    {
        [Theory]
        [InlineData("1.1.0", "1.2.0", "1.2.0")]
        [InlineData("1.2.0", "1.2.0", "1.2.0")]
        public void Tests(string arg1, string arg2, string answer)
        {
            Assert.Equal(answer, SemanticVersion.GetGreaterVersion(arg1, arg2));
        }

        [Theory]
        [InlineData("1.a.0", "1.2.0", typeof(NonNumericValueException))]
        [InlineData("", "1.2.0", typeof(InvalidFormatException))]
        [InlineData(null, "1.2.0", typeof(InvalidFormatException))]
        [InlineData("1.2.3.4.5.6", "1.2.0", typeof(InvalidFormatException))]
        [InlineData("1..6", "1.2.0", typeof(InvalidFormatException))]
        [InlineData("1.6", "1.2.0", typeof(InvalidFormatException))]
        public void ExceptionTests(string arg1, string arg2, Type exceptionType)
        {
            Assert.Throws(exceptionType, () =>
            {
                SemanticVersion.GetGreaterVersion(arg1, arg2);
            });
        }
    }
}
