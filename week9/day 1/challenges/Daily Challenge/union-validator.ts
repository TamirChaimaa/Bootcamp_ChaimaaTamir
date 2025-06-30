function validateUnionType(value: any, allowedTypes: string[]): boolean {
    const valueType = typeof value;

    for (let i = 0; i < allowedTypes.length; i++) {
        if (valueType === allowedTypes[i]) {
            return true;
        }
    }

    return false;
}

console.log(validateUnionType(25, ["number", "string"]));    
console.log(validateUnionType("hello", ["number", "string"])); 
console.log(validateUnionType(false, ["number", "string"]));    
console.log(validateUnionType({}, ["object"]));                  
console.log(validateUnionType(undefined, ["string", "boolean"]));