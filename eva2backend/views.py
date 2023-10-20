from django.shortcuts import render

# Create your views here.
def eval(request):
    return render(request,'templatesEva2Backend/index.html')

def principal(request):
    data={
        "main":"Evaluación 2 - Backend",
        'title1':"Colombia",
        'title2':"Chile",
        'title3':"Argentina",
        'submain':'Seleccione el país que desee conocer',
        'subtitle1':'Colombia es un país del extremo norte de Sudamérica. Su paisaje cuenta con bosques tropicales, las montañas de los Andes y varias plantaciones de café.',
        'subtitle2':'Chile es un país largo y angosto que se extiende por el borde occidental de Sudamérica, con más de 6,000 km de costa en el océano Pacífico.',
        'subtitle3':'Argentina es un país sudamericano de gran envergadura con un terreno que incluye las montañas de los Andes, lagos glaciales y praderas en las Pampas',
        'imagen1':'imagenes/bandera_colombia.jpg',
        'imagen2':'imagenes/bandera_chile.jpg',
        'imagen3':'imagenes/bandera_argentina.jpg',
    }
    return render(request,'templatesEva2Backend/index.html',data)

def colombia(request):
    data={
        "main":"Colombia",
        'title1':"Habitantes",
        'title2':"Comida típica",
        'title3':"Capital",
        'submain':'Se fundó el 20 de Julio de 1810',
        'subtitle1':'Cuenta con una población de 51.52 millones de personas',
        'subtitle2':'Una de sus comidas típícas es la sopa de fríjol cabeza negra',
        'subtitle3':'Su capital es Bogotá',
        'imagen1':'imagenes/producto.jpg',
        'imagen2':'imagenes/producto.jpg',
        'imagen3':'imagenes/producto.jpg',
    }
    return render(request,'templatesEva2Backend/index.html',data)

def chile(request):
    data={
        "main":"Colombia",
        'title1':"Habitantes",
        'title2':"Comida típica",
        'title3':"Capital",
        'submain':'Se fundó el 20 de Julio de 1810',
        'subtitle1':'Cuenta con una población de 51.52 millones de personas',
        'subtitle2':'Una de sus comidas típícas es la sopa de fríjol cabeza negra',
        'subtitle3':'Su capital es Bogotá',
        'imagen1':'imagenes/producto.jpg',
        'imagen2':'imagenes/producto.jpg',
        'imagen3':'imagenes/producto.jpg',
    }
    return render(request,'templatesEva2Backend/index.html',data)

def argentina(request):
    data={
        "main":"Colombia",
        'title1':"Habitantes",
        'title2':"Comida típica",
        'title3':"Capital",
        'submain':'Se fundó el 20 de Julio de 1810',
        'subtitle1':'Cuenta con una población de 51.52 millones de personas',
        'subtitle2':'Una de sus comidas típícas es la sopa de fríjol cabeza negra',
        'subtitle3':'Su capital es Bogotá',
        'imagen1':'imagenes/producto.jpg',
        'imagen2':'imagenes/producto.jpg',
        'imagen3':'imagenes/producto.jpg',
    }
    return render(request,'eva2backend/index.html',data)