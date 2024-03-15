const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World, this was executed by express')
})

app.listen(3000)