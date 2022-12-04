import re

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


    def validate_fields(self, passport):
        _valid = True

        
        if not (int(passport['byr']) > 1920 and int(passport['byr']) < 2002 and len(passport['byr']) == 4):
            _valid = False  
            
        if not (int(passport['iyr']) > 2010 and int(passport['iyr']) < 2020 and len(passport['iyr']) == 4):
            _valid = False  

        if not (int(passport['eyr']) > 2020 and int(passport['eyr']) < 2030 and len(passport['eyr']) == 4):
            _valid = False  

        if 'in' in passport['hgt']:
            if not (int(passport['hgt']) > 59 and int(passport['hgt']) < 76):
                _valid = False  
        else:
            if not (int(passport['hgt']) > 150 and int(passport['hgt']) < 193):
                _valid = False  

        if not self.validate_hcl(passport['hcl']):
            _valid = False  

        return _valid


    def validate_hcl(string):
        regex = re.compile('#[0-9a-f]{6}\Z', re.I)
        match = regex.match(str(string))
        return bool(match)

    def validate_passport(self, passport):
        if 'cid' in passport: # opcional, ergo no comparo
            passport.pop('cid')
        keys = set([x for x in passport.keys()])
        if keys == self.VALIDATION:
            if self.validate_fields(passport):
                return True
            else:
                print(f'This passport has the required fields but they are not in the right format')
        return False


    def load_passport(self, passport, i):
        self.PASSPORTS[i] = {}
        for key, value in passport.items():
            self.PASSPORTS[i][key] = value


if __name__ == '__main__':
    app = Excercise()