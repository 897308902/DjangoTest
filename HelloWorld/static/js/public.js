//自动加载头部
function headers(n) {
	$.ajax({
		url: "../static/public/header.html",
		type: "get",
		async: true,
		success: function(data) {

			$(".tops").html(data);

			//给对应的li分配高亮
			$(".tops .nav>li").eq(n).addClass("current").siblings("li").removeClass("current");
		}
	});
}

//自动加载尾部
$.ajax({
	url: "../static/public/footer.html",
	type: "get",
	async: true,
	success: function(data) {
		$(".a_footer").html(data);
	}
});

//返回顶部
$(window).scroll(function() {
	if($(window).scrollTop() > 0) {
		$(".toTop").css("display", "block");
	} else {
		$(".toTop").css("display", "none");
	}
});