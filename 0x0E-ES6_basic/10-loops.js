/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  const appendedArray = []
  for (const string of array) {
    appendedArray.push(`${appendString}${string}`);
  }

  return appendedArray;
}
