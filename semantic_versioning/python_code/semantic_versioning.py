
'''
 A normal version number
 MUST take the form X.Y.Z where X, Y, Z are non-negative integers
 MUST NOT contain leading zeroes.  X is the major version,
 Each element MUST increase numerically.  For instance 1.9.0 -> 1.10.0 -> 1.11.0
'''

class SemanticVersionQuestion:

    @staticmethod
    def get_greater_version(first_version: str, second_version: str) -> str:
        if first_version is None or second_version is None:
            raise SemanticVersionException('Invalid Format: Null value detected')

        first_version_list = first_version.split('.')
        second_version_list = second_version.split('.')

        if len(first_version_list) != 3 or len(second_version_list) != 3:
            raise SemanticVersionException('Invalid Format: Values must take the form X.Y.Z')

        empty = next(filter(lambda s: s is '', first_version_list + second_version_list), None)
        if empty is not None:
            raise SemanticVersionException('Invalid Format: Values must take the form X.Y.Z')

        non_numeric = next(filter(lambda s: invalid_value(s), first_version_list + second_version_list), None)
        if non_numeric is not None:
            raise SemanticVersionException('Invalid Format: Non-numeric values detected')

        for first, second in zip(first_version_list, second_version_list):
            if first > second:
                return first_version
            elif first < second:
                return second_version
            else:
                continue
        return first_version


class SemanticVersionException(Exception):
    def __init__(self, message: str):
        self.message = message


def invalid_value(s: str) -> bool:
    return not s.isdigit()
