# Results window view

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class ViewResults:
    def build_view(self, songs, interval, example):
        self.songs_list = songs

        self.window = Gtk.Window(title="Xazam - Resultados")

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.window.add(self.vbox)

        self.label1 = Gtk.Label(f"Para el intervalo {interval}, un ejemplo sería:")
        self.vbox.pack_start(self.label1, expand=True, fill=False, padding=5)

        self.label_ejemplo = Gtk.Label(example)
        self.vbox.pack_start(self.label_ejemplo, expand=True, fill=False, padding=5)

        self.label_canciones = Gtk.Label("Canciones representativas del intervalo: ")
        self.vbox.pack_start(self.label_canciones, expand= True, fill=False, padding=5)

        # Las canciones se almacenan en una lista de tuplas (ternas) de la forma (nombre, link, is_fav)
        # Dicha lista viene por parámetro. La ventana de resultados se instancia cuando ya se saben los resultados

        # El conjunto de los tres elementos que muestran una canción (la label con su nombre, la label que indica
        # si es o no favorita, y el botón de escuchar), vienen en un contenedor Gtk.HorizontalBox, que se añade a la ventana
        # principal

        # Generador de widgets de canciones
        self.songs_generator = self._get_song_box()
        self.vbox.pack_start(self.songs_generator.__next__(), expand=True, fill=False, padding=5)

        # Boton para ver más

        self.see_more_align = Gtk.Alignment(xalign= 0.10, xscale=0, yalign=0.10, yscale=0)
        see_more_button = Gtk.Button("Ver más")
        see_more_button.connect('clicked', self.see_more)
        self.see_more_align.add(see_more_button)
        self.vbox.pack_start(self.see_more_align, expand=True, fill=False, padding=5)

        # Boton de volver

        self.volver_align = Gtk.Alignment(xalign= 0.90, xscale=0, yalign=0.10, yscale=0)
        self.volver_button = Gtk.Button("Volver")
        self.volver_align.add(self.volver_button)
        self.vbox.pack_end(self.volver_align, expand=True, fill=False, padding=5)


    def see_more(self, wigdet):
        # Hides away the "Ver más" button
        self.see_more_align.hide()
        for songbox in self.songs_generator:
            self.vbox.pack_start(songbox, expand=True, fill=False, padding=5)
            songbox.show_all()

    # Yields a horizontal box with the widgets referring to a song from the list
    def _get_song_box(self):
        import webbrowser
        for song in self.songs_list:
            song_title = Gtk.Label(song[0])
            is_fav = Gtk.Label("❤️" if song[2] else "♡") #Shows a heart if the song is considered "favorite"
            listen_button = Gtk.Button(label="Escuchar")
            listen_button.connect('clicked', (lambda x: webbrowser.open(song[1])))

            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            hbox.pack_start(song_title, expand=True, fill=True, padding=5)
            hbox.pack_start(is_fav, expand=True, fill=False, padding=5)
            hbox.pack_start(listen_button, expand=True, fill=False, padding=5)
            yield hbox

    def show_all(self):
        self.window.show_all()

    def connect_delete_event(self, handler):
        self.window.connect('delete-event', handler)

    def connect_volver_clicked(self, handler):
        self.volver_button.connect('clicked', handler)