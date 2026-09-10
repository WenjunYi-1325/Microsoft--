import { useState } from "react"

function App() {

  // 第一个输入框
  const [param, setParam] = useState("")

  // 第二个输入框
  const [body, setBody] = useState("")

  // 第三个输入框
  const [age, setAge] = useState("")

  // Flask 返回的结果
  const [result, setResult] = useState("")


  const handleClick = () => {

    fetch(
      "http://127.0.0.1:5000/test2?param=" + param + "&age=" + age,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          body: body
        })
      }
    )
      .then(response => response.text())
      .then(data => {
        setResult(data)
      })
  }


  return (
    <div>

      <h1>React + Flask 参数测试</h1>


      <div>
        <input
          type="text"
          placeholder="请输入 param"
          value={param}
          onChange={(e) => setParam(e.target.value)}
        />
      </div>


      <div>
        <input
          type="text"
          placeholder="请输入 body"
          value={body}
          onChange={(e) => setBody(e.target.value)}
        />
      </div>


      <div>
        <input
          type="text"
          placeholder="请输入 age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </div>


      <button onClick={handleClick}>
        发送
      </button>


      <p>{result}</p>

    </div>
  )
}

export default App