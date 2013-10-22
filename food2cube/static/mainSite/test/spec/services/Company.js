'use strict';

describe('Service: Company', function () {

  // load the service's module
  beforeEach(module('food2cubeApp'));

  // instantiate service
  var Company;
  beforeEach(inject(function (_Company_) {
    Company = _Company_;
  }));

  it('should do something', function () {
    expect(!!Company).toBe(true);
  });

});
