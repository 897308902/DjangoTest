$(function(){
	
	var timer=null;
	var num=0;
	
	//顶部导航
	headers(2);
	
	//分页pages
	$(".pages a").eq(1).click(function(){
		getnews("./public/news2.html",function(data){
			$(".newsbox").html(data);
		});
	}).end()
	.eq(2).click(function(){
		getnews("./public/news3.html",function(data){
			$(".newsbox").html(data);
		});
	});
	
	function getnews(urls,fn){
		$.ajax({
			type:"get",
			url:urls,
			async:true,
			success:function(data){
				fn(data);
			}
			
		});
	}
	
});