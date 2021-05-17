// Given a set of strings, removes startString from every string in the set
export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || startString === '') return '';

  return [...set]
    .filter((str) => str.startsWith(startString))
    .map((str) => str.replace(startString, ''))
    .join('-');
}
