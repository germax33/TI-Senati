# TI-Senatiauto = {
"marca": "Toyota",
"Modelo": "Hilux",
"NumeroAccidentes": 1,
"estado": True,
"colores": ["negro", "gris"]
}

auto["estado"] = False
lista_colores = auto.get("colores")

lista_colores.append("azul")


auto["colores"] = lista_colores


print(auto)

