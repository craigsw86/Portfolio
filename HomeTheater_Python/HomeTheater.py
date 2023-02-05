#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:00:21 2021

@author: craigsweinstein
"""

class Movie:
    def __init__(film, title, year, genre, director, language):
        film.title = title
        film.year = year
        film.genre = genre
        film.director = director
        film.language = language

movie01 = Movie("Fail Safe", 1964, "Thriller", "Sidney Lumet", "English");
movie02 = Movie("Dersu Uzala", 1975, "Historical", "Akira Kurosawa", "Russian");
movie03 = Movie ("Madadayo", 1993, "Drama", "Akira Kurosawa", "Japanese");
movie04 = Movie("American History X", 1998, "Drama", "Tony Kaye", "English");
movie05 = Movie("Accepted", 2006, "Comedy", "Steve Pink", "English");
movie06 = Movie("Bonjour Monsieur Shlomi", 2003, "Comedy", "Shemi Zarchin", "Hebrew");
movie07 = Movie("Aviva, My Love", 2006, "Drama", "Shemi Zarchin", "Hebrew");
movie08 = Movie("The Wooden Gun", 1979, "Drama", "Ilan Moshenson", "Hebrew");
movie09 = Movie("Campfire", 2004, "Drama", "Joseph Cedar", "Hebrew");
movie10 = Movie("Off White Lies", 2011, "Drama", "Maya Kenig", "Hebrew");
movie11 = Movie("Operation Grandma", 1999, "Comedy", "Dror Shaul", "Hebrew");
movie12 = Movie("The War of the Roses", 1989, "Comedy", "Danny DeVito", "English");
movie13 = Movie("1945", 2017, "Drama", "Ferenc Torok", "Hungarian");
movie14 = Movie("Z", 1969, "Drama", "Costa-Gavras", "French");
movie15 = Movie("The Confession", 1970, "Drama", "Costa-Gavras", "French");
movie16 = Movie("Parasite", 2019, "Comedy", "Bong Joon-ho", "Korean");
movie17 = Movie("The Host", 2006, "Monster", "Bong Joon-ho", "Korean");
movie18 = Movie("Save the Green Planet!", 2003, ["Science-Fiction", "Comedy"], "Jang Joon-hwan", "Korean");
movie19 = Movie("The Bad Sleep Well", 1960, "Mystery", "Akira Kurosawa", "Japanese");
movie20 = Movie("Stray Dog", 1949, "Drama", "Akira Kurosawa", "Japanese");
movie21 = Movie("Drunken Angel", 1948, "Drama", "Akira Kurosawa", "Japanese");
movie22 = Movie("Dodes'ka-den", 1970, "Drama", "Akira Kurosawa", "Japanese");
movie23 = Movie("Red Beard", 1965, "Drama", "Akira Kurosawa", "Japanese");
movie24 = Movie("Dora-heita", 2000, "Drama", "Kon Ichikawa", "Japanese");
movie25 = Movie("White Material", 2009, "Drama", "Claire Denis", "French");
movie26 = Movie("Danton", 1983, "Drama", "Andrzej Wajda", "French");
movie27 = Movie("Kuroneko", 1968, "Horror", "Kaneto Shindo", "Japanese");
movie28 = Movie("Onibaba", 1964, "Horror", "Kaneto Shindo", "Japanese");
movie29 = Movie("Harakiri", 1962, "Drama", "Masaki Kobayashi", "Japanese");
movie30 = Movie("Europa Europa", 1990, "Drama", "Agnieszka Holland", ["German", "Russian", "Polish", "Hebrew", "Yiddish"]);
movie31 = Movie("Phoenix", 2014, "Drama", "Christian Petzold", "German");
movie32 = Movie("Cold War", 2018, "Drama", "Pawel‚ Pawlikowski", ["Polish", "French"]);
movie33 = Movie("Viridiana", 1961, "Drama", "Luis Bunuel", "Spanish");
movie34 = Movie("The Exterminating Angel", 1962, ["Supernatural", "Surrealist"], "Luis Bunuel", "Spanish")
movie35 = Movie("Simon of the Desert", 1965, "Surrealist", "Luis Bunuel", "Spanish")
movie36 = Movie("Theeb", 2014, ["Period Drama", "Historical Drama", "Thriller"], "Naji Abu Nowar", "Arabic")

print(movie30.title)
print(movie30.year)
print(movie30.genre)
print(movie30.director)
print(movie30.language)