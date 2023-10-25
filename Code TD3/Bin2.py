 
def binairedecimal(ficelle):
        x = len(ficelle) - 1
        n = 0
        res = 0
        while x != -1:
            if ficelle[x] == "1":
                res = res + 2 ** n
            n = n + 1
            x = x - 1
        return res

def decimalbinaire(ficelle):
        quotient = int(ficelle)
        res = ""
        while quotient != 1:
            res = res + str(quotient % 2)
            quotient = quotient // 2
        res = res + "1"
        return res

def binairehexa(ficelle):
        res = ""
        while len(ficelle) > 4:
            res = ficelle[-4:] + res  
            ficelle = ficelle[:-4]
        res = ficelle + res  
        while len(res) % 4 != 0:
            res = "0" + res 
        return res

def hexabinaire(ficelle):
        res = ""
        for x in range(len(ficelle)):
            res = res + format(int(ficelle[x], 16), '04b')
        return res

def decimalhexa(ficelle):
        return binairehexa(decimalbinaire(ficelle))

def hexadecimal(ficelle):
        return str(hex(int(ficelle)))

def decimaloctal(ficelle):
        return oct(int(ficelle))

def octal(ficelle):
        return str(oct(int(ficelle)))


###########################################################################
################TD3 : Entiers signés , complément à 2######################
###########################################################################
while True : 
    def inverse_binaire(binaire):
        if len(binaire) != 8:
            raise ValueError("La chaîne binaire doit contenir exactement 8 bits.")
        inverse = ""
        for bits in binaire:
            if bits == '0':
                inverse += '1'
            elif bits == '1':
                inverse += '0'
            else:
                raise ValueError("La chaîne binaire ne doit contenir que des 0 et des 1.")
        return inverse

    def compl_a_deux(Cad):
        if not isinstance(Cad, int):
            raise ValueError("Cad doit être un nombre décimal.")

        if Cad < 0:
            num_bits = 8
            max_value = 2 ** num_bits
            Cad = Cad + max_value

        binaire = format(Cad, '08b')
        return binaire

    def compl_a_deux_lect(Cadl):
        completion_lecture = ''
        for i in Cadl:
            if i == '1':
                completion_lecture = '0' + completion_lecture
            elif i == '0':
                completion_lecture = '1' + completion_lecture
        return completion_lecture

    def complement_a_deux_calculator(decimal_number, num_bits):
        binary_representation = format(decimal_number, f'0{num_bits}b')
        complement_a_un = ''.join(['1' if bits == '0' else '0' for bits in binary_representation])
        complement_a_deux = ''
        carry = 1
        for bits in complement_a_un[::-1]:
            if bits == '0':
                complement_a_deux = ('1' if carry == 1 else '0') + complement_a_deux
                carry = 0
            else:
                complement_a_deux = ('0' if carry == 1 else '1') + complement_a_deux
        return complement_a_deux

    def add_bin(Binaire1, Binaire2):
        if len(Binaire1) != 8 or len(Binaire2) != 8:
            raise ValueError("Les nombres binaires doivent avoir une longueur de 8 bits.")

        carry = 0
        result = ['0'] * 8
        for i in range(7, -1, -1):
            bits1 = int(Binaire1[i])
            bits2 = int(Binaire2[i])
            somme_temp = bits1 + bits2 + carry
            result[i] = str(somme_temp % 2)
            carry = somme_temp // 2
        if carry:
            result = [str(carry)] + result
        resultat = ''.join(result)
        return resultat

    operation = input("Entrez l'opération : ")


    try:
        resultat_decimal = eval(operation)
        if type(resultat_decimal) == int:
            complement1 = compl_a_deux(resultat_decimal)
            print(f"Complément à deux de {resultat_decimal}: {complement1}")
            print(f"Résultat en décimal : {resultat_decimal}")
        else:
            print("L'opération n'est pas une expression valide.")
    except:
        print("L'opération n'est pas une expression valide.")
