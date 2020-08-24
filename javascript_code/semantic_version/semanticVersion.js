
module.exports = SemanticVersioning();

function SemanticVersioning() {
  return {
    getGreaterVersion: getGreaterVersion
  };

  /*
    A normal version number MUST take the form X.Y.Z where X, Y, Z
    Z are non-negative integers,
    MUST NOT contain leading zeroes. X is the major version,
    Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
   */
  function getGreaterVersion(firstVersion, secondVersion) {
    firstVersionList = firstVersion.split('.');
    secondVersionList = secondVersion.split('.');

    for (let i = 0; i <= firstVersionList.length - 1; ++i) {
      if (parseInt(firstVersionList[i]) > parseInt(secondVersionList[i])) {
        return firstVersion;
      } else if (parseInt(firstVersionList[i]) < parseInt(secondVersionList[i])) {
        return secondVersion;
      } else {
        continue;
      }
    }

    return '0.0.0';
  }

  function VersionMismatchException(message) {
    return {
      errorMessage: message
    };
  }
}