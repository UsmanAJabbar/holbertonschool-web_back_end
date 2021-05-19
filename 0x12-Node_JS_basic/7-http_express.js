const app = require('express')();

app.listen(1245);

const countStudents = require('./3-read_file_async');

const pathToCSVFile = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(pathToCSVFile)
    .then((success) => res.send(success));
});

module.exports = app;
