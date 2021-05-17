// Returns whether a value is in a set or not
export default function hasValuesFromArray(set, array) {
  return array.every((e) => set.has(e));
}
