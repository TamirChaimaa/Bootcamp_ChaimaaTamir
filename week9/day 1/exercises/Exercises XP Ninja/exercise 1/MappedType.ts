type MappedType = number | string;

function mapType(value: MappedType): number {
  if (typeof value === "number") {
    return value * value;
  } else {
    return value.length;
  }
}

console.log(mapType(4));         
console.log(mapType("hello"));   
