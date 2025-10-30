El programa debe estar realizado para python 3.12.
• El programa tiene que ser implementado utilizando un esqueleto de proyecto como el
provisto por cookiecutter.
• Toda vez que sea posible hay que separar la lógica funcional de la lógica relacionada
con la presentación e interacción con el usuario.
• El programa debe utilizar reglas de formateo PEP8.
• El programa debe utilizar las convenciones de PEP257 para los docstrings.
• El programa debe utilizar ru5 & black para formateo consistente.
• Debes tener especial cuidado que la ejecución de ru5 no de errores.
• El programa debe utiliza MyPy para los módulos principales.
• El programa debe ser realizado en un formato tal que permita la utilización como
package Python.
• El programa debe utilizar técnicas de programación de object oriented.
• El programa debe implementar las funciones toda vez que sea posible mediante el
uso de patrones.
• Deben implementarse con PyTest las hipótesis de test unitario que permitan una
cobertura objetivo del 80% o mejor.
• Se debe utilizar bandit para la evaluación básica de seguridad y asegurar que el
código resultante no tiene observaciones significativas.
• Debe producirse la documentación básica inicial del funcionamiento del módulo y
reflejarla con un archivo en lenguaje markdown (.md) que se incluya con el proyecto.
• Las funciones implementadas deben tener tratamiento y gestión de las excepciones
producidas durante el runtime además de las que sean específicamente pedidas en
la historia a implementar.
• Produce un archivo comprimido con toda la estructura necesaria para subir el
proyecto a GitHub
• Agrega al proyecto un archivo especificando que la licencia será MIT
• Si el proyecto tiene dependencias externas mandatorias u opcionales produce el
archivo requirements.txt necesario que permita instalar todos los paquetes que sean
dependencias directas u opcionales.
• El programa debe ser optimizado por performance.
• Automatiza en Github integrando la fase de CI/CD completa
• Aumenta la cobertura y validación funcional de acuerdo a tus recomendaciones
• Publica y documenta la creación de un README.md y un CHANGELOG.md mas
detallado
• Genera una versión de la documentación automáticamente con pdoc o sphinx
Prompt funcional
La siguiente es la descripción del caso de uso o historia que describe la función que se
necesita implementar. Se trata de una función para el cálculo del factorial de un número
dado, el número podrá ser proporcionado por argumento o ingresado por teclado por el
usuario en forma mutuamente excluyente. Se harán controles de rango sobre la validez
del número provisto de acuerdo a la definición de la función factorial y la capacidad de
calcularlo sin dar errores por desborde.