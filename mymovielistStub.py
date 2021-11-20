""" Classes to implement a (simulated) movie list.

E.g. "My List" on Netflix

Note that the movies, TV series, etc. exist as independent objects, stored
elsewhere in the system. What we are doing with MyMovieList is linking them
together so that we can recall them and browse them.

For this to work in a single programming exercise, we are including the
definition of the Movie class, and in the test methods we may create some
new movie objects.

For CS2515 labs on DoublyLinked Lists

Stub file - the implementation of the class MyMovieList needs to be
completed.
"""

class Movie:
    """ A movie in a library. """

    def __init__(self, i_title, i_director, i_cast, i_minutes):
        """ Create a new movie.

        Args:
             i_title: the (string) title of the movie
             i_director: the (string) name of the director
             i_cast: the (string) of names of cast members
             i_length: the (int) length of the movie in minutes

        """
        self.title = i_title
        self.director = i_director
        self.cast = i_cast
        self.minutes = i_minutes


    def __str__(self):
        """ Return a short string representation of the movie. """
        return (   str(self.title) + ", by "  + str(self.director))


    def get_info(self):
        """ Return a full string representation of the movie. """
        ret_str = ("Title: " + str(self.title) + "; "
                   + "Director: " + str(self.director) + "; "
                   + "Cast: " + str(self.cast) + "; "
                   + "Minutes: " + str(self.minutes) + "; ")
        return ret_str


    def play(self):
        """ Simulate the movie being played. """
        print("   Now playing", self)
        print("   ...")
        print("   (", self.minutes, " minutes later ...)")
        print("   THE END")


    def _test():
        """ Create some tracks and test their methods. """
        movie_a = Movie("No time to die", "Cari Joji Fukanaga",
                           "Daniel Craig, Anna de Armas", 163)
        movie_b = Movie("Black Widow", "Cate Shortland",
                           "Scarlett Johanssen, Florence Pugh", 134)
        movie_c = Movie("The Trial of the Chicago 7", "Aaron Sorkin",
                           "Eddie Redmayne, Alex Sharp, Sacha Baron Cohen",
                           129)
        print("movie_a is: ", movie_a)
        print('movie_b info is:', movie_b.get_info())
        print("now about to play movie_c")
        movie_c.play()

Movie._test()


class DLLMovieNode:
    """ An internal node in a doubly linked list of Movie files.

    Attributes: (all private)
    """

    # _element: the object in this position in the list
    # _next: the next DLLMovieNode instance in the list
    # _prev: the previous DLLMovieNode instance in the list

    def __init__(self, item, prevnode, nextnode):
        self._element = item
        self._next = nextnode
        self._prev = prevnode
    
    def add_after(self, item, before):


    def add_first(self, item, before):
        

    def add_last(self, item):
        

    def get_first(self):
        pass

    def get_last(self):
        pass

    def remove_node(self, node):
        pass

    def remove_first(self):
       pass

    def remove_last(self):
       pass



class MyMovieList:
    """ A movie library maintained as a doubly linked list of Movie objects.

    Attributes: (all private)
    """

    # Can be implemented with the dummy head and dummy tail, or instead with
    # fields first and last, that point to DLLMovieNodes with real movie
    # instances

    # but must have the following two fields:

    # _size: the number of Movie instances in the list
    # _current: one node in the list, representing the current selection
    #           This must always refer to a real node in the list (as opposed
    #           to a dummy head or tail node), unless the list is empty, in
    #           which case it refers to the dummy head.

    def __init__(self):
        """ Initialise an empty library. """


    def __str__(self):
        """ Return a string representation of the list. """

#---------- Public Methods ------------------------------#

# This is the specification - each one of these methods should be implemented,
# return types should not be different from that specified, the order of the
# arguments should not change, and arguments should not be removed.
# If you add additional arguments, they must go at the end of the sequence,
# and they must be optional.
# Anyone calling your code must be able to invoke the methods below exactly
# as they are specified, and they must receive return types as specified.


    def add_movie(self, movie):
        """ Add movie to the end of the list.

        Args:
            movie: the Movie instance to be added

        """


    def get_current(self):
        """ Get the currently selected movie.

        Returns the Movie instance.
        """


    def next_movie(self):
        """ Select the movie after the current one, in current order.
            Wrap around if at the end of the list.
        """

    def prev_movie(self):
        """ Select movie before the current one, in current order.
            Wrap around if at the start of the list.
        """


    def reset(self):
        """ Reset the current movie to point to the first movie
            (assuming there is one -- if the list is empty, then should point
             to dummy head (if used) or should point to None)
        """


    def info(self):
        """ Display the info for the current movie to the screen. """


    def remove_current(self):
        """ Remove the currently selected movie from the list.

        Returns the Movie instance that has been removed.
        Returns None if the list is empty.
        """


    def length(self):
        """ Return the number of movies. """


    def search(self, word):
        """ Return the next movie (ie current selection or after) which
            contains word anywhere as a substring.

        If movie is found, current movie should change to be that one.
        If no such movie, leave current selection where it is, and return None.
        """



# ---------- Private Methods ------------------------------ #


# Methods in here are for you as programmer, if they help you write the public
# methods.

# Some of the methods from the lecture on DoublyLinkedLists might be useful.
# I use  add_node_after() and remove_node()

# But you don't have to put anything here - it is fine to implement it
# directly inside the public methods above.




# ----------- End of class definition for MyMovieList --------------------- #


def _lab_test():
    """ The test sequence specified in the lab description. """
    ml = MyMovieList()
    ml.add_movie(Movie("No time to die", "Cari Joji Fukanaga", "Daniel Craig, Anna de Armas", 163))
    ml.add_movie(Movie("Black Widow", "Cate Shortland", "Scarlett Johanssen, Florence Pugh", 134))
    ml.add_movie(Movie("The Trial of the Chicago 7", "Aaron Sorkin", "Eddie Redmayne, Alex Sharp, Sacha Baron Cohen", 129))
    print(ml)
    ml.next_movie()
    ml.info()
    ml.next_movie()
    print(ml)
    print("\nCurrent: " + str(ml.get_current()) + "\n")
    ml.prev_movie()
    ml.remove_current()
    print(ml)
    ml.info()
    ml.add_movie(Movie("Dune", "Denis Villeneuve", "Timothée Chalamet, Rebecca Ferguson", 155))
    ml.next_movie()
    ml.next_movie()
    ml.info()
    print(ml)
    word = 'ill'
    print("Searching for 'ill' ")
    movie = ml.search(word)
    if movie is not None:
        print('Found movie matching', word, ":")
        ml.info()
    else:
        print('No match for', word)
    print(ml)



def _teststate(input1, input2):
    """ Compare two strings, and print an error message if not the same. """
    if input1 != input2:
        print("ERROR: should have been: "
                  + str(input2)
                  + " but was: "
                  + str(input1))

_lab_test()
