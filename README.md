# ListingFiles
## 💻 About this project (sobre este projeto)
:us: This project aimed to create an app executable able to list all files in a folder.

:brazil: Este projeto teve por objetivo criar uma aplicação .exe capaz de listar todos os arquivos em uma pasta.

---
## ⚙️ Project demonstration (demontração do projeto)
The algorithm maps a directory and list its files names and sizes on a csv file (listingfiles.csv).
There are four types of executables (and its codes). They only differ on size and if they have, or not, a graphic interface so users can see the process running.

- Name: simplelistingfiles_wo_interface.exe
- Executable size: 6.6 mb
- Description:  This executable (and its code) is light because it does not have Graphic interface for users and does not use Pandas (to create DataFrame) or Numpy (to manipulate data).

<p align="center"> <src="./assets/checkbox-toggle.gif" width="400px">

- Name: simplelistingfiles_w_interface.exe
- Executable size: 9.4 mb
- Description: This executable (and its code) uses TKinter to create a Graphic interface for users (while processing, using threading) that makes it a little heavier. However, it is still light because it does not use Pandas (to create DataFrame) or Numpy (to manipulate data).

<p align="center"> <src="./assets/checkbox-toggle.gif" width="400px">
 
- Name: listingfiles_wo_interface.exe
- Executable size: 27.6 mb
- Description: This executable (and its code) although it does not create a Graphic interface for users, it uses Pandas (to create DataFrame and CSV) that makes the program heavy.

<p align="center"> <src="./assets/checkbox-toggle.gif" width="400px">
 
- Name: listingfiles_w_interface
- Executable size: 30.3 mb
- Description: This executable (and its code) is the heaviest, bacause it uses TKinter to create a Graphic interface for users (while processing, using threading), as well as, Pandas (to create DataFrame and CSV). It was the first version of app that was adjusted until has it size reduced five times (from 30 mb to 6mb), by removing Pandas, Tkinter, and Threading).

<p align="center"> <src="./assets/checkbox-toggle.gif" width="400px">

---
	
## 💡 Knowledge acquired (conhecimentos adquiridos)

- During this project, I learned:
  - pending to be written;
  - pending to be written; and
  - pending to be written.

---

## 🚀 How to execute this project (como executar este projeto)

There are two ways to execute this app:
- Using one of the four apps available at the Executable folder:
  - Choose and download one executable app;
  - Place the app on the folder that you what to list the names and sizes of files there; and
  - Double click the app to be executed (the .csv listing the files will be created at the folder inspected.

- Using one of the four codes available at the Code folder:
  - To run the code it is recommended to use an IDE, such as Pycharm;
  - When played, the code will list the name and size of files from where it will be running; and
  - The .csv listing the files will be created at the folder inspected.

### 🎲 Requirements (requisitos)

There is no recommendation to run the executable apps.

To run the code, it is recommended to install the following Python Packaged:
- csv;
- hurry.filesize;
- pandas;
- pathlib;
- threading;
- tkinter; and
- os

#### Running the codes (rodando os códigos)

```bash

# Clone this repository
$ git@github.com:rosadigital/listingfiles.git
# Open the repository on pycharm

```

---

## 🦸 Author (autor)


Felipe Rosa on [LinkedIn](https://www.linkedin.com/in/felipe-rosa/)

---

## 📝 License (licença)

This project is licensed under [MIT](./LICENSE).

Este projeto esta sobe a licença [MIT](./LICENSE).

Made with ❤️ by Felipe Rosa 👋🏽 [Contact here!](https://www.linkedin.com/in/felipe-rosa/)

Feito com ❤️ por Felipe Rosa 👋🏽 [Entre em contato!](https://www.linkedin.com/in/felipe-rosa/)

--
