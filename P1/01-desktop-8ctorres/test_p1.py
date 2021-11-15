#!/usr/bin/env python3

import sys
import textwrap
from collections import namedtuple

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

import e2e

"""Histories:
    GIVEN he lanzado la aplicación
    THEN veo el texto "Seleccionar intervalo"
    GIVEN he lanzado la aplicación
    WHEN selecciono '3M'
    THEN la vista del intervalo muestra el texto "Tercera mayor(3M)"
    GIVEN he lanzado la aplicacion
    WHEN selecciono 'asc'
    THEN el intervalo es asc
    GIVEN he lanzado la aplicación
    WHEN busco intervalo
    THEN compruebo favorita
"""

# Funciones de ayuda

def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "    Passed", '\033[0m')

def show_not_passed(e):
    print('\033[91m', "    Not passsed", '\033[0m')
    print(textwrap.indent(str(e), "    "))


# Contexto de las pruebas

Ctx = namedtuple("Ctx", "path process app")


# Implementación de los pasos

def given_he_lanzado_la_aplicacion(ctx):
    process, app = e2e.run(ctx.path)
    assert app is not None
    return Ctx(path= ctx.path, process= process, app= app)

def then_veo_el_texto_Seleccionar_intervalo(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, 0).startswith("Seleccionar intervalo"))
    label = next(gen, None)
    assert label and label.get_text(0, 0, 0) == "Seleccionar intervalo:", label.get_text(0, 0, 0)
    return ctx

def when_selecciono_3M(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'combo box' and node.get_name() == 'Tercera mayor (3M)')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'press')
    return ctx
    
def then_veo_el_texto_3M(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'menu item' and node.get_text(0, 0, 1,  1, 0, 3).startswith("Tercera mayor"))
    label = next(gen, None)
    assert item and label.get_text(1, 0, 0) == "Para el intervalo tercera mayor, un ejemplo sería", label.get_text(1, 0, 0)
    return ctx

def when_selecciono_asc(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'radio button' and node.get_name() == 'asc')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    return ctx
  
def then_el_intervalo_es_asc(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'radio button' and node.get_text(0, 0, 1, 2, 0).startswith("asc"))
    label = next(gen, None)
    assert label and label.get_text(1, 0, 1) == "Do - Mi", label.get_text(1, 0, 1)
    return ctx

def when_busco_intervalo(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button' and node.get_name() == 'Buscar')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    return ctx

def then_compruebo_favorita(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(1, 0, 3, 0).startswith("cumpleaños feliz"))
    label = next(gen, None)
    assert label and label.get_text(1, 0, 3, 1) == "❤️", label.get_text(1, 0, 3, 1)
    return ctx


if __name__ == '__main__':
    sut_path = sys.argv[1]
    initial_ctx = Ctx(path= sut_path, process= None, app= None)

    show("""
    GIVEN he lanzado la aplicación
    THEN veo el texto "Seleccione intervalo"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = then_veo_el_texto_Seleccionar_intervalo(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    
    show("""
    GIVEN he lanzado la aplicación
    WHEN selecciono '3M'
    THEN la vista del intervalo muestra el texto "Tercera mayor(3M)"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_selecciono_3M(ctx)
        ctx = then_veo_el_texto_3M(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
    
    show("""
    GIVEN he lanzado la aplicacion
    WHEN selecciono 'asc'
    THEN el intervalo es asc
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_selecciono_asc(ctx)
        ctx = then_el_intervalo_es_asc
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
    
    show("""
    GIVEN he lanzado la aplicación
    WHEN busco intervalo
    THEN compruebo favorita
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_busco_intervalo(ctx)
        ctx = then_compruebo_favorita(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
