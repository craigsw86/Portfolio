const express = require('express')
const app = express()
const port = 3000

const moviesRoutes = require('./routes/movies');

app.set('view engine', 'pug');

app.use(moviesRoutes)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})