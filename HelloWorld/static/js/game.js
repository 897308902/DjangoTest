$(function(){
	
	var timer=null;
	var num=0;
	
	//顶部导航
	headers(1);
	
	$(".gnav li").on("click",function(){
		//给当前li标签的孩子加class，同时要给相邻li的孩子a去掉class
		$(this).children("a").addClass("current").end().siblings("li").children("a").removeClass("current");
	});
});