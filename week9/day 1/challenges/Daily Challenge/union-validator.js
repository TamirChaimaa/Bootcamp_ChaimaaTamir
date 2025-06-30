function validateUnionType(value, allowedTypes) {
    var valueType = typeof value;
    for (var i = 0; i < allowedTypes.length; i++) {
        if (valueType === allowedTypes[i]) {
            return true; // If type matches any allowed type, return true
        }
    }
    return false;
}
console.log(validateUnionType(25, ["number", "string"]));
console.log(validateUnionType("hello", ["number", "string"]));
console.log(validateUnionType(false, ["number", "string"]));
console.log(validateUnionType({}, ["object"]));
console.log(validateUnionType(undefined, ["string", "boolean"]));
