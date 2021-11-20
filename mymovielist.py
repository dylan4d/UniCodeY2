""" Classes to implement a (simulated) movie list.

E.g. "My List" on Netflix

Note that the movies, TV series, etc. exist as independent objects, stored
elsewhere in the system. What we are doing with MyMovieList is linking them
together so that we can recall them and browse them.

For this to work in a single programming exercise, we are including the
definition of the Movie class, and in the test methods we may create some
new movie objects.

For CS2515 labs on DoublyLinked Lists

Note that the test method has been updated since the lab was issued.
"""

class Movie:
    """ A movie in a library. """

    def __init__(self, i_title, i_director, i_cast, i_minutes):
        """ Create a new movie.

        Args:
             i_title: the (string) title of the movie
             i_director: the (string) name of the director
             i_cast: the (string) of names of cast members
             i_minutes: the (int) length of the movie in minutes

        """
        self.title = i_title
        self.director = i_director
        self.cast = i_cast
        self.minutes = i_minutes


    def __str__(self):
        """ Return a short string representation of the movie. """
        return (   str(self.title) + ", by "
                   + str(self.director))


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
        """ Create some tracks and test their methods.

        Note that this does not have the 'self' input argument, and so is a
        class method - that means it is called by Movie._test() and not by
        (e.g.) m._test(), where m is some instance of the Movie class.
        """
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


class MyMovieList:
    """ A movie library maintained as a doubly linked list of Movie objects.

    Attributes: (all private)
    """

    # _head: an empty DLLMovieNode to start the list
    # _tail: an empty DLLMovieNode to end the list
    # _size: the number of Movie instances in the list
    # _current: one node in the list, representing the current selection
    #           This must always refer to a real node in the list (as opposed
    #           to the dummy head or tail nodes), unless the list is empty, in
    #           which case it refers to the dummy head.

    def __init__(self):
        """ Initialise an empty library. """
        self._head = DLLMovieNode(None, None, None)  # before the first item
        self._tail = DLLMovieNode(None, self._head, None)  # after the last item
        self._head._next = self._tail
        self._size = 0          # an integer
        self._current = self._head    # the node of the currently selected movie


    def __str__(self):
        """ Return a string representation of the list. """
        outstr = "\n$$$ M movie list\n"
        node = self._head._next
        while node != self._tail:
            if self._current == node:
                outstr += "--> "
            else:
                outstr += "    "
            outstr += "(" + str(node._element) + ")\n"
            # can access node's private variable, because defined in this file
            node = node._next
        return outstr + "$$$\n"

#---------- Public Methods ------------------------------#
    
    def add_movie(self, movie):
        """ Add movie to the end of the list.

        Args:
            movie: the Movie instance to be added

        """
        node = DLLMovieNode(movie, None, None)
        self._add_node_after(node, self._tail._prev)
        if self._size == 1:
            self._current = self._head._next


    def get_current(self):
        """ Get the currently selected movie.

        Returns the Movie instance.
        """
        return self._current._element


    def next_movie(self):
        """ Select the movie after the current one, in current order.
            Wrap around if at the end of the list.
        """
        if self._size > 0:
            if self._current._next == self._tail:
                self._current = self._head
            self._current = self._current._next
        else:
            self._current = self._head

    def prev_movie(self):
        """ Select movie before the current one, in current order.
            Wrap around if at the start of the list.
        """
        if self._size > 0:
            if self._current == self._head:
                self._current = self._tail
            self._current = self._current._prev
        else:
            self._current = self._head


    def reset(self):
        """ Reset the current movie to point to the first movie
            (assuming there is one -- self._head if not)
        """
        if self._size > 0:
            self._current = self._head._next
        else:
            self._current = self._head


    def info(self):
        """ Display the info for the current movie to the screen. """
        if self._size == 0:
            print('\nEmpty list - no movie info to display!\n')
        else:
            print("(Info) " + self._current._element.get_info())


    def remove_current(self):
        """ Remove the currently selected movie from the list.

        Returns the Movie instance that has been removed.
        """
        if self._current == self._head:
            return None
        temp = self._current
        self._current = temp._next
        if temp._next == self._tail:
            if self._size > 1:   # since if it is 1, that node is about to be removed
                self._current = self._head._next
            else:
                self._current = self._head
        return self._remove_node(temp) # and this will decrement size


    def length(self):
        """ Return the number of movies.
        """
        return self._size


    def search(self, word):
        """ Return the next movie which contains word as a substring.

        If movie is found, current movie should change to be that one.
        If no such movie, leave current selection where it is, and return None.
        """
        if self._size == 0:
            return None
        old = self._current
        wrapped = False
        while not wrapped:
            movie = self._current._element
            print('      searching', movie)
            if (word in movie.title
                or word in movie.director
                or word in movie.cast):
                return movie
            self.next_movie()
            if self._current == self._tail:
                self.next_movie()
            if self._current is old:
                wrapped = True
        return None



# ---------- Private Methods ------------------------------ #


    def _add_node_after(self, node, nodebefore):
        """ (Private) Add a node after the specified DLLNode """
        node._prev = nodebefore
        node._next = nodebefore._next
        nodebefore._next._prev = node
        nodebefore._next = node
        self._size = self._size + 1


    def _remove_node(self, node):
        """ (Private) Remove a node and return its element.

        Note: wipes the DLLNode. """
        self._extract_node(node)
        item = node._element
        node._element = None   # cleaning up, so that Python can save space
        return item


    def _extract_node(self, node):
        """ (Private) Remove a DLLNode from the list.

        Note: leaves the Track instance with the  DLLNode.
        """
        if self._current == node:
            self._current = node._prev
        node._prev._next = node._next
        node._next._prev = node._prev
        node._next = None
        node._prev = None
        self._size = self._size - 1


    def _print_node(self, node):
        """ (Private) test function to print internal node details. """
        print('   ' + str(node._element)
                    + "[" + str(node._prev._element)
                    + "--" + str(node._next._element) + "]")





# ----------- End of class definition for MyMovieList --------------------- #


def _lab_test():
    """ The test sequence specified in the lab description. """
    ml = MyMovieList()
    ml.add_movie(Movie("No time to die", "Cari Joji Fukanaga", "Daniel Craig, Anna de Armas", 163))
    ml.add_movie(Movie("Black Widow", "Cate Shortland", "Scarlett Johanssen, Florence Pugh", 134))
    ml.add_movie(Movie("The Trial of the Chicago 7", "Aaron Sorkin", "Eddie Redmayne, Alex Sharp, Sacha Baron Cohen", 129))
    print(ml)
    ml.next_movie()
    print('[stepped forward one movie, now printing selection')
    ml.info()
    ml.next_movie()
    print('[stepped forward one movie, now printing full list]')
    print(ml)
    print("\nCurrent: " + str(ml.get_current()) + "\n")
    ml.prev_movie()
    ml.remove_current()
    print('[stepped back one movie, then deleted selection, so current should have stepped forward again]')
    print(ml)
    print('[printing current selection: ]')
    ml.info()
    ml.add_movie(Movie("Dune", "Denis Villeneuve", "Timothée Chalamet, Rebecca Ferguson", 155))
    ml.next_movie()
    ml.next_movie()
    print('[added Dune as a new movie, then stepped forward twice, so should be at start, then printing current selection]')
    ml.info()
    print('[Now printing full list: ]')
    print(ml)
    word = 'ill'
    print("Searching for 'ill' ")
    movie = ml.search(word)
    if movie is not None:
        print('Found movie matching', word, ':')
        print('[and so current selection should now be that movie]')
        ml.info()
    else:
        print('No match for', word)
    print('[so current selection should not have changed]')
    ml.info()
    print('[and now printing the final list]')
    print(ml)



def _teststate(input1, input2):
    """ Compare two strings, and print an error message if not the same. """
    if input1 != input2:
        print("ERROR: should have been: "
                  + str(input2)
                  + " but was: "
                  + str(input1))

_lab_test()
