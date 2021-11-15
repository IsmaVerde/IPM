# Main window view

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class View:
    @classmethod
    def start(cls):
        Gtk.main()

    @classmethod
    def quit(cls, widget):
        Gtk.main_quit()

    def build_view(self):
        self.window = Gtk.Window(title="Xazam")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.window.add(vbox)

        self.label1 = Gtk.Label("Seleccionar intervalo:")
        vbox.pack_start(self.label1, expand=True, fill=False, padding=5) #Child of VBOX

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        #Dropdown list
        
        drop_list = Gtk.ListStore(str)
        drop_list.append(["Segunda menor (2m)"])
        drop_list.append(["Segunda mayor (2M)"])
        drop_list.append(["Tercera menor (3m)"])
        drop_list.append(["Tercera mayor (3M)"])
        drop_list.append(["Cuarta justa (4j)"])
        drop_list.append(["Cuarta aumentada (4aum)"])
        drop_list.append(["Quinta justa (5j)"])
        drop_list.append(["Sexta menor (6m)"])
        drop_list.append(["Sexta mayor (6M)"])
        drop_list.append(["Séptima menor (7m)"])
        drop_list.append(["Séptima mayor (7M)"])
        drop_list.append(["Octava (8a)"])

        self.dropdown_menu = Gtk.ComboBox.new_with_model(drop_list)
        text_renderer = Gtk.CellRendererText()
        self.dropdown_menu.pack_start(text_renderer, expand=True)
        self.dropdown_menu.add_attribute(text_renderer, "text", 0)

        # Radio Buttons

        self.asc_radiobutton = Gtk.RadioButton.new_with_label(None, "Asc")
        self.des_radiobutton = Gtk.RadioButton.new_with_label_from_widget(self.asc_radiobutton, "Des")
        
        radiobuttons_box = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        radiobuttons_box.pack_start(self.asc_radiobutton, expand=False, fill=False, padding=3)
        radiobuttons_box.pack_start(self.des_radiobutton, expand=False, fill=False, padding=3)

        hbox.pack_start(Gtk.Box(), expand=False, fill=False, padding=2)

        hbox.pack_start(self.dropdown_menu, expand=True, fill=True, padding=10) ##Child of HBOX

        hbox.pack_start(radiobuttons_box, expand=False, fill=False, padding=5) ##Child of HBOX

        self.button_buscar = Gtk.Button(label="Buscar")
        hbox.pack_start(self.button_buscar, expand=False, fill=False, padding=10) ##Child of HBOX

        hbox.pack_start(Gtk.Box(), expand=False, fill=False, padding=2)

        vbox.pack_start(hbox, expand=True, fill=False, padding=5) #Child of VBOX

        self.button_salir = Gtk.Button(label="Salir")

        salir_align = Gtk.Alignment(xalign= 0.90, xscale=0, yalign=0.10, yscale=0)
        salir_align.add(self.button_salir)

        vbox.pack_start(salir_align, expand=True, fill=True, padding=5) #Child of VBOX

    def show_all(self):
        self.window.show_all()

    def connect_buscar_clicked(self, handler):
        self.button_buscar.connect('clicked', handler)

    def connect_interval_changed(self, handler):
        self.dropdown_menu.connect('changed', handler)

    def connect_ascdes_changed(self, handler):
        return

    def connect_delete_event(self, handler):
        self.window.connect('delete-event', handler)

    def connect_salir_clicked(self, handler):
        self.button_salir.connect('clicked', handler)