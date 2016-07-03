function hash(s) {
	var hash = 7;
	var letters = "acdfgilmnoprstuw";
	for(var i = 0; i < s.length; i++) {
		hash = (hash * 23 + letters.indexOf(s[i]));
	}
	return hash;
}

function unhash(int) {
	var hash = 7;
	var letters = "acdfgilmnoprstuw";
	for(var i = int.length; i > 0; i--) {
		hash = (hash / 23 - letters.indexOf(s[i]));
	}
	return hash;
}

console.log(hash('tortilla'));
console.log(unhash(593846452632))

