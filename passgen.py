#!/usr/local/bin/python3
import click
import random
import string

def generate_pwd(length, digit, special):
    '''Generate password based on options'''
    seed = string.ascii_letters # base seed string

    if digit: # if digit add digits to the seed
        seed += string.digits
    if special: # if special add special chars to the seed
        seed += string.punctuation

    # generate a random password
    password = ''.join(random.SystemRandom().choice(seed) for i in range(length))
    
    # if numbers in password are less than 3 generate password again
    if  not sum(c.isdigit() for c in password) >= 3 and digit:
        password = generate_pwd(length, digit, special)

    return password # generate password 

def save_pwd(password):
    '''Saves password in passwords.txt'''
    with open('passwords.txt', 'a+') as file: # open text file
        file.write(password)
        file.write('\n')


@click.command()
@click.option('--length', default=8, help='password length')
@click.option('--save/--no-save', default=False, help='save password to text file')
@click.option('--digit/--no-digit', default=False, help='include digits in password')
@click.option('--special/--no-special', default=False, help='include special characters in password')
def main(length, digit, special, save):
    password = generate_pwd(length, digit, special) # generate password
    click.echo(click.style(password, fg="blue")) # display password

    if save:
        save_pwd(password) # save password
        click.secho('Password saved', fg='green')

if __name__ == '__main__':
    main()