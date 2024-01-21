class Songs:
  def __init__(self,lyrics):
    self.lyrics=lyrics

  def sing_me_a_song(self):
    for lyric in self.lyrics:
      print(lyric)

bday=["May god bless you, "
     "Have a sunshine on you,"
      "Happy Birthday to you !"]

obj=Songs(bday)
obj.sing_me_a_song()
