Característica: Alta datos personales de docente
    Como usuario del sistema Area Operativo de Atencion a Personal docente
    Deseo agregar un docente con su informacion personal y laboral
    Para tener actualizada la información del docente

    Escenario: Datos correctos para el docente
        Dado que ingreso al formulario para ingresar la informacion un nuevo docente
        Y escribo los datos personales: nombres: "Pedro Angel", apellido paterno: "Sanchez", apellido materno: "Hinostroza"
        Y escribo los datos personales: fecha de nacimiento: "07/10/1998", rfc: "SAHP981007KF7", curp:"SAHP981007HZSNND03"
        Y escribo los datos personales: nss: "123124", sexo: "HOMBRE", estado civil:"SOLTERO"
        Y escribo los datos personales: domicilio: "Netzahualcoyotl 107", municipio: "Zacatecas", estatus: "True"
        Y escribo los datos laborales: matricula docente: "1231", matricula nomina: "312312", fecha de ingreso: "07/10/2016"
        Y escribo los datos laborales: numero expediente: "12.31", es exclusivo: "True", cvu: "31241", cuerpo academico:"los perrones", programa:"Ingeniería de Software"
        Y escribo los datos conacyt: numero de proyecto: "3124", nombre del proyecto: "Un proyecto chido", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018"
        Y escribo los datos prodep: clave: "23123", descripcion: "Un prodep bien perris", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018", imagen prodep: "C:\\UAZ\\Constancia.jpeg"
        Y escribo los datos sni: clave: "23123", descripcion: "Un sni bien perris", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018", nivel: "SNI 1", imagen nivel: "C:\\UAZ\\Constancia.jpeg"
        Cuando presiono el botón guardar de docente
        Entonces puedo ver el docente: "Pedro Angel Sanchez Hinostroza" en la lista

    Escenario: Datos incorrectos para el docente
        Dado que ingreso al formulario para ingresar la informacion un nuevo docente
        Y escribo los datos personales: apellido paterno: "Sanchez", apellido materno: "Hinostroza"
        Y escribo los datos personales: fecha de nacimiento: "07/10/1998", rfc: "SAHP981007KF7", curp:"SAHP981007HZSNND03"
        Y escribo los datos personales: nss: "123124", sexo: "HOMBRE", estado civil:"SOLTERO"
        Y escribo los datos personales: domicilio: "Netzahualcoyotl 107", municipio: "Zacatecas", estatus: "True"
        Y escribo los datos laborales: matricula docente: "1231", matricula nomina: "312312", fecha de ingreso: "07/10/2016"
        Y escribo los datos laborales: numero expediente: "12.31", es exclusivo: "True", cvu: "31241", cuerpo academico:"los perrones", programa:"Ingeniería de Software"
        Y escribo los datos conacyt: numero de proyecto: "3124", nombre del proyecto: "Un proyecto chido", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018"
        Y escribo los datos prodep: clave: "23123", descripcion: "Un prodep bien perris", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018", imagen prodep: "C:\\UAZ\\Constancia.jpeg"
        Y escribo los datos sni: clave: "23123", descripcion: "Un sni bien perris", fecha de inicio: "07/10/2017", fecha de termino: "07/10/2018", nivel: "SNI 1", imagen nivel: "C:\\UAZ\\Constancia.jpeg"
        Cuando presiono el botón guardar de docente
        Entonces permanezco en el mismo formulario ya que me falto ingresar datos