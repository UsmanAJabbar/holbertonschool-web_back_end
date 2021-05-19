const http = require('http');
const countStudents = require('./3-read_file_async');

const pathToCSVFile = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Endpoints
  if (req.url === '/students') {
    countStudents(pathToCSVFile)
      .then((success) => res.end(success));
  } else {
    res.end('Hello Holberton School!');
  }
}).listen(1245);

module.exports = app;
