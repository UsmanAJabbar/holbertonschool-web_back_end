const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  // Pull data from CSV file
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) reject(Error('Cannot load the database'));
    else {
      const fileData = data
        .split('\n')
        .map((student) => student.split(','))
        .slice(1)
        .reduce((total, currentVal) => {
          const eslint = total;
          const subj = currentVal[currentVal.length - 1];
          const firstName = currentVal[0];

          if (typeof eslint[subj] === 'undefined') eslint[subj] = [firstName];
          else eslint[subj].push(firstName);

          return eslint;
        }, {});

      // Prepare Print Statements
      let totalStudents = 0;
      let output = '';

      for (const field in fileData) {
        if (fileData.hasOwnProperty) {
          totalStudents += fileData[field].length;
          output += `Number of students in ${field}: ${fileData[field].length}. List: ${fileData[field].join(', ')}\n`;
        }
      }

      // Print necessary print statements
      output = (`Number of students: ${totalStudents}\n${output}`).slice(0, -1);
      console.log(output);
      resolve(output);
    }
  });
});

module.exports = countStudents;
