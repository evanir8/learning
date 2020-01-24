#!/usr/bin/env node
const util = require('util');
let str = !process.argv[2] ? "Hello World Nodejs" : process.argv[2];
let starts = 0
let ends   = str.length;
while (true) {
  process.stdout.write(util.format('%s %s \r', str.substring(starts, ends), str.substring(0,starts)));
  starts =  starts > ends ? 0 : starts+1;
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 500); // msleep(500);
}

function msleep(n) {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
}
