using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using Xunit;

namespace remove_duplicates
{
    public class UnitTest1
    {
        [Theory]
        [InlineData(new[] { 1, 2, 2, 2, 3, 4, 5 }, new[] { 1, 2, 3, 4, 5 })]
        [InlineData(new[] { 5, 2, 4, 6, 2, 7, 4, 99, 5, 2, 11 }, new[] { 5, 2, 4, 6, 7, 99, 11 })]
        public void TestInts(int[] items, int[] expected)
        {
            AssertSequenceEqual(items.RemoveDuplicates(), expected);
        }

        [Theory]
        [InlineData(new[] { "one", "fish", "two", "fish", "red", "fish", "blue", "fish" }, new[] { "one", "fish", "two", "red", "blue" })]
        public void TestStrings(string[] items, string[] expected)
        {
            AssertSequenceEqual(items.RemoveDuplicates(), expected);
        }

        [Fact]
        public void TestComparableObjects()
        {
            var items = new[] { new TestObject("fish", "fish"), new TestObject("red", "blue"), new TestObject("fish", "fish"), new TestObject("red", "blue") };
            var expected = new[] { new TestObject("fish", "fish"), new TestObject("red", "blue") };

            AssertSequenceEqual(items.RemoveDuplicates(), expected);
        }

        class TestObject : IEqualityComparer<TestObject>
        {
            private readonly string _s1;
            private readonly string _s2;

            public TestObject(string s1, string s2)
            {
                _s1 = s1;
                _s2 = s2;
            }

            public bool Equals(TestObject x, TestObject y)
            {
                return x._s1 == y._s1 &&
                        x._s2 == y._s2;
            }

            public int GetHashCode(TestObject obj)
            {
                return HashCode.Combine(obj._s1.GetHashCode(), obj._s2.GetHashCode());
            }

            public override string ToString()
            {
                return $"({_s1}, {_s1})";
            }

            public override bool Equals(object obj)
            {
                return obj is TestObject other
                    ? Equals(this, other)
                    : false;
            }
        }

        static void AssertSequenceEqual<T>(IEnumerable<T> one, IEnumerable<T> two)
        {
            foreach (var (first, second) in one.Zip(two))
                Assert.True(first.Equals(second), $"{first} != {second}");
        }
    }
}
