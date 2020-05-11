"""
 A normal version number
 MUST take the form X.Y.Z where X, Y, Z are non-negative integers
 MUST NOT contain leading zeroes.  X is the major version,
 Each element MUST increase numerically.  For instance 1.9.0 -> 1.10.0 -> 1.11.0
"""


class SemanticVersionQuestion:

    @staticmethod
    def get_greater_version(first_version: str, second_version: str) -> str:
        first_version_list = first_version.split('.')
        second_version_list = second_version.split('.')
        for first, second in zip(first_version_list, second_version_list):
            if first > second:
                return first_version
            elif first < second:
                return second_version
            else:
                continue
        return '0.0.0'


class SemanticVersionException(Exception):
    pass
