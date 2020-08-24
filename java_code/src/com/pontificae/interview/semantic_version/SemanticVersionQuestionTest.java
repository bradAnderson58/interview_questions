package com.pontificae.interview.semantic_version;

import org.junit.Assert;
import org.junit.Test;

public class SemanticVersionQuestionTest {

    @Test
    public void test1(){
        String arg1 = "1.1.0";
        String arg2 = "1.2.0";
        Assert.assertEquals(arg2, SemanticVersionQuestion.getGreaterVersion(arg1,arg2));
    }

    @Test
    public void test2(){
        String arg1 = "1.2.0";
        String arg2 = "1.2.0";
        Assert.assertEquals(arg1,SemanticVersionQuestion.getGreaterVersion(arg1,arg2));
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test3(){
        String arg1 = "1.a.0";
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test4(){
        String arg1 = "";
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test5(){
        String arg1 = null;
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test6(){
        String arg1 = "1.2.3.4.5.6";
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test7(){
        String arg1 = "1..6";
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }

    @Test(expected = SemanticVersionQuestion.VersionMismatchException.class)
    public void test8(){
        String arg1 = "1.6";
        String arg2 = "1.2.0";
        SemanticVersionQuestion.getGreaterVersion(arg1,arg2);
    }


}
