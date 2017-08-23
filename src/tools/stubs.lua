-- functions used in map save files
-- reqired to be able to parse the lua files

function BOOLEAN(arg) return arg end
function FLOAT(arg) return arg end
function GROUP(arg) return arg end
function RECTANGLE(arg) return arg end
function STRING(arg) return arg end
function VECTOR3(x, y, z) return {x, z, y} end
