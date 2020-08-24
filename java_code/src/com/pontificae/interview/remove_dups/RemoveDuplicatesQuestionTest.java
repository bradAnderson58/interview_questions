package com.pontificae.interview.remove_dups;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

class TestObject {
    public String one;
    public String two;

    TestObject(String one, String two) {
        this.one = one;
        this.two = two;
    }
}

public class RemoveDuplicatesQuestionTest {

    @Test
    public void testRemoveDuplicates() {
        final List<Integer> duplicates = Arrays.asList(1, 2, 2, 2, 3, 4, 5);
        final List<Integer> noDuplicates = RemoveDuplicatesQuestion.removeDuplicates(duplicates);

        Assert.assertEquals(noDuplicates, Arrays.asList(1, 2, 3, 4, 5));
    }

    @Test
    public void testRemoveOutOfOrder() {
        final List<Integer> duplicates = Arrays.asList(5, 2, 4, 6, 2, 7, 4, 99, 5, 2, 11);
        final List<Integer> noDuplicates = RemoveDuplicatesQuestion.removeDuplicates(duplicates);

        Assert.assertEquals(noDuplicates, Arrays.asList(5, 2, 4, 6, 7, 99, 11));
    }

    @Test
    public void testRemoveStringDuplicates() {
        final List<String> duplicates = Arrays.asList("one", "fish", "two", "fish", "red", "fish", "blue", "fish");
        final List<String> noDuplicates = RemoveDuplicatesQuestion.removeDuplicates(duplicates);

        Assert.assertEquals(noDuplicates, Arrays.asList("one", "fish", "two", "red", "blue"));
    }

    @Test
    public void testRemoveArbitraryObjects() {
        final List<TestObject> duplicates = Arrays.asList(
                new TestObject("fish", "fish"),
                new TestObject("red", "blue"),
                new TestObject("fish", "fish"),
                new TestObject("red", "blue")
        );
        final List<TestObject> noDuplicates = RemoveDuplicatesQuestion.removeDuplicates(duplicates);

        Assert.assertEquals(noDuplicates, Arrays.asList(new TestObject("fish", "fish"), new TestObject("red", "blue")));
    }
}
