const express = require('express')
const app = express()
const port = 3000

const moviesRoutes = require('./routes/movies');

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));
app.use(moviesRoutes)


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})