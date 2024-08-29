function chart_5(){
    var myChart = echarts.init(document.getElementById('word_chart'));
    const colorList = ['#f89b6299', '#afcf7cde', '#fece5b','blue','green']
    var option = {
    tooltip: {
        show:true
    },
        series: [{
            type: 'wordCloud',
            gridSize: 6,//字符间距
            sizeRange: [10, 40],  //字体大小
            shape: 'circle', //形状
            drawOutOfBound: true,
            top:0,
            textStyle: {
                color: function() {
                  let index = Math.floor(Math.random() * colorList.length)
                  return colorList[index]
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: word_data
        }]
    };
    myChart.setOption(option);
}