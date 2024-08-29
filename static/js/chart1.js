function chart_1(){
		var myChart = echarts.init(document.getElementById('map_chart'));
		var mapName = 'china'
		var geoCoordMap = {};
		/*获取地图数据*/
		myChart.showLoading();
		var mapFeatures = echarts.getMap(mapName).geoJson.features;
		myChart.hideLoading();
		mapFeatures.forEach(function(v) {
		    // 地区名称
		    var name = v.properties.name;
		    // 地区经纬度
		    geoCoordMap[name] = v.properties.cp;

		});

		var convertData = function(data) {
		    var res = [];
		    for (var i = 0; i < data.length; i++) {
		        var geoCoord = geoCoordMap[data[i].name];
		        if (geoCoord) {
		            res.push({
		                name: data[i].name,
		                value: geoCoord.concat(data[i].value),
		            });
		        }
		    }
		    return res;
		};
		option = {
            tooltip: {
                padding: 0,
                enterable: true,
                transitionDuration: 1,
                textStyle: {
                    color: '#000',
                    decoration: 'none',
                },
                formatter: function(params) {
                        var tipHtml = '';
                        tipHtml = '<div style="width:180px;height:120px;background:rgba(22,80,158,0.8);border:1px solid rgba(7,166,255,0.7)">'
                        +'<div style="width:90%;height:30px;line-height:30px;border-bottom:2px solid rgba(7,166,255,0.7);padding:0 10px">'+'<i style="display:inline-block;width:8px;height:8px;background:#16d6ff;border-radius:30px;">'+'</i>'
                        +'<span style="margin-left:10px;color:#fff;font-size:16px;">'+params.name+'</span>'+'</div>'
                        +'<div style="padding:10px">'
                        +'<p style="color:#fff;font-size:12px;">'+'<i style="display:inline-block;width:10px;height:10px;background:#16d6ff;border-radius:40px;margin:0 8px">'+'</i>'
                        +'总房源：'+'<span style="color:#11ee7d;margin:0 6px;">'+all_map_data[params.dataIndex].value+'</span>'+'</p>'
                        +'<p style="color:#fff;font-size:12px;">'+'<i style="display:inline-block;width:10px;height:10px;background:#16d6ff;border-radius:40px;margin:0 8px">'+'</i>'
                        +'二手房：'+'<span style="color:#f48225;margin:0 6px;">'+second_map_data[params.dataIndex].value+'</span>'+'</p>'
                        +'</div>'+'</div>';
                        return tipHtml;
                    }

            },
            visualMap: {
                show: true,
                min: 20000,
                max: 900000,
                left: '10%',
                bottom:'10%',
                calculable: true,
                seriesIndex: [0],
                textStyle:{
                    color:'white',
                 },
                inRange: {
                    color: ['#9ACCFF', '#0091FE', '#0080FF', '#1751B2', '#013998'],
                }
	        },
		    geo: {
		        show: true,
		        map: mapName,
                label: {
                   normal: {
                       show:true,
                       fontSize:10,
                       color:'white'
                   },
                   //鼠标移入后查看效果
                   emphasis: {
                       textStyle: {
                           color: 'orange'
                       }
                   }
                },
		        roam: false,
		        itemStyle: {
		            normal: {
		                areaColor: '#023677',
		                borderColor: '#1180c7',
		            },
		            emphasis: {
		                areaColor: 'orange',
		            }
		        }
		    },
		    series: [
				{
					type: 'map',
					map: mapName,
					geoIndex: 0,
					animation: false,
					data: all_map_data
				},
				{
					name: '点',
					type: 'scatter',
					coordinateSystem: 'geo',
					zlevel: 6,
				},
		        {
		            name: '散点',
		            type: 'effectScatter',
		            animation: false,
		            coordinateSystem: 'geo',
		            data: convertData(second_map_data),
		            symbolSize: function(val) {
		                return val[2]/20000 ;
		            },
		            showEffectOn: 'render',
		            rippleEffect: { //涟漪特效
						period: 4, //动画时间，值越小速度越快
						brushType: 'stroke', //波纹绘制方式 stroke, fill
						scale: 4 //波纹圆环最大限制，值越大波纹越大
					},
		            hoverAnimation: true,
		            label: {
		                normal: {
		                    formatter: '{b}',
		                    position: 'left',
		                    show: false
		                }
		            },
		            itemStyle: {
		                normal: {
		                    color: 'yellow',
		                    shadowBlur: 10,
		                    shadowColor: 'yellow'
		                }
		            },
		            zlevel: 1
		        },

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
		}, 2000);
    myChart.on("click", function (params) {
       if (params.name == "山东") {
           location.href='/shandong/';
       }
   });
}