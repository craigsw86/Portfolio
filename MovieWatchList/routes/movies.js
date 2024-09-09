const express = require('express')
const router = express.Router()

// define the home page route
router.get('/', (req, res) => {
  res.render('index')
})

// define the about route
router.get('/about', (req, res) => {
  res.send('About my list of movies')
})

// Creating
router.post('/movies/create', (req, res) => {
    res.send('Add more movies here!')
    console.log(req.body.title)
})

// Updating
router.get('/movies/update', (req, res) => {
    res.send('Update your movies here!')
})

// Deleting
router.get('/movies/delete', (req, res) => {
    res.send('Delete your movies here!')
})

module.exports = router