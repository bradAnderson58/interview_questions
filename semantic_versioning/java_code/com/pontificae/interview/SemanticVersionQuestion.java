package com.pontificae.interview;


import java.util.ArrayList;
import java.util.Arrays;

/**
 * A normal version number MUST take the form X.Y.Z where X, Y, Z
 * Z are non-negative integers,
 * MUST NOT contain leading zeroes. X is the major version,
 * Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
 */


public class SemanticVersionQuestion {


    public static String getGreaterVersion(String firstVersion, String secondVersion) {
        ArrayList<String> firstVersionList = new ArrayList<>(Arrays.asList(firstVersion.split("\\.")));
        ArrayList<String> secondVersionList = new ArrayList<>(Arrays.asList(secondVersion.split("\\.")));

        for (int i=0; i <= firstVersionList.size()-1; i++) {
            if (Integer.parseInt(firstVersionList.get(i)) > Integer.parseInt(secondVersionList.get(i))) {
                return firstVersion;
            } else if (Integer.parseInt(firstVersionList.get(i)) < Integer.parseInt(secondVersionList.get(i))) {
                return secondVersion;
            } else {
                continue;
            }
        }
        return "0.0.0";
    }


    public static class VersionMismatchException extends RuntimeException {

    }
}