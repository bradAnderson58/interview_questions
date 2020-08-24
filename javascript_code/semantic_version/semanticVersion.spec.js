const assert = require('assert');
const semanticVersion = require('./semanticVersion');

describe('Checking Semantic Versions', () => {

  it('should return the higher version', () => {
    const arg1 = '1.1.0';
    const arg2 = '1.2.0';

    assert.equal(arg2, semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should return either when they are equal', () => {
    const arg1 = '1.2.0';
    const arg2 = '1.2.0';

    assert.equal(arg1, semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject alphanumerics', () => {
    const arg1 = '1.a.0';
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject empty strings', () => {
    const arg1 = '';
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject null values', () => {
    const arg1 = null;
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject invalid semantic version format 1', () => {
    const arg1 = '1.2.3.4.5.6';
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject invalid semantic version format 2', () => {
    const arg1 = '1..6';
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });

  it('should reject invalid semantic version format 3', () => {
    const arg1 = '1.6';
    const arg2 = '1.2.0';

    assert.throws(() => semanticVersion.getGreaterVersion(arg1, arg2));
  });
});