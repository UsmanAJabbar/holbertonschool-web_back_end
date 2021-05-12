// Class HolbertonCourse
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Name getter/setter method
  set name(newName) {
    if (typeof newName !== 'string') { throw TypeError('Name must be a string'); }
    this._name = newName;
  }

  get name() {
    return this._name;
  }

  // Length getter/setter method
  set length(newLength) {
    if (typeof newLength !== 'number') { throw TypeError('Length must be a number'); }
    this._length = newLength;
  }

  get length() {
    return this._length;
  }

  // Students getter/setter method
  set students(arrOfStudents) {
    if (typeof arrOfStudents !== 'object') { throw TypeError('Student array must be an array'); }
    for (const student in arrOfStudents) {
      if (typeof student !== 'string') { throw TypeError('Students must only contain arrays'); }
    }
    this._students = arrOfStudents;
  }

  get student() {
    return this._students;
  }
}
