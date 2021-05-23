const app = require('express')();

app.listen(1245);

const countStudents = require('./3-read_file_async');

const pathToCSVFile = process.argv[2];

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(pathToCSVFile)
    .then((success) => {
      const out = `This is the list of our students\n${success}`;
      res.status(200).send(out);
    });
});

module.exports = app;
