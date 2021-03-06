import requests
import urllib
from PIL import Image

def get_pokemons(url, pokename):

    url2= url + pokename
    response= requests.get(url2)
  
    if response.status_code == 200:
        response2= requests.get(url2)
        payload2= response2.json()
        sprites= payload2.get('sprites', [])
        types= payload2.get('types', [])
        abilities= payload2.get('abilities', [])
        stats= payload2.get('stats', [])
        front_sprite=''
        tipo1=0
        habilidad=0
        stabs=0
        valor=0
        oculta= False
        si= '-Habilidad oculta-'

        print("\n\t", pokename.upper())

        if sprites:
            #Descargando Imagen
            front_sprite= sprites['front_default']
            imagen= open("./Sprite/Sprite.png", 'wb')
            imagen.write(urllib.request.urlopen(front_sprite).read())
            imagen.close()

            #Abriendo imagen
            ruta= ("./Sprite/Sprite.png")
            In= Image.open(ruta)
            In.show()


        print("\n***Tipo***")
        if types:
            for tipos in types:
                tipo1= tipos['type']
                print(tipo1['name'])

        print("\n***Habilidades***")
        if abilities:
            for hiden in abilities:
                oculta= hiden['is_hidden']
                habilidad= hiden['ability']
                if(oculta== True):
                    print(habilidad['name'],si)
                else:
                    print(habilidad['name'])
                    
        print("\n***Stats Base***")
        if stats:
            for base in stats:
                valor= base['base_stat']
                stabs= base['stat']
                print(stabs['name'], ": ",valor)

    else:
        print("\nMal escrito o Pokemon no existente en base de datos.")


if __name__ == "__main__":
    url='http://pokeapi.co/api/v2/pokemon/'
    nombrepokemon=str(input("\nPokemon: "))
    pokename= nombrepokemon.lower()

    get_pokemons(url,pokename)