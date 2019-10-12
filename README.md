# Encrypted Diary - Python
Project for the 4th Semester Sub -> Open Source Lab Technology

Encrypted	Diary	is	a	fututrproof	data/ﬁle encryptor	and	decryptor created	in	python.

- Enter your data in textbox
- Just	with	a	click	of	a	button	encrypt/decrypt	your	data
- Magic :3

## Features
- Generate	a	base64	encoded	key,and	directly	save	it	in	a	txt	ﬁle.
- Using	the	unique	key	ﬁle	type	and	encrypt	your	data	in	a ‘.encrypted’	ﬁle,export	it	directly	to	the	program	directory.
- Decryption	of	the	‘.encrypted’	ﬁle	will	be	done	if	and	only	if	the same	base64	encoded	key	ﬁle	which	was	used	to	encrypt	the data	is	present	in	the	directory.The	key	is	thus	unique. 
- Erase	all	the	traces	of	your	data	and	all	the	encrypted/decrypted ﬁles	in	a	single	click	of	a	button.

_Encrypted	Diary	is	a	simple	but	a	powerful	tool	to	secure	your	data	form outsider	uses._

## Aim

#### The aim of this project was to explore the possibilites using cryptography and to understand file handling using python.


## Modules Used
Our	program	uses	a	number	of	python	modules	to	work	properly:

1. tkinter	-	For	developing	the	GUI	of	the	program. 
1. cryptography	-	For	all	the	key	generation	to encryption/decryption.
1. datetime	-	To	print	the	date	and	time	in	the	txt	ﬁle. 
1. os.path	-	For	all	the	OS	related	functions	:like	ﬁle	deletion.

## Instalation 

This Encrypted Diary requires [Cryptography](https://cryptography.io/en/latest/) package to run.

Install the package by typing the following in CMD

`python	-m	pip	install	cryptography`

To make sure it is installed correctly, open IDLE and execute :

`import cryptography`

If no errors appeared then the installation is done correctly.

## Functions

The Diary uses the following functions :

- **The	Generate	new	key	button**	generates	new	key
- **Take input in Diary button** accepts	and	collects	what	you have	written	in	the	textbox	and	then	sends	it	to	the	encrypt function	and	thus	an	encrypted	ﬁle	is	created	in	the	directory. 
- **Decrypt the Diary button** opens	the	‘.encrypted’	diary	ﬁle and	exports	it	as	a	text	ﬁle	in	the	same	directory.
- **Erase all traces** button	erases	all	the	traces	,i.e,all	the	ﬁles and	key	ﬁles	of	the	program	from	the	directory(computer). 
- **Exit Button** closes	the	program	window	and	stops	the execution	of	the	program. 

## Contributers 
[Yash Kadam](https://github.com/reziorr)

## To-Do's

- Add	multiple	simultaneous	ﬁle	encryption	and	decryption support 
- Add	a	password	module	so	that	only	the	ones	with	the	correct password	can	access	the	program 
- Add	support	send	the	encrypted	ﬁles	via	email	directly	through the	program 
- Make	the	program	more	secure 
- Add	some	kind	of	backup	methods 

## License 

Free to use : )
