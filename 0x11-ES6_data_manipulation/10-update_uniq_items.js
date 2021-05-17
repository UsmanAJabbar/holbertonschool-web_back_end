// Updates items whose qty == 1 to 100
export default function updateUniqueItems(someMap) {
  if (someMap instanceof Map) {
    return [...someMap.entries()]
      .filter((keyValArr) => keyValArr[1] === 1)
      .map((keyValArr) => someMap.set(keyValArr[0], 100));
  }
  return Map();
}
