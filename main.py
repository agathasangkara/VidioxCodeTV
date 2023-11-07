try:
    import requests as r, os, sys as s
    from colorama import Fore as x
except Exception as error:
    print(" Installing Library Python")
    os.system("pip install -r requirements.txt")


class Vidio:

    def __init__(self):
        self.red = x.RED
        self.green = x.GREEN
        self.white = x.WHITE
        self.password = "chsangkara" # setting our password here
        self.api = r.Session()
    
    def create_account(self, code):
        headers = {
            "Content-Type":"application/json"
        }
        data = {
            "code":code,
            "password":self.password
        }

        signup = self.api.post("https://cars.dimanasye.my.id/api/v1/vidio", json=data, headers=headers)
        if "error" in signup.text:
            print(f"\n {signup.json()['email']} | {signup.json()['password']} | {self.red}{signup.json()['data']['error_message']}{self.white}\n")
            return False
        elif signup.json()["data"]["success"] == True:
            print(f"\n {signup.json()['email']} | {signup.json()['password']} | {self.green}Account successfully Premium{self.white}\n")
            with open('vidio.txt', 'a') as f:
                f.write(f"{signup.json()['email']} | {signup.json()['password']}\n")
            return True
        else:
            None
            return False

class Generate:

    os.system('cls' if os.name == "nt" else 'clear')
    print(f"""{x.RED}                                  
     .-.  .-.      .'   .-.       
_.;  :    `-' .-..'     `-' .-.   
 ;   ;   ;'  :   ;     ;'  ;   ;' {x.WHITE} Vidio Creator Platinum Code TV {x.RED}
 `._.'_.;:._.`:::'`._.;:._.`;;'   
                                  """)
    count = 0
    berapa = int(input(f"\n {x.WHITE}Berapa Account : "))
    print(f'\n Ready Generate Vidio Platinum {berapa} Account\n')
    while count < berapa:
        try:
            while True:
                code = int(input(" Code TV : "))
                try:
                    if len(str(code)) == 6:
                        create = Vidio().create_account(code)
                        if create == True:
                            count += 1
                            if count == berapa:
                                print(f" {x.GREEN}Operation Successfully XD")
                        elif create == False:
                            None
                            break
                    else:
                        continue
                except ValueError:
                    None
        except Exception as e:
            s.exit(f" Error : {e}\n")


if __name__ == "__main__":
    Generate()
