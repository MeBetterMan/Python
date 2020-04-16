$(document).ready(function(){
    $("#btn").bind("click", function(){
        $.ajax(
         {
            type:"get",
            url:"/studentsinfo/",
            dataType:"json",
            success:function(data, status){
                console.log(data)
                var d = data["data"]
                for(i=1;i < d.length; i++){
                    document.write("<h1>"+ d[i][0] +"</h1>")
                }
            }
         }
        )
    })
})