$(document).ready(function () {
	var url=window.location.pathname;
	
	$(".nav_list").removeClass('hover');

	if (url=="/" || url=="/index/") {
		$(".nav_index").addClass('hover');
	};
	if (url=="/classes/") {
		$(".nav_jsUl").show();
		// $(".nav_classes").addClass('hover');

	};
	if (url=="/discuss/") {
		$(".nav_discuss").addClass('hover');
	};
	if (url=="/activity/") {
		$(".nav_activity").addClass('hover');
	};
	if (url=="/test/") {
		$(".nav_test").addClass('hover');
	};
	if (url=="/download/") {
		$(".nav_download").addClass('hover');
	};

	if (url=="/user_login/") {
		$(".navBar").hide();
	};
	


	$(".jsMore").hover(
		function(){
			clearTimeout(this.timer),
			$(this).find(".jsUl").show()
		},
		function(){
			var e=this;
			this.timer=setTimeout(
				function(){
					$(e).find(".jsUl").hide()},100)
		});

	// $(".nav_list").hover(
	// 	function(){
	// 		clearTimeout(this.timer),
	// 		$(".nav_jsUl").show()
	// 	},
	// 	function(){
	// 		var e=$(".nav_jsUl");
	// 		this.timer=setTimeout(
	// 			function(){
	// 				$(e).hide()},100)
	// 	});


$(".tag_a").hover(
	function(){
		var i=Math.floor(Math.random()*7+1);
		var colors=new Array("#FF0000","#FF7F00","#FFFF00","#00FF00","#00FFFF","#0000FF","#8B00FF");
		var color_choose=colors[i];
		$(this).css("background-color",color_choose);
	},
	function(){
		$(this).css("background-color","#fff");
	}
	);





});




