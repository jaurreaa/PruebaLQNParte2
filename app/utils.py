def generic_model_mutation_process(model, data, id=None, commit=True):
    """ Recibe 4 parametros: model, data, id y commit """
    if id:# Si id es True
        item = model.objects.get(id=id)#Traemos el id del modelo que nos estan pasando
        try:
            del data['id'] # Eliminamos el id de la data que nos esta llegando
        except KeyError:
            pass # De lo contrario dejamos pasar

        for field, value in data.items():
            #Recorremos los items que nos trae data
            setattr(item, field, value)
    else:
        #Si id es None o false la variable item la igualamos a el diccionario que nos llega en data
        item = model(**data)

    if commit:
        #Si commit es True
        item.save()
        #Guardamos la información ya validada anterior mente

    return item
    #Returnamos la información
