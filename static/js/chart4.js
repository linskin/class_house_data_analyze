function chart_4(){
    var myChart = echarts.init(document.getElementById('year_chart'));
    option = {
        grid: {
            show:false,
            top:"10%",
            left: "5%",
            bottom:"20%",
            right: "5%",
            containLabel: true,
        },
        tooltip:{
            show:true,
            trigger:'axis',
            formatter:function(params) {
                return '<span style="color:#E78932;">'+params[0].value + '</span><br/>';           　　
            },
            axisPointer:{
                type:'line',
                label:{
                    show:true,
                    fontSize:8,
                },
                lineStyle: {
                    color:'#2094CA',
                    type:'dotted',
                },
            },
            textStyle:{
                fontSize:10,
            },
        },
        xAxis :{
               type : 'category',
               boundaryGap : false,
               axisLabel:{
                   fontSize:10,
                   color:'#2094CA',
               },
               axisLine: {
                   show:true,
                   lineStyle: {
                       color: '#1C7DEE'
                },
            },
               data : year_data.year,
           },
        yAxis :{
                splitLine:{
                    show: false
                },
                type : 'value',
                axisLabel:{
                    fontSize:10,
                    color:'#2094CA',
                },
                axisLine: {
                    show:true,
                    lineStyle: {
                        color: '#1C7DEE'
	                }
	            },
            },
        series : [{
                type:'line',
                symbol:'circle',
                symbolSize:10,
                itemStyle:{
                    normal:{
                        color:'#0099FF',
                    },
                },
                lineStyle:{
                    color:'#0099FF',
                    width:2,
                },
                areaStyle: {
                    color:{
                        type: 'linear',
                        x: 0,
                        y: 0,
                        x2: 0,
                        y2: 1,
                        colorStops: [{
                            offset: 0, color: '#0099FF' // 0% 处的颜色
                        }, {
                            offset: 1, color: '#394E7F' // 100% 处的颜色
                        }],
                        global: false // 缺省为 false
                    },
                    opacity:0.3,
                },
                data:year_data.house_count,
                showAllSymbol:true,
            }]
        };

    myChart.setOption(option)
   var currentIndex = -1;
   setInterval(function () {
       var dataLen = option.series[0].data.length;
       // 取消之前高亮的图形
       myChart.dispatchAction({
           type: 'downplay',
           seriesIndex: 0,
           dataIndex: currentIndex
       });
       currentIndex = (currentIndex + 1) % dataLen;
       // 高亮当前图形
       myChart.dispatchAction({
           type: 'highlight',
           seriesIndex: 0,
           dataIndex: currentIndex
       });
       // 显示 tooltip
       myChart.dispatchAction({
           type: 'showTip',
           seriesIndex: 0,
           dataIndex: currentIndex
       });
   }, 2000);
}