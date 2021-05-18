// Returns the ids found in an arrayOfObjects
export default function getListStudentIds(arrayOfObjects) {
  const arr = [];
  if (Array.isArray(arrayOfObjects)) {
    return arrayOfObjects.map((item) => item.id);
  }
  return arr;
}
