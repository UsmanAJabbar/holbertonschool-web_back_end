const { expect } = require('chai');
const ping = require('./request');

describe('index page test', () => {
  it('test API root endpoint with /', async () => {
    await new Promise((done) => {
      ping('http://localhost:7865')
        .then((data) => expect(data === 'Welcome to the payment system').to.be.true);
      done();
    });
  });

  it('test API root endpoint w/o /', async () => {
    await new Promise((done) => {
      ping('http://localhost:7865')
        .then((data) => expect(data === 'Welcome to the payment system').to.be.true);
      done();
    });
  });

  it('test unknown endpoint', async () => {
    await new Promise((done) => {
      ping('http://localhost:7865/end')
        .catch((err) => expect(err).contains('Cannot GET /end'));
      done();
    });
  });
});
