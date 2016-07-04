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

<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
				<!-- Identify your business so that you can collect the payments. -->
				<input type="hidden" name="business" value="jake@jakessnakes.com">

				<!-- Specify a PayPal Shopping Cart Add to Cart button. -->
				<input type="hidden" name="cmd" value="_cart">
				<input type="hidden" name="add" value="1">

				<!-- Specify details about the item that buyers will purchase. -->
				<input type="hidden" name="item_name" value="{{snake.title}}">
				<input type="hidden" name="amount" value="{{snake.price}}">
				<input type="hidden" name="currency_code" value="USD">

				<!-- Display the payment button. -->
				<input type="image" name="submit" border="0" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif" alt="PayPal - The safer, easier way to pay online">
				<img alt="" border="0" width="1" height="1" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" >
			</form>	