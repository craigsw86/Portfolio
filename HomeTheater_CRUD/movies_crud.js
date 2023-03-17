var app = new function() {
    // Code
}

this.el = document.getElementById('movies');

this.movies = ['Fail Safe', 'Dersu Uzala', 'Madadayo', 'American History X', 'Accepted', 'Bonjour Monsieur Shlomi', 'Aviva, My Love', 'The Wooden Gun', 'Campfire', 'Off White Lies', 'Operation Grandma', 'The War of the Rose', '1945', 'Z', 'The Confession', 'Parasite', 'The Host', 'Save the Green Planet!', 'The Bad Sleep Well', 'Stray Dog'];

this.Count = function(data) {
    var el = document.getElementById('counter');
    var name = 'movie';

    if (data) {
        if (data > 1) {
            name = 'movies';
        }
        el.innerHTML = data + ' ' + name;
    } else {
        el.innerHTML = 'No ' + name;
    }
}

this.FetchAll = function() {
    var data = '';

    if (this.movies.length > 0) {
        for (i = 0; i < this.movies.length; i++) {
            data += '<tr>';
            data += '<td>' + this.movies[i] + '</td>';
            data += '</tr>';
        }
    }
    this.Count(this.movies.length);
    return this.el.innerHTML = data;
}

app.FetchAll();

this.Add = function() {
    alert('add something');
}