$(function(){
	
	var timer=null;
	var num=0;
	
	//顶部导航
	headers(0);
	
	//banner图相关的
	var ol=$("<ol></ol>");
	//先遍历一次给所有li添加背景图片
	$(".topBanner>ul>li").each(function(i,e){
		$(e).children("a").css("background",'url(../static/img/index/b_'+(i+1)+'.jpg) no-repeat center center');
		ol.append($("<li></li>"));
	});
	$(".topBanner").append(ol);
	
	
	//自动轮播
	timer=setInterval(bannertimer,2000);
	//鼠标停留在图片上时,暂停播放
	$(".topBanner>ul>li").on("mouseenter",function(){
		clearInterval(timer);
	})
	.on("mouseleave",function(){
		clearInterval(timer);
		timer=setInterval(bannertimer,2000);
	});
	
	//默认选中第一个ol li
	$(".topBanner>ol>li").eq(0).addClass("current");
	$(".bannerList li").eq(0).fadeIn(1).siblings().fadeOut(1);
	
	//BUG=============================================
	//第一次点击的时候变化得太快了
	//页面有滚动时,点他会跳
	
	
	//点击切换图片
	$(".topBanner>ol>li").on("click",function(){
		$(this).addClass("current").siblings("li").removeClass("current");
		$(".topBanner>ul>li").eq($(this).index()).fadeIn().siblings().fadeOut();
	})
	
	
	//四个图片
	//鼠标经过时,背景颜色有个动画
	$(".indexmain .bd ul>li").on("mouseenter",function(){

		$(".indexmain .bd ul>li").eq($(this).index()).stop().animate({"background-color":"#38b774"},1000)
		.css("color","#FFFFFF");
		
	}).on("mouseleave",function(){
		$(".indexmain .bd ul>li").eq($(this).index()).stop().animate({"background-color":"#ffffff"},10)
		.css("color","#444866");
		
	});
	
	//下的小圆点
	$(".hd>ul>li").eq(0).addClass("current");
	//点击第一个圆点让ul回到原点
	$(".hd>ul>li").eq(0).on("click",function(){
		$(this).addClass("current").siblings("li").removeClass("current");
		$(".bd>ul").animate({"left":0},500);
		
	});
	//点击第二个让ul左移他自己的宽度,再加上一个margin-right的值
	$(".hd>ul>li").eq(1).on("click",function(){
		$(this).addClass("current").siblings("li").removeClass("current");
		$(".bd>ul").animate({"left":"-1043px"},500);
	});
	
	
	
	
	
	function bannertimer(){
		num++;
		if(num>($(".topBanner>ul>li").length-1)){
			num=0;
		}
		$(".bannerList li").eq(num).fadeIn().siblings().fadeOut();
		$(".topBanner>ol>li").eq(num).addClass("current").siblings("li").removeClass("current");
	}
});


