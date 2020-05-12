import requests

def get_pokemons(url, offset, pokename):

    args= {'offset':offset} if offset else {}

    response= requests.get(url, params= args)
    name=[]
    encontrado=0

    if response.status_code == 200:
        payload= response.json()
        results= payload.get('results', [])

        if results:
            for pokemon in results:
                name.append(pokemon['name'])
        
        for i in range(len(name)):
            if name[i] == pokename:
                encontrado=1
                print("\n¡Existe en la base de datos!")
                url2= 'http://pokeapi.co/api/v2/pokemon/' + pokename
                if response.status_code == 200:
                    response2= requests.get(url2)
                    payload2= response2.json()
                    types= payload2.get('types', [])
                    abilities= payload2.get('abilities', [])
                    stats= payload2.get('stats', [])
                    tipo1=0
                    habilidad=0
                    stabs=0
                    valor=0
                    oculta= False
                    si= '-Habilidad oculta-'

                    print("\n***Habilidades***")
                    if abilities:
                        for hiden in abilities:
                            oculta= hiden['is_hidden']
                            habilidad= hiden['ability']
                            if(oculta== True):
                                print(habilidad['name'],si)
                            else:
                                print(habilidad['name'])

                    print("\n***Tipo***")
                    if types:
                        for tipos in types:
                            tipo1= tipos['type']
                            print(tipo1['name'])
                    
                    print("\n***Stats Base***")
                    if stats:
                        for base in stats:
                            valor= base['base_stat']
                            stabs= base['stat']
                            print(stabs['name'], ": ",valor)
        
        if(encontrado==0):
            offset= offset+20
            get_pokemons(url,offset,pokename) 

         



if __name__ == "__main__":
    url='http://pokeapi.co/api/v2/pokemon-form/'
    offset=0
    nombrepokemon=str(input("\nNombre del Pokemon: "))
    pokename= nombrepokemon.lower()

    get_pokemons(url,offset,pokename)