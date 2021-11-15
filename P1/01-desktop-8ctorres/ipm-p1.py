#!/usr/bin/env python3

import view
import viewresults

if __name__ == '__main__':
    vista = view.View()
    vista.build_view()
    vista.show_all()
    resultados = viewresults.ViewResults()
    resultados.build_view(interval="tercera mayor", example="unas notas", songs=[("FIC", "fic.udc.es", True), ("Filo", "udc.es/filo", False), ("Comunicacion", "comunicacion.udc.es", True), ("Económicas", "economicas.udc.es", False)])
    resultados.show_all()
    vista.connect_salir_clicked(vista.quit)
    vista.connect_delete_event(vista.quit)
    resultados.connect_volver_clicked(vista.quit)
    resultados.connect_delete_event(vista.quit)
    vista.start()