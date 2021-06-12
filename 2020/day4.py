class Excercise():
    PASSPORTS = {}
    VALIDATION = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    VALID_PASSPORTS = set()


    def __init__(self):
        self.read_passports()
        self.validate_passports()
        print(f'Hay un total de {len(self.VALID_PASSPORTS)} validos sobre {len(self.PASSPORTS)} pasaportes')
        # print(self.get_passports())
        # print(self.get_validated_passports())


    def read_passports(self):
        f = open('passports', 'r')
        data = f.readlines()

        i = 0
        passport = {}
        for line in data:
            i += 1
            if line == '\n':
                print('---')
                self.load_passport(passport, i)
                passport = {}
            else:
                print(f'Imprimo linea con (:): {line}')
                count = 0
                line = line.split(' ')
                explode = [x.strip().split(':') for x in line]

                for key in explode:
                    passport[key[0]] = key[1]

  
    def get_passports(self):
        return self.PASSPORTS 


    def get_validated_passports(self):
        return self.VALID_PASSPORTS


    def validate_passports(self):
        for id, passport in self.PASSPORTS.items():
            if self.validate_passport(passport):
                print(f'Passport {passport["pid"]} is valid!')
                self.VALID_PASSPORTS.add(passport['pid'])

    
    def validate_passport(self, passport):
        if 'cid' in passport: # opcional, ergo no comparo
            passport.pop('cid')
        keys = set([x for x in passport.keys()])
        if keys == self.VALIDATION:
            return True

        return False


    def load_passport(self, passport, i):
        self.PASSPORTS[i] = {}
        for key, value in passport.items():
            self.PASSPORTS[i][key] = value


if __name__ == '__main__':
    app = Excercise()