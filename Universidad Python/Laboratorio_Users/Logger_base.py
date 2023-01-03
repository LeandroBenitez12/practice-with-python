import logging as log

#agregamos mas caracteristicas
log.basicConfig(
    level=log.INFO,
    format=('%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s'),
    datefmt = '%I:%M:%S %p',
    handlers= [
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
)    
#configuramops el nivel a trabajar
#Al poner en el LEVEL = DEBUG se van a estar imprimeindo todos ya que es el nivel mas basico hacia adelante


if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG')
    log.info('Mensaje a nivel INFO')
    log.error('Mensaje a nivel ERROR')
    log.warning('Mensaje a nivel WARNING')
    log.critical('Mensaje a nivel CRITICAL')
# ESTE ARCHIVO LO VAMOS A USAR EN OTROS PROGRAMAS
