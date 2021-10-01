
def init_db(db):
	# drops DB models, to reset the db
	# db.drop_all()

	#Delete all rows from all tables
	db.session.commit()
	db.session.query(User).delete()
	db.session.query(Quiz).delete()
	db.session.query(QuizStyle).delete()
	db.session.query(Question).delete()
	db.session.query(QuestionChoice).delete()
	db.session.query(QuestionContent).delete()
	db.session.query(UserAnswer).delete()
	db.session.commit()

	db.session.add(User(username="admin", email="admin@admin.admin", admin=True, password_hash=generate_password_hash("admin")))
	db.session.add(User(username="user", email="user@user.user", admin=False, password_hash=generate_password_hash("user")))

	db.session.add(Quiz(quizname="Flag Quiz",creator_id=1,style=1))

	db.session.add(QuizStyle(style_name="Old flag style",template_file="quizStyle1.html"))

	db.session.add(QuizContent(quiz_id=1,text_content="Are you truly aware of the outside world? Do you have what it takes to test your knowledge on the flags of the world? Take our test !",img_content="au.svg"))

	db.session.add(Question(quiz_id=1,question_number=1))
	db.session.add(Question(quiz_id=1,question_number=2))
	db.session.add(Question(quiz_id=1,question_number=3))
	db.session.add(Question(quiz_id=1,question_number=4))
	db.session.add(Question(quiz_id=1,question_number=5))
	db.session.add(Question(quiz_id=1,question_number=6))
	db.session.add(Question(quiz_id=1,question_number=7))
	db.session.add(Question(quiz_id=1,question_number=8))
	db.session.add(Question(quiz_id=1,question_number=9))
	db.session.add(Question(quiz_id=1,question_number=10))

	db.session.add(QuestionContent(question_id=1,text_content="What country flag is this?",img_content="flag01.svg"))
	db.session.add(QuestionContent(question_id=2,text_content="What country flag is this?",img_content="flag02.svg"))
	db.session.add(QuestionContent(question_id=3,text_content="What country flag is this?",img_content="flag03.svg"))
	db.session.add(QuestionContent(question_id=4,text_content="What country flag is this?",img_content="flag04.svg"))
	db.session.add(QuestionContent(question_id=5,text_content="What country flag is this?",img_content="flag05.svg"))
	db.session.add(QuestionContent(question_id=6,text_content="What country flag is this?",img_content="flag06.svg"))
	db.session.add(QuestionContent(question_id=7,text_content="What country flag is this?",img_content="flag07.svg"))
	db.session.add(QuestionContent(question_id=8,text_content="What country flag is this?",img_content="flag08.svg"))
	db.session.add(QuestionContent(question_id=9,text_content="What country flag is this?",img_content="flag09.svg"))
	db.session.add(QuestionContent(question_id=10,text_content="What country flag is this?",img_content="flag10.svg"))

	#Question choices for flag quiz
	db.session.add(QuestionChoice(question_id=1,choice_number=1,choice_content="Namibia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=1,choice_number=2,choice_content="Turks and Caicos Islands",choice_correct=False))
	db.session.add(QuestionChoice(question_id=1,choice_number=3,choice_content="Mongolia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=1,choice_number=4,choice_content="Saint Pierre and Miquelon",choice_correct=True))

	db.session.add(QuestionChoice(question_id=2,choice_number=1,choice_content="French Polynesia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=2,choice_number=2,choice_content="Maldives",choice_correct=False))
	db.session.add(QuestionChoice(question_id=2,choice_number=3,choice_content="Djibouti",choice_correct=False))
	db.session.add(QuestionChoice(question_id=2,choice_number=4,choice_content="Botswana",choice_correct=True))

	db.session.add(QuestionChoice(question_id=3,choice_number=1,choice_content="Anguilla",choice_correct=False))
	db.session.add(QuestionChoice(question_id=3,choice_number=2,choice_content="Lesotho",choice_correct=False))
	db.session.add(QuestionChoice(question_id=3,choice_number=3,choice_content="Western Sahara",choice_correct=False))
	db.session.add(QuestionChoice(question_id=3,choice_number=4,choice_content="Gabon",choice_correct=True))

	db.session.add(QuestionChoice(question_id=4,choice_number=1,choice_content="Heard Island and McDonald Islands",choice_correct=False))
	db.session.add(QuestionChoice(question_id=4,choice_number=2,choice_content="American Samoa",choice_correct=False))
	db.session.add(QuestionChoice(question_id=4,choice_number=3,choice_content="Zimbabwe",choice_correct=False))
	db.session.add(QuestionChoice(question_id=4,choice_number=4,choice_content="Puerto Rico",choice_correct=True))

	db.session.add(QuestionChoice(question_id=5,choice_number=1,choice_content="Isle of Man",choice_correct=False))
	db.session.add(QuestionChoice(question_id=5,choice_number=2,choice_content="South Georgia and the South Sandwich Islands",choice_correct=False))
	db.session.add(QuestionChoice(question_id=5,choice_number=3,choice_content="Iran",choice_correct=False))
	db.session.add(QuestionChoice(question_id=5,choice_number=4,choice_content="Pitcairn",choice_correct=True))

	db.session.add(QuestionChoice(question_id=6,choice_number=1,choice_content="Korea (Republic of)",choice_correct=False))
	db.session.add(QuestionChoice(question_id=6,choice_number=2,choice_content="Cayman Islands",choice_correct=False))
	db.session.add(QuestionChoice(question_id=6,choice_number=3,choice_content="Myanmar",choice_correct=False))
	db.session.add(QuestionChoice(question_id=6,choice_number=4,choice_content="Kiribati",choice_correct=True))

	db.session.add(QuestionChoice(question_id=7,choice_number=1,choice_content="Slovenia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=7,choice_number=2,choice_content="Brunei",choice_correct=False))
	db.session.add(QuestionChoice(question_id=7,choice_number=3,choice_content="Saint Martin (French part)",choice_correct=False))
	db.session.add(QuestionChoice(question_id=7,choice_number=4,choice_content="Suriname",choice_correct=True))

	db.session.add(QuestionChoice(question_id=8,choice_number=1,choice_content="Finland",choice_correct=False))
	db.session.add(QuestionChoice(question_id=8,choice_number=2,choice_content="Fiji",choice_correct=False))
	db.session.add(QuestionChoice(question_id=8,choice_number=3,choice_content="Bahamas",choice_correct=False))
	db.session.add(QuestionChoice(question_id=8,choice_number=4,choice_content="Colombia",choice_correct=True))

	db.session.add(QuestionChoice(question_id=9,choice_number=1,choice_content="Rwanda",choice_correct=False))
	db.session.add(QuestionChoice(question_id=9,choice_number=2,choice_content="Georgia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=9,choice_number=3,choice_content="Palestine",choice_correct=False))
	db.session.add(QuestionChoice(question_id=9,choice_number=4,choice_content="Czechia",choice_correct=True))

	db.session.add(QuestionChoice(question_id=10,choice_number=1,choice_content="Afghanistan",choice_correct=False))
	db.session.add(QuestionChoice(question_id=10,choice_number=2,choice_content="Indonesia",choice_correct=False))
	db.session.add(QuestionChoice(question_id=10,choice_number=3,choice_content="Angola",choice_correct=False))
	db.session.add(QuestionChoice(question_id=10,choice_number=4,choice_content="Jersey",choice_correct=True))

	db.session.add(Quiz(quizname="Language Quiz",creator_id=1,style=2))

	db.session.add(QuizStyle(style_name="Language quiz style",template_file="quizStyle2.html"))

	db.session.add(QuizContent(quiz_id=2,text_content="How much do you know about world culture, information and languages?",img_content="people-banner.png"))

	db.session.add(Question(quiz_id=2,question_number=1))
	db.session.add(Question(quiz_id=2,question_number=2))
	db.session.add(Question(quiz_id=2,question_number=3))
	db.session.add(Question(quiz_id=2,question_number=4))
	db.session.add(Question(quiz_id=2,question_number=5))
	db.session.add(Question(quiz_id=2,question_number=6))
	db.session.add(Question(quiz_id=2,question_number=7))
	db.session.add(Question(quiz_id=2,question_number=8))
	db.session.add(Question(quiz_id=2,question_number=9))
	db.session.add(Question(quiz_id=2,question_number=10))

	db.session.add(QuestionContent(question_id=11,text_content="What is the Official Language of Taiwan",img_content="taiwan-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=12,text_content="What is the Official Language of Australia",img_content="australia-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=13,text_content="What is the Official Language of Norway",img_content="norway-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=14,text_content="What is the Official Language of Colombia",img_content="colombia-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=15,text_content="What is the Official Language of Pakistan",img_content="pakistan-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=16,text_content="What is the Official Language of Ukraine",img_content="ukraine-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=17,text_content="What is the Official Language of Malaysia",img_content="malaysia-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=18,text_content="What is the Official Language of Mexico",img_content="mexico-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=19,text_content="What is the Official Language of Iran",img_content="iran-languageQuiz.jpg"))
	db.session.add(QuestionContent(question_id=20,text_content="What is the Official Language of Indonesia",img_content="indonesia-languageQuiz.jpg"))

	db.session.add(QuestionChoice(question_id=11,choice_number=1,choice_content="Taiwanese",choice_correct=False))
	db.session.add(QuestionChoice(question_id=11,choice_number=2,choice_content="Japanese",choice_correct=False))
	db.session.add(QuestionChoice(question_id=11,choice_number=3,choice_content="Mandarin",choice_correct=True))
	db.session.add(QuestionChoice(question_id=11,choice_number=4,choice_content="Cantonese",choice_correct=False))

	db.session.add(QuestionChoice(question_id=12,choice_number=1,choice_content="English",choice_correct=True))
	db.session.add(QuestionChoice(question_id=12,choice_number=2,choice_content="German",choice_correct=False))
	db.session.add(QuestionChoice(question_id=12,choice_number=3,choice_content="Korean",choice_correct=False))
	db.session.add(QuestionChoice(question_id=12,choice_number=4,choice_content="Russian",choice_correct=False))

	db.session.add(QuestionChoice(question_id=13,choice_number=1,choice_content="German",choice_correct=False))
	db.session.add(QuestionChoice(question_id=13,choice_number=2,choice_content="Spanish",choice_correct=False))
	db.session.add(QuestionChoice(question_id=13,choice_number=3,choice_content="English",choice_correct=False))
	db.session.add(QuestionChoice(question_id=13,choice_number=4,choice_content="Romani",choice_correct=True))

	db.session.add(QuestionChoice(question_id=14,choice_number=1,choice_content="Spanish",choice_correct=True))
	db.session.add(QuestionChoice(question_id=14,choice_number=2,choice_content="Irish",choice_correct=False))
	db.session.add(QuestionChoice(question_id=14,choice_number=3,choice_content="Dutch",choice_correct=False))
	db.session.add(QuestionChoice(question_id=14,choice_number=4,choice_content="French",choice_correct=False))

	db.session.add(QuestionChoice(question_id=15,choice_number=1,choice_content="Perish",choice_correct=False))
	db.session.add(QuestionChoice(question_id=15,choice_number=2,choice_content="Hindi",choice_correct=False))
	db.session.add(QuestionChoice(question_id=15,choice_number=3,choice_content="Arabic",choice_correct=False))
	db.session.add(QuestionChoice(question_id=15,choice_number=4,choice_content="Urdu",choice_correct=True))

	db.session.add(QuestionChoice(question_id=16,choice_number=1,choice_content="Ukrainian",choice_correct=True))
	db.session.add(QuestionChoice(question_id=16,choice_number=2,choice_content="Russian",choice_correct=False))
	db.session.add(QuestionChoice(question_id=16,choice_number=3,choice_content="Greenlandic",choice_correct=False))
	db.session.add(QuestionChoice(question_id=16,choice_number=4,choice_content="Galician",choice_correct=False))

	db.session.add(QuestionChoice(question_id=17,choice_number=1,choice_content="Malaysian",choice_correct=False))
	db.session.add(QuestionChoice(question_id=17,choice_number=2,choice_content="Malayense",choice_correct=False))
	db.session.add(QuestionChoice(question_id=17,choice_number=3,choice_content="Mandarin",choice_correct=False))
	db.session.add(QuestionChoice(question_id=17,choice_number=4,choice_content="Malay",choice_correct=True))

	db.session.add(QuestionChoice(question_id=18,choice_number=1,choice_content="Spanish",choice_correct=True))
	db.session.add(QuestionChoice(question_id=18,choice_number=2,choice_content="Mexian",choice_correct=False))
	db.session.add(QuestionChoice(question_id=18,choice_number=3,choice_content="Portuguese",choice_correct=False))
	db.session.add(QuestionChoice(question_id=18,choice_number=4,choice_content="Welsh",choice_correct=False))

	db.session.add(QuestionChoice(question_id=19,choice_number=1,choice_content="Arabic",choice_correct=False))
	db.session.add(QuestionChoice(question_id=19,choice_number=2,choice_content="Hebrew",choice_correct=False))
	db.session.add(QuestionChoice(question_id=19,choice_number=3,choice_content="Persian",choice_correct=True))
	db.session.add(QuestionChoice(question_id=19,choice_number=4,choice_content="Hindi",choice_correct=False))

	db.session.add(QuestionChoice(question_id=20,choice_number=1,choice_content="Malay",choice_correct=False))
	db.session.add(QuestionChoice(question_id=20,choice_number=2,choice_content="Indonesia",choice_correct=True))
	db.session.add(QuestionChoice(question_id=20,choice_number=3,choice_content="Mandarin",choice_correct=False))
	db.session.add(QuestionChoice(question_id=20,choice_number=4,choice_content="Thai",choice_correct=False))
	db.session.commit()