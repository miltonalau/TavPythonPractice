#Milton Lau
#2/25/19
#Song test run

class Song():
    
    def why(self):
        print("I don't know why she swallowed that fly,"
        "\nPerhaps she'll die.\n")

    def fly(self):
        print("There was an old woman who swallowed a fly." )
        Song.why()

    def spider(self):
        print("There was an old woman who swallowed a spider," 
        "\nThat iggled and wriggled and jiggled inside her."
        "\nShe swallowed the spider to catch the fly,")
        Song.why()

    def bird(self):
        print("There was an old woman who swallowed a bird," 
        "\nHow absurd to swallow a bird."
        "\nShe swallowed the bird to catch the spider,"
        "\nShe swallowed the spider to catch the fly,")
        Song.why()

    def cat(self):
        print("There was an old woman who swallowed a cat," 
        "\nImagine that to swallow a cat."
        "\nShe swallowed the cat to catch the bird,"
        "\nShe swallowed the bird to catch the spider,"
        "\nShe swallowed the spider to catch the fly,")
        Song.why()

    def dog(self):
        print("There was an old woman who swallowed a dog,"
        "\nWhat a hog to swallow a dog."
        "\nShe swallowed the dog to catch the cat,"
        "\nShe swallowed the cat to catch the bird,"
        "\nShe swallowed the bird to catch the spider,"
        "\nShe swallowed the spider to catch the fly,")
        Song.why()

    def horse(self):
        print("There was an old woman who swallowed a horse,"
        "\nShe died of course.")

Song = Song()

Song.fly()
Song.spider()
Song.bird()
Song.cat()
Song.dog()
Song.horse()