class CuentaBancaria:
    def __init__(self,nro_cuenta,saldo):
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo

    def mostar_saldo(self):
        return f"Saldo: ${self.saldo}"

    def depositar(self,dep):
        if dep > 0:
            self.saldo += dep
        else:
            print("El deposito tiene que ser de $1 o mas")

    def retirar(self,ret):
        if self.saldo > ret:
            self.saldo -= ret
            print(f"Ha retirado {ret}")
        else:
            print(f"Saldo insuficiente")
        


cuenta = CuentaBancaria(4444333322221111,1000)
print(cuenta.mostar_saldo())
cuenta.depositar(500)
print(cuenta.mostar_saldo())
cuenta.retirar(2000)
a