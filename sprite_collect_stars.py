"""
Sprite Collect Start

C:\Python37\python.exe C:\czarodzieje_kodu\sprite_collect_stars.py
"""

import random
import arcade
import os

# --- Skalowania ---
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_STAR = 0.1
SPRITE_SCALING_ALIEN = 0.4

STAR_COUNT = 1200
ALIEN_COUNT = 20

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Kosmiczna przygoda"


class MojaGra(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Zmienne trzymające listy
        self.player_list = None
        self.star_list = None
        self.alien_list = None

        # Informacje o graczu
        self.player_sprite = None
        self.score = 0

        # Ukrycie kursora myszy
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.COBALT)

    def setup(self):
        """ Ustawienie gry i użycie zmiennych """

        # Listy
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()

        # Punktacja
        self.score = 0

        # Ustawienia gracza
        self.player_sprite = arcade.Sprite("images/character_female.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Stworzenie gwiazd
        for i in range(STAR_COUNT):

            # Utworzenie instancji gwiazdy
            star = arcade.Sprite("images/star.png", SPRITE_SCALING_STAR)

            # Pozycje gwiazd
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)

            # Dodanie gwiazdy do listy
            self.star_list.append(star)

        # Utworzenie robotow
        for i in range(ALIEN_COUNT):

            alien = arcade.Sprite("images/character_alien.png", SPRITE_SCALING_ALIEN)
            alien.center_x = random.randrange(SCREEN_WIDTH)
            alien.center_y = random.randrange(SCREEN_HEIGHT)
            self.alien_list.append(alien)

    def on_draw(self):
        """ Wyrysowanie obiektów """
        arcade.start_render()
        self.star_list.draw()
        self.alien_list.draw()
        self.player_list.draw()

        # Wypisanie tekstu
        output = f"Wynik: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Ustawienie gracza na pozycji 
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Logika i ruchy """

        # Aktualizacja obiektów
        self.star_list.update()
        self.alien_list.update()

        # Generowanie list kolizji
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
        alien_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.alien_list)

        # Pętla punktacji dla gwiazd i robotów
        for star in star_hit_list:
            star.kill()
            self.score += 1

        for alien in alien_hit_list:
            alien.kill()
            self.score -= 10


def main():
    """ główna metoda """
    window = MojaGra()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
