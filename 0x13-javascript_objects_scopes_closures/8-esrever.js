#!/usr/bin/node
const esrever = function (list) {
  return list.map((element, index) => list[list.length - 1 - index]);
};
module.exports.esrever = esrever;
