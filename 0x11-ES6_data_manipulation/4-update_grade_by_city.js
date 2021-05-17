// Returns an array of students for a specific city with their new grade
/* eslint-disable */
export default function updateStudentGradeByCity(arrOfStudentObjs, city, newGrades) {
  if (Array.isArray(arrOfStudentObjs) && typeof city === 'string' && typeof newGrades === 'object') {
    const filtStudents = arrOfStudentObjs.filter((obj) => obj.location === city);

    filtStudents.forEach((studentObj) => {
      const objFound = newGrades.find((obj) => obj.studentId === studentObj.id);
      if (objFound) { studentObj.grade = objFound.grade; } else { studentObj.grade = 'N/A'; }
    });

    return filtStudents;
  }
  return [];
}
