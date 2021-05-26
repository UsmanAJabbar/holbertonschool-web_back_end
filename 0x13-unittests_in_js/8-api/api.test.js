const { expect } = require('chai');
const request = require('request');

describe('index page test', () => {

  it('Returns the right content', function (done) {
    request('http://localhost:7865', function (error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

});
