function chart_3(){
    var myChart = echarts.init(document.getElementById('tree_chart'));
    option = {
      tooltip: {
        show:true,
      },
      series: [
        {
          type: 'treemap',
          roam:false,
          nodeClick:false,
          breadcrumb:false,
          left:10,
          right:10,
          top:10,
          bottom:40,
          label:{
            fontSize:8
          },
          data: all_data
        }
      ]
    };

    myChart.setOption(option)
}