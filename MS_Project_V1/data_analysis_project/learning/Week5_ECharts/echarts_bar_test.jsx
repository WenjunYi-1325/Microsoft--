import * as echarts from "echarts"
import { useEffect } from "react" 

function App() {

  useEffect(() => {    


    const chartDom = document.getElementById("chart")


    const myChart = echarts.init(chartDom)

   
    const option = {   
      title: {
        text: "电影评分"
      },

      xAxis: {
        type: "category",
        data: ["肖申克的救赎", "霸王别姬", "阿甘正传", "泰坦尼克号", "这个杀手不太冷"]
      },

      yAxis: {
        type: "value"
      },

      series: [
        {
          type: "bar",
          data: [9.7, 9.6, 9.5, 9.5, 9.4]
        }
      ]
    }

    myChart.setOption(option) 
    
  }, [])


  return (
    <div>

      <h1>豆瓣电影数据分析</h1>

      <div
        id="chart"
        style={{
          width: "800px",
          height: "500px"
        }}
      ></div>

    </div>
  )
}

export default App