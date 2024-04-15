#!/usr/bin/node
const logMe = (item) => {
  if (typeof logMe.count === 'undefined') {
    logMe.count = 0;
  }
  console.log(`${logMe.count}: ${item}`);
  logMe.count++;
};

module.exports.logMe = logMe;
