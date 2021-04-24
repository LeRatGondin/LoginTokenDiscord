"""
MIT License

Copyright (c) 2021 LeRatGondin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from selenium import webdriver
import os
def main(_token):
    try:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome('chromedriver.exe', options=opts)
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }   
               """
        driver.get("https://discordapp.com/login")
        driver.execute_script(script+f'\nlogin("{_token}")')
    except:
        print("Une erreur est survenue la page a été fermée")    
        
    
    
if __name__ == '__main__':
    os.system('cls')
    token = input("""
     _                 _         _______    _                   _____  _                       _ 
    | |               (_)       |__   __|  | |                 |  __ \(_)                     | |
    | |     ___   __ _ _ _ __      | | ___ | | _____ _ __      | |  | |_ ___  ___ ___  _ __ __| |
    | |    / _ \ / _` | | '_ \     | |/ _ \| |/ / _ \ '_ \     | |  | | / __|/ __/ _ \| '__/ _` |
    | |____ (_) | (_| | | | | |    | | (_) |   <  __/ | | |    | |__| | \__ \ (__ (_) | | | (_| |
    |______\___/ \__, |_|_| |_|    |_|\___/|_|\_\___|_| |_|    |_____/|_|___/\___\___/|_|  \__,_|
                  __/ |                                                                       
                 |___/                                 
    by LeRatGondin

    Entrez le token : """)
    main(token)