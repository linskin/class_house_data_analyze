
var time_div=document.getElementById("currentTime");
start();
function start(){
    function get_time_str(){
        var time=new Date();
        var hour=time.getHours();
        var minute=time.getMinutes();
        var second=time.getSeconds();
        var year=time.getFullYear();
        var month=time.getMonth()+1;
        var day=time.getDate();
        var week=time.getDay();
        var weeks=["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
        hour=hour<10?'0'+hour:hour;
        minute=minute<10?'0'+minute:minute;
        second=second<10?'0'+second:second;
        day=day<10?'0'+day:day;
        var currentweek=weeks[week];
        return year+'年'+month+'月'+day+'日'+' '+currentweek+' '+hour+':'+minute+':'+second;
        }
    time_div.innerText=get_time_str();
}
setInterval(start,1000);
