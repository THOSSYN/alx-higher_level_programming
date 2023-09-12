#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} if (process.argv.length === 3) {
  console.log(0);
}else {
  let max = process.argv[2];
  let max2;
  for (let i = 2; i < process.argv.length; i++) {
      const convArg_I = parseInt(process.argv[i]);
      if (!isNaN(convArg_I) && convArg_I > max) {
	max2 = max;
        max = convArg_I;
      } else if (convArg_I > max2 && convArg_I < max) {
        max2 = convArg_I;
      }
  }
  console.log(max2);
}
