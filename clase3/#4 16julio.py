monto = float(input("Ingrese el monto de la compra: "))
if monto > 100:
    descuento = monto * 0.10
    monto_final = monto - descuento
    print(f"Se aplicó un 10% de descuento. Total a pagar: {monto_final: }")
else:
    print(f"Total a pagar: {monto: }")