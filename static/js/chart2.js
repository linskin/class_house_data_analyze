function chart_2(){
    var myChart = echarts.init(document.getElementById('house_mean'));
    option = {
        grid:{
            bottom:'20%',
            top:'5%',
            left:'10%',
            right:'5%'
        },
        tooltip: {
            show:true,
            trigger: 'axis',
            textStyle:{
                fontSize:10,
                color:'#2094CA',
            },
            axisPointer: {
                type:'none',
                label:{
                    show:true,
                    fontSize:10,
                },
            }
        },
	    xAxis: {
	        data: price_mean[0],
	        axisLine: {
	            lineStyle: {
	                color: '#1C7DEE'
	            }
	        },
	        axisLabel:{
	        	fontSize:8,
	        },
	    },
      yAxis: {
        type: 'value',
        splitLine: {
            show: false
        },
        axisLine: {
            show:true,
            lineStyle: {
                color: '#1C7DEE'
            }
        },
        axisLabel:{
            fontSize:8,
        },
      },
      series: [
        {
            name:'平均房价',
            type: 'bar',
            barWidth: 10,
            itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1,[
                        {offset: 0, color: '#D98234'},
                        {offset: 1, color: '#33313C'}
                    ]),
                opacity:0.5,
                borderColor:'#D98234',
                borderWidth:0.5,
            },
            emphasis:{
	        	itemStyle:{
	        		color:'#E78932',
	        		borderColor:'#1C7DEE',
	        		opacity:1,
	        	},
	        	label:{
	        		position:'top'
	        	}
	        },
	        data: price_mean[1],
        }
      ]
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
    }, 1000);
}