
GRAVATAR_URL = "http://www.gravatar.com/avatar/"

function generateGravatarUrl(email) {

	var hash = require('crypto').createHash('md5').update(email).digest("hex");
	console.log(hash);
	return GRAVATAR_URL+hash;

};


console.log(generateGravatarUrl("yodebu@gmail.com"));