from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)

    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


sample_text = ''' 
Marvel is a renowned American entertainment company known for its creation of iconic superhero comic book characters and its extensive multimedia universe. Founded in 1939 as Timely Publications and later known as Marvel Comics, the company has played a significant role in shaping popular culture.

Marvel's roster of characters includes beloved figures such as Spider-Man, Iron Man, Captain America, Thor, the Hulk, and the X-Men, among many others. These characters have become cultural symbols, transcending comic books to feature in various forms of media, including television, film, and merchandise.

The Marvel Cinematic Universe (MCU) has been a groundbreaking achievement, comprising a series of interconnected films that have redefined the superhero genre. Notable MCU films include "The Avengers," "Black Panther," and "Avengers: Endgame," which became the highest-grossing film of all time.

Marvel's impact extends beyond comics and movies, influencing television series, animation, and gaming. The company continues to evolve, introducing new characters and storylines that captivate audiences worldwide. Marvel's enduring legacy lies in its ability to tell compelling stories, create diverse and relatable characters, and connect with audiences across generations.
 '''


generate_word_cloud(sample_text)
