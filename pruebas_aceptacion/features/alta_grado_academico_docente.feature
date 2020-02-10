Característica: Alta grado académico
    Como usuario del sistema Area Operativo de Atencion a Personal docente
    Deseo agregar un docente con su informacion escolar a la UAZ
    Para tener actualizada la información del docente

    Escenario: Datos correctos para grado académico
        Dado que ingreso al formulario para ingresar la informacion del grado académico del docente "José Andres Muro Vargas"
        Y escribo los datos: Escuela: "UAD", Fecha obtencion: "15/11/2003"
        Y escribo los datos: Categoria grados: "DOCTORADO", nombre estudio: "DOCTORADO en Ingeniería de Software"
        Y escribo los datos: cedula: "HZ2235" y la imagen "D:\\Pictures\\Diseños finales\\Mtn.jpg"
        Cuando presio el botón guardar
        Entonces puedo ver la categoria de grado: "DOCTORADO" con el nombre de estudio: "DOCTORADO en Ingeniería de Software" en la informacion escolar del docente "José Andres Muro Vargas" en los detalles del docente

    Escenario: No se escribe el nombre dek grado
        Dado que ingreso al formulario para ingresar la informacion del grado académico del docente "José Andres Muro Vargas"
        Y escribo los datos: Escuela: "UAD", Fecha obtencion: "15/11/2003"
        Y escribo los datos: Categoria de grados: "DOCTORADO"
        Y escribo los datos: cedula: "HZ2235" y la imagen "D:\\Pictures\\Diseños finales\\Mtn.jpg"
        Cuando presio el botón guardar
        Entonces permanezco en el mismo formulario ya que me falto ingresar la institucion