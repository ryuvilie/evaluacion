import csv
import random
import math
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos={}

def asignar_sueldos(trabajadores):
    sueldos={trabajador : random.randint(300000,2500000) for trabajador in trabajadores}
    print("asignando sueldos... ")
    for trabajador, sueldo in sueldos.items():
        print(f"{trabajador}: ${sueldo}")
    return sueldos


def clasificar_sueldos(sueldos):
    clasificaciones={"sueldos menores a $800.000":[],"sueldos entre $800.000 y $2.000.000":[],"sueldos superiores a $2.000.000": []}
    for trabajadores, sueldo in sueldos.items():
        if sueldo <  800000:
            clasificaciones["sueldos menores a $800.000"].append((trabajadores, sueldo))
        elif sueldo <2000000:
            clasificaciones["sueldos entre $800.000 y $2.000.000"].append((trabajadores, sueldo))
        else:
            clasificaciones["sueldos superiores a $2.000.000"].append((trabajadores, sueldo))
        print("sueldos clasificados")
        for clasificacion, trabajadores in clasificaciones.items():
            print(f"{clasificacion}  TOTAL:{len(trabajadores)}")
            print()
            print("NOMBRE TRABAJADOR     SUELDO")
            for trabajador, sueldo in trabajadores:
                print(f"{trabajador}       {sueldo}")
            print()
        print()
    print(f"TOTAL SUELDOS: $ {sum(sueldos.values())}")

def ver_estadisticas(sueldos):
    print("ESTADISTICAS")
    print()
    sueldo_max=max(sueldos.values())
    print(f"sueldo más alto: {sueldo_max}")
    sueldo_min=min(sueldos.values())
    print(f"sueldo más bajo: {sueldo_min}")
    promedio=round(sum(sueldos.values()) / len(sueldos.values()))
    print(f"promedio de sueldos: {promedio}")
    producto=1
    for sueldo in sueldos.values():
        producto*= sueldo
    medida_geometrica=math.pow(producto, 1/len(sueldos))
    print(f"medida geometrica: {round(medida_geometrica)}")

def reporte_sueldos(sueldos):
    print("nombre trbajador sueldo base  descuento salud  descuento AFP sueldo liquido")
    for trabajador, sueldo in sueldos.items():
        dsc_salud=sueldo*0.07
        dsc_afp=sueldo*0.12
        sueldo_liqui=sueldo-dsc_salud-dsc_afp
        print(f"{trabajador}         {sueldo}         {round(dsc_salud)}       {round(dsc_afp)}        {round(sueldo_liqui)}")
      
while True:
    print("Menú")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion=input()
    if opcion=="1":
        sueldos=asignar_sueldos(trabajadores)
    elif opcion=="2":
        clasificar_sueldos(sueldos)
    elif opcion=="3":
        ver_estadisticas(sueldos)
    elif opcion=="4":
        reporte_sueldos(sueldos)
    else:
        print("Finalizando el programa...")
        print("Desarrollado por moira guzmán")
        print("RUT: 20.496.920-5")
        break