jQuery('document').ready(function(){

	//adds array of objects
	var array = [
		{ name: 'Ivan', message: 'My name is Ivan', date: 1 },
		{ name: 'Petr', message: 'My name is Petr', date: 2 },
		{ name: 'Sergey', message: 'My name is Sergey', date: 3 },
		{ name: 'Aleksey', message: 'My name is Aleksey', date: 4 },
		{ name: 'Dmitriy', message: 'My name is Dmitriy', date: 5 },
	];

	//posts bust
	for ( var i=0; i < array.length; i++ ) {
		var a = '<div class="del">' + array[i].name + ": " + array[i].message + '</div>'
		jQuery('body').append(a);
	};

	//remove default array
	/*jQuery( init );

	function init() {
		jQuery('.del').empty();
	}*/

	//adds sort array
	/*alert(array.sort(function(obj1, obj2) {
		return obj2.date-obj1.date})
);*/


	//output sort array depending on conditions


});

