# app/utils/validadores.py

def validar_ruc_ecuador(ruc: str) -> str:
    # -------- VALIDACIONES BÁSICAS --------
    if len(ruc) != 13:
        raise ValueError("El RUC debe tener exactamente 13 dígitos.")

    if not ruc.isdigit():
        raise ValueError("El RUC solo puede contener números.")

    provincia = int(ruc[0:2])
    if not (1 <= provincia <= 24 or provincia == 30):
        raise ValueError("Código de provincia inválido en el RUC.")

    tercer = int(ruc[2])

    if tercer < 6:
        tipo = "natural"
    elif tercer == 6:
        tipo = "publica"
    elif tercer == 9:
        tipo = "privada"
    else:
        raise ValueError(
            "El tercer dígito del RUC no es válido. Debe ser 0-5 (natural), 6 (pública) o 9 (privada)."
        )

    if ruc[10:13] == "000":
        raise ValueError("Los últimos tres dígitos del RUC no pueden ser '000'.")

    # ------------- DÍGITO VERIFICADOR ---------------
    digito_verificador = int(ruc[9])
    cuerpo = ruc[:10]

    if tipo == "natural":
        coef = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        total = 0
        for i in range(9):
            mult = int(cuerpo[i]) * coef[i]
            total += mult - 9 if mult >= 10 else mult

        digito_ok = 10 - (total % 10)
        digito_ok = 0 if digito_ok == 10 else digito_ok

    elif tipo == "publica":
        coef = [3, 2, 7, 6, 5, 4, 3, 2]
        total = sum(int(cuerpo[i]) * coef[i] for i in range(8))

        digito_ok = 11 - (total % 11)
        digito_ok = 0 if digito_ok == 11 else digito_ok

    else:  # privada
        coef = [4, 3, 2, 7, 6, 5, 4, 3, 2]
        total = sum(int(cuerpo[i]) * coef[i] for i in range(9))

        digito_ok = 11 - (total % 11)
        digito_ok = 0 if digito_ok == 11 else digito_ok

    # Validar DV
    if digito_ok != digito_verificador:
        raise ValueError(f"Dígito verificador incorrecto para RUC tipo {tipo}.")

    return ruc
