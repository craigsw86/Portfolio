let facts = [
'I\'ve loved art ever since I was a kid and I once wanted to be an artist.',
'The most recent country I\'ve visited is Israel.',
'I want to visit lots of other countries, but I feel like I should visit Canada next because it\'s practically right next door.',
'My favorite color is blue.',
'I want to be a writer now.',
'My favorite food as a kid was pasta, but I\'m trying to move away from all the carbs now.',
'My favorite band has been Renaissance, the prog rock band from the 1970s.',
'My biggest fear is being forced to live a meaningless life.',
]

function newFact() {
let randomFact = Math.floor(Math.random() * (facts.length));
alert(facts[randomFact]);
}