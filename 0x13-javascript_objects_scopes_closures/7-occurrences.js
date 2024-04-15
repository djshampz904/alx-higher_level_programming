#!/usr/bin/node
const nbOccurences = (list, searchElement) => {
  return list.filter(element => element === searchElement).length;
};

module.exports.nbOccurences = nbOccurences;
